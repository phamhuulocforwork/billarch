# Billarch Project Overview

## Purpose
Billarch is an Arch Linux automated setup and configuration tool that helps users set up a complete desktop environment with customizable packages, themes, and configurations. It's designed to streamline the process of configuring a fresh Arch Linux installation with popular desktop environments like Hyprland and BSPWM.

## Key Features
- Automated installation of packages from both official repositories and AUR
- Support for multiple window managers (Hyprland, BSPWM)
- Driver installation (Intel, NVIDIA, AMD)
- Comprehensive dotfiles management
- Theme customization (Catppuccin variants)
- Backup functionality for existing configurations
- Interactive questionnaire-based setup process

## Tech Stack
- **Language**: Python 3
- **Dependencies**: inquirer, loguru, psutil, gputil, pyamdgpuinfo, pyyaml, pillow, colorama
- **Package Management**: Pacman, AUR helpers (yay, paru)
- **Target OS**: Arch Linux
- **License**: MIT License

## Project Structure
- `builder/` - Main Python application code
  - `install.py` - Main entry point and orchestration
  - `question.py` - Interactive questionnaire system
  - `packages.py` - Package definitions and configurations
  - `managers/` - Various system management modules
  - `utils/` - Utility functions and data structures
- `home/` - Dotfiles and configuration templates
- `misc/` - Themes and additional assets
- `install.sh` - Initial bootstrap script