from utils.schemes import DistributionPackages, PackageInfo, Packages

BASE = Packages(
	pacman=DistributionPackages(
		common=[
			"pacman-contrib", "libnotify", "ffmpeg","ffmpegthumbnailer", "jq", "parallel", "kitty", "fastfetch", "lsd", "bat", "brightnessctl", 
			"automake", "blueman", "bluez", "bluez-utils", "dunst", "fakeroot", "fish", "fisher", "dpkg", "gcc", "git", "btop", 
			"micro", "mat2", "nemo", "papirus-icon-theme", "pavucontrol", "pamixer", "pipewire", "pipewire-pulse", "pipewire-audio",
			"pipewire-jack", "pipewire-alsa", "wireplumber", "python-pyalsa", "ranger", "redshift", "reflector", "sudo", "tree", "unrar",
			"zip", "unzip", "uthash", "ark", "cmake", "clang", "gzip", "imagemagick",
			"make", "openssh", "shellcheck", "vlc", "loupe", "usbutils", "openvpn", "networkmanager-openvpn", "gparted",
			"sshfs", "wget", "netctl", "ttf-ubuntu-nerd", "ttf-ubuntu-mono-nerd", "ttf-fira-code",
			"playerctl", "starship", "upower", "udiskie", "zenity", "gvfs", "qt5ct", "qt6ct",
			"timeshift", "sddm", "qt5-graphicaleffects", "qt5-svg",  "qt5-quickcontrols2", "clipnotify",
			"xdg-desktop-portal-gtk", "gnome-disk-utility", "evince", "tmux", "polkit-gnome",
			"rofimoji", "wmname", "pyenv", "xdg-desktop-portal", "networkmanager", "noto-fonts", 
      "noto-fonts-cjk", "noto-fonts-emoji", "noto-fonts-extra", "flameshot", "rofi-wayland",
			"fcitx5", "fcitx5-configtool", "fcitx5-gtk", "fcitx5-qt", "flatpak"
		],
		bspwm_packages=["xorg", "bspwm", "sxhkd", "xorg-xinit", "xclip", "feh", "lxappearance", "polybar", "xorg-xrandr", "xsettingsd"],
		hyprland_packages=[
			"hyprland", "waybar", "swww", "cliphist", "wl-clipboard", "xdg-desktop-portal-hyprland", "qt5-wayland", "qt6-wayland",
			"xdg-desktop-portal-wlr", "hypridle"]
	),
	aur=DistributionPackages(
		common=[
			"gnu-netcat", "downgrade","gnome-calculator-gtk3", "bibata-cursor-theme-bin", "tela-circle-icon-theme-dracula", "localsend-bin",
			"themix-theme-oomox-git", "themix-plugin-base16-git", "themix-gui-git", "themix-export-spotify-git", "zen-browser-bin",
			"themix-theme-materia-git", "oomox-qt5-styleplugin-git", "oomox-qt6-styleplugin-git", "cava", "ttf-firacode-nerd",
			"youtube-dl", "update-grub", "ttf-meslo-nerd-font-powerlevel10k", "visual-studio-code-bin", "fcitx5-bamboo",
		],
		bspwm_packages=["i3lock-color", "picom-ftlabs-git"],
		hyprland_packages=["hyprpicker", "swaylock-effects-git", "wlr-randr-git", "hyprprop", "grimblast-git"]
	)
)

DRIVERS = {
	"intel": Packages(
		pacman=DistributionPackages(
			common=[
				"lib32-mesa", "vulkan-intel", "lib32-vulkan-intel", 
				"vulkan-icd-loader", "lib32-vulkan-icd-loader", "intel-media-driver",
				"libva-intel-driver", "xf86-video-intel"
			]
		)
	),
	"amd": Packages(
		pacman=DistributionPackages(
			common=[
				"lib32-mesa", "vulkan-radeon", "lib32-vulkan-radeon", 
				"vulkan-icd-loader", "lib32-vulkan-icd-loader"
			]
		)
	),
	"nvidia": Packages(
		pacman=DistributionPackages(
			common=[
				"nvidia-dkms", "nvidia-utils", "lib32-nvidia-utils",
				"nvidia-settings", "vulkan-icd-loader", "lib32-vulkan-icd-loader",
				"lib32-opencl-nvidia", "opencl-nvidia", "libxnvctrl"
			]
		)
	)
}


CUSTOM = {
	"development": {
		"obsidian": PackageInfo("A powerful knowledge base that works on top of a local folder of plain text Markdown files", recommended=True),
		"cursor-bin": PackageInfo("A simple and highly customizable animated cursor", aur=True, recommended=True, selected=False),
	},
	"social_media": {
		"discord": PackageInfo("Popular social platform", recommended=True, selected=True),
		"zalo-macos": PackageInfo("Zalo is an application that allows users to make free calls and send free messages", aur=True, recommended=True, selected=True)
	},
	"tools": {
		"obs-studio": PackageInfo("A cross-platform video recording and live streaming software", recommended=True, selected=True),
		"bleachbit-git": PackageInfo("A tool for cleaning up your system", aur=True, recommended=True, selected=True),
	},
	"games": {
		"steam": PackageInfo("The best launcher for games", recommended=True, selected=False), 
		"gamemode": PackageInfo("Game optimization tool", recommended=True, selected=True), 
		"mangohud": PackageInfo("Displays metrics in running games"),
		"portproton": PackageInfo("Launcher for Windows games with good optimization", recommended=True, aur=True)
	},
	"office": {
		"libreoffice-fresh": PackageInfo("Comprehensive office suite for word processing, spreadsheets, and presentations"),
		"onlyoffice-bin": PackageInfo("Office suite that allows collaborative editing of documents", aur=True, recommended=True, selected=True)
	}
}
