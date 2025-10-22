import glob
import os
import shutil
import subprocess
import time
import traceback

from loguru import logger

from .package_manager import PackageManager

class AppsManager:
    @staticmethod
    @staticmethod
    def configure_fish() -> None:
        logger.info("Starting the Fish shell configuration process")
        try:
            subprocess.run(["fish", "--version"], check=True, capture_output=True)
            fish_exists = True
        except FileNotFoundError:
            fish_exists = False

        if not fish_exists:
            PackageManager.install_packages(packages_list=["fish"])

        try:
            subprocess.run(["fish", "-c", "fisher install jorgebucaran/nvm.fish"], check=True)
            logger.success("nvm has been successfully installed via fisher!")
        except Exception:
            logger.error(f"Error installing nvm: {traceback.format_exc()}")

        try:
            subprocess.run(["bash", "-c", "curl -LsSf https://astral.sh/uv/install.sh | sh"], check=True)
            logger.success("uv has been successfully installed!")
        except Exception:
            logger.error(f"Error installing uv: {traceback.format_exc()}")
        

    @staticmethod
    def configure_code() -> str:
        try:
            result = subprocess.run(
                ["code", "--version"], capture_output=True, text=True
            )
            code_exists = result.returncode == 0
        except FileNotFoundError:
            code_exists = False

        if not code_exists:
            PackageManager.install_packages(packages_list=["code"])

    @staticmethod
    def configure_normcap() -> None:
        logger.info("Starting the NormCap installation process")
        try:
            subprocess.run(["flatpak", "remote-add", "--if-not-exists", "flathub", "https://flathub.org/repo/flathub.flatpakrepo"], check=True)
            subprocess.run(["flatpak", "install", "flathub", "com.github.dynobo.normcap", "--noninteractive"], check=True)
            logger.success("NormCap has been successfully installed!")
        except Exception:
            logger.error(f"Error installing NormCap: {traceback.format_exc()}")

    @staticmethod
    def configure_spotify() -> str:
        try:
            result = subprocess.run(
                ["spotify", "--version"], capture_output=True, text=True
            )
            spotify_exists = result.returncode == 0
        except FileNotFoundError:
            spotify_exists = False

        if not spotify_exists:
            PackageManager.install_packages(packages_list=["spotify"])
            try:
                subprocess.run(
                    ["bash", "-c", "curl -sSL https://spotx-official.github.io/run.sh | bash"],
                    check=True
                )
                logger.success("SpotX has been successfully installed!")
            except Exception:
                logger.error(f"Error installing SpotX: {traceback.format_exc()}")
        return "Spotify and SpotX installation attempted."

    @staticmethod
    def configure_zen_browser() -> None:
        logger.info("Start installing Zen Browser")

        try:
            subprocess.run(["yay", "-S", "zen-browser-bin", "--noconfirm"], check=True)
            logger.success("Zen Browser has been successfully installed!")
        except Exception:
            logger.error(f"Error installing Zen Browser: {traceback.format_exc()}")

    @staticmethod
    def configure_sddm() -> None:
        logger.info("Starting the SDDM installation process")
        theme_name = "billarch"
        sddm_config_file = "/etc/sddm.conf"
        temp_sddm_config_path = "/tmp/sddm.conf"
        path_to_theme = f"/usr/share/sddm/themes/{theme_name}"
        avatars_folder = "/var/lib/AccountsService/icons/"

        with open(temp_sddm_config_path, "w") as file:
            file.write(
                f"[Theme]\nCurrent={theme_name}\nFacesDir={avatars_folder}\nCursorTheme=Bibata-Modern-Classic\n"
            )

        try:
            username = subprocess.check_output("whoami", text=True).strip()
            subprocess.run(
                [
                    "sudo",
                    "mv",
                    "./misc/.face.icon",
                    f"{avatars_folder}{username}.face.icon",
                ],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["sudo", "mv", temp_sddm_config_path, sddm_config_file], check=True
            )
            subprocess.run(
                ["sudo", "cp", "-r", "./misc/sddm_theme", path_to_theme], check=True
            )
            logger.success("The SDDM theme has been successfully installed!")
        except Exception:
            logger.error(
                f"The installation of the SDDM theme failed: {traceback.format_exc()}"
            )

    @staticmethod
    def configure_grub() -> None:
        logger.info("Starting the GRUB installation process")
        grub_config_file = "/etc/default/grub"
        temp_grub_config_path = "/tmp/grub"
        path_to_theme = "/boot/grub/themes/billarch"
        grub_theme_setting = f"GRUB_THEME={path_to_theme}/theme.txt\n"

        if not os.path.exists(grub_config_file):
            logger.error("GRUB is not installed. Skipping theme installation.")
            return

        with open(grub_config_file, "r") as file:
            grub_config = [
                line for line in file.readlines() if not line.startswith("GRUB_THEME")
            ]

        grub_config.append(grub_theme_setting)

        with open(temp_grub_config_path, "w") as file:
            file.writelines(grub_config)

        try:
            subprocess.run(
                ["sudo", "cp", "-r", "./misc/grub_theme", path_to_theme], check=True
            )
            subprocess.run(
                ["sudo", "mv", temp_grub_config_path, grub_config_file], check=True
            )
            subprocess.run(["sudo", "update-grub"], check=True)
            logger.success("The GRUB theme has been successfully installed!")
        except Exception:
            logger.error(
                f"The installation of the grub theme failed: {traceback.format_exc()}"
            )
