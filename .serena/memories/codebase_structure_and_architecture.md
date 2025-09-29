# Codebase Structure and Architecture

## Directory Structure
```
billarch/
├── builder/                 # Main Python application
│   ├── __init__.py
│   ├── install.py          # Main entry point and orchestration
│   ├── question.py         # Interactive questionnaire system
│   ├── packages.py         # Package definitions and configurations
│   ├── managers/           # System management modules
│   │   ├── apps_manager.py
│   │   ├── drivers_manager.py
│   │   ├── filesystem_manager.py
│   │   ├── package_manager.py
│   │   └── post_install_manager.py
│   └── utils/              # Utilities and data structures
│       ├── banner.py
│       └── schemes.py
├── home/                   # User configuration templates
│   ├── .bashrc, .profile, .env, .xinitrc, .Xresources, .gitconfig
│   ├── bin/                # User scripts
│   ├── .config/            # Application configurations
│   │   ├── hypr/          # Hyprland configs
│   │   ├── bspwm/         # BSPWM configs
│   │   ├── kitty/         # Terminal configs
│   │   ├── waybar/        # Status bar configs
│   │   ├── tmux/          # Terminal multiplexer
│   │   └── billarch/      # Custom themes and configs
│   └── .local/            # Local user data
├── misc/                   # Themes and additional assets
│   ├── grub_theme/        # GRUB bootloader theme
│   └── sddm_theme/        # Display manager theme
├── install.sh             # Bootstrap installation script
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── .gitignore            # Git ignore rules
```

## Architecture Components

### 1. Builder System (`builder/`)
- **install.py**: Main orchestrator that coordinates the entire installation process
- **question.py**: Interactive questionnaire using `inquirer` library
- **packages.py**: Centralized package definitions with categorization

### 2. Manager Pattern (`builder/managers/`)
- **PackageManager**: Handles pacman and AUR package installation
- **DriversManager**: Manages graphics driver installation and detection
- **FileSystemManager**: Handles dotfile copying and backup creation
- **AppsManager**: Configures specific applications (GRUB, SDDM, etc.)
- **PostInstallation**: Final system setup and service configuration

### 3. Configuration System
- **Dataclass-based**: Uses Python dataclasses for type-safe configuration
- **Enum-driven**: Choices like AUR helpers use enums for validation
- **Modular packages**: Packages organized by category and window manager

### 4. User Configuration (`home/`)
- **Dotfiles**: Shell configurations, environment variables
- **Application configs**: Window manager, terminal, status bar configurations
- **Theme system**: Multiple theme variants (Catppuccin Latte/Mocha)

### 5. Flow Architecture
1. **Bootstrap** (`install.sh`) → Install Python dependencies
2. **Questionnaire** (`question.py`) → Gather user preferences
3. **Backup** (`filesystem_manager`) → Backup existing configurations
4. **Package Installation** (`package_manager`) → Install system packages
5. **Driver Installation** (`drivers_manager`) → Install graphics drivers
6. **Configuration** (`filesystem_manager`) → Copy dotfiles and themes
7. **Service Setup** (`apps_manager`) → Configure system services
8. **Post-Installation** (`post_install_manager`) → Final system tweaks