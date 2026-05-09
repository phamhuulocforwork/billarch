function cleanup --description "Audit/Cleanup Arch-based system safely"
    argparse 'a/audit' 'c/clean' 'd/deep' 'f/flatpak-only' 'y/yes' 'h/help' -- $argv
    or return 1

    if set -q _flag_help
        echo "Usage: arch_cleanup [--audit] [--clean] [--deep] [--flatpak-only] [--yes]"
        echo "  --audit         Show what can be cleaned"
        echo "  --clean         Run cleanup"
        echo "  --deep          Stronger cleanup (implies --clean)"
        echo "  --flatpak-only  Cleanup Flatpak only"
        echo "  --yes           Non-interactive orphan removal"
        return 0
    end

    set -l do_audit 0
    set -l do_clean 0
    set -l do_deep 0
    set -l flatpak_only 0
    set -l assume_yes 0

    set -q _flag_audit; and set do_audit 1
    set -q _flag_clean; and set do_clean 1
    set -q _flag_deep; and set do_deep 1; and set do_clean 1
    set -q _flag_flatpak_only; and set flatpak_only 1; and set do_clean 1
    set -q _flag_yes; and set assume_yes 1

    if test $do_audit -eq 0 -a $do_clean -eq 0
        set do_audit 1
    end

    if test $do_audit -eq 1
        echo "== OS =="
        if test -r /etc/os-release
            grep -E '^(PRETTY_NAME|ID|ID_LIKE)=' /etc/os-release
        end
        echo

        echo "== Disk usage =="
        df -h /
        echo

        if test $flatpak_only -eq 0
            echo "== Pacman cache =="
            du -sh /var/cache/pacman/pkg 2>/dev/null
            echo

            echo "== Orphan packages =="
            set -l orphans (pacman -Qdtq 2>/dev/null)
            if test (count $orphans) -gt 0
                echo "Count: "(count $orphans)
                printf '%s\n' $orphans
            else
                echo "No orphan packages."
            end
            echo

            echo "== Journal usage =="
            journalctl --disk-usage 2>/dev/null
            echo

            if type -q yay
                echo "== AUR orphan packages (yay) =="
                set -l aur_orphans (yay -Qdtq 2>/dev/null)
                if test (count $aur_orphans) -gt 0
                    echo "Count: "(count $aur_orphans)
                    printf '%s\n' $aur_orphans
                else
                    echo "No AUR orphans."
                end
                echo
            end
        end

        echo "== Flatpak apps =="
        if type -q flatpak
            set -l flatpak_apps (flatpak list --app --columns=application 2>/dev/null)
            if test (count $flatpak_apps) -gt 0
                echo "Count: "(count $flatpak_apps)
                printf '%s\n' $flatpak_apps
            else
                echo "No flatpak apps."
            end
            echo

            echo "== Flatpak unused (dry-run) =="
            flatpak uninstall --unused --noninteractive --dry-run
        else
            echo "flatpak not installed"
        end
        echo
    end

    if test $do_clean -eq 1
        if test $flatpak_only -eq 0
            echo "== Cleaning pacman cache (keep 2 versions) =="
            if type -q paccache
                sudo paccache -rk2
                sudo paccache -ruk0
            else
                echo "paccache not found. Install pacman-contrib."
            end

            echo
            echo "== Cleaning old journals (keep 14 days) =="
            sudo journalctl --vacuum-time=14d

            echo
            set -l orphans (pacman -Qdtq 2>/dev/null)
            if test (count $orphans) -gt 0
                set -l remove_orphans 0
                if test $assume_yes -eq 1
                    set remove_orphans 1
                else
                    read -l -P "Remove orphan packages? [y/N] " ans
                    if string match -qi "y" -- $ans
                        set remove_orphans 1
                    end
                end

                if test $remove_orphans -eq 1
                    sudo pacman -Rns $orphans
                else
                    echo "Skip orphan removal."
                end
            else
                echo "No orphan packages to remove."
            end

            if type -q yay
                echo
                echo "== Cleaning yay cache =="
                yay -Sc --noconfirm
            end
        end

        echo
        echo "== Cleaning Flatpak unused runtimes =="
        if type -q flatpak
            flatpak uninstall --unused -y
        else
            echo "flatpak not installed"
        end
    end

    if test $do_deep -eq 1 -a $flatpak_only -eq 0
        echo
        echo "== Deep mode: keep only 1 package version in cache =="
        if type -q paccache
            sudo paccache -rk1
        else
            echo "paccache not found. Install pacman-contrib."
        end
    end

    if test $do_clean -eq 1
        echo
        echo "Done. Run: arch_cleanup --audit"
    end
end
