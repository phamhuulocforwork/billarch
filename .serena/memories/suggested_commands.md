# Essential Commands for Billarch Development

## Project Setup and Installation
```bash
# Make install script executable and run
chmod +x install.sh
./install.sh

# Or run directly with Python after dependencies are installed
python builder/install.py
```

## Development Commands
```bash
# Navigate to project directory
cd /home/huuloc/Github/billarch

# Run the main installer
python builder/install.py

# Check Python syntax
python -m py_compile builder/install.py

# Install Python dependencies manually
pip install inquirer loguru psutil gputil pyamdgpuinfo pyyaml pillow colorama --break-system-packages
```

## System Commands (Linux/Arch)
```bash
# Package management
sudo pacman -S <package>        # Install from official repos
yay -S <package>               # Install from AUR (if yay is installed)
paru -S <package>              # Install from AUR (if paru is installed)

# File operations
ls -la                         # List files with details
find . -name "*.py"           # Find Python files
grep -r "pattern" .           # Search for patterns
tree                          # Show directory structure

# Git operations
git status                    # Check repository status
git add .                     # Stage all changes
git commit -m "message"       # Commit changes
git push                      # Push to remote

# System info
uname -a                      # System information
lscpu                         # CPU information
lspci                         # PCI devices (for graphics detection)
```

## Configuration Management
```bash
# Backup existing configs (done automatically by the tool)
# Located in ./backup/ after running

# Copy dotfiles
cp -r home/.* ~/              # Copy dotfiles to home directory

# Manage systemd services
sudo systemctl enable <service>
sudo systemctl start <service>
sudo systemctl status <service>
```