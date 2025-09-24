# Code Style and Conventions

## Python Code Style
- **Language**: Python 3.x
- **Import Style**: Absolute imports, grouped by standard library, third-party, and local modules
- **Class Names**: PascalCase (e.g., `PackageManager`, `DriversManager`)
- **Function Names**: snake_case (e.g., `install_packages`, `update_database`)
- **Variable Names**: snake_case (e.g., `build_options`, `not_installed_packages`)
- **Constants**: UPPER_CASE (e.g., `BASE`, `CUSTOM`, `DRIVERS`)

## Code Organization
- **Dataclasses**: Used extensively for configuration objects (e.g., `BuildOptions`, `PackageInfo`)
- **Type Hints**: Present in function signatures and dataclass fields
- **Enum Usage**: For configuration options (e.g., `AurHelper.YAY`, `AurHelper.PARU`)
- **Logging**: Uses `loguru` library with structured logging
- **Error Handling**: Try-catch blocks with proper error logging

## File Structure Conventions
- **Managers**: Separate modules for different system aspects (apps, drivers, filesystem, packages, post-install)
- **Utils**: Shared utilities and data structures in `utils/` directory
- **Configurations**: Centralized package definitions in `packages.py`
- **Entry Point**: Clear main entry point in `install.py`

## Documentation
- **Docstrings**: Not heavily used, focus on clear function/class names
- **Comments**: Minimal inline comments, code is largely self-documenting
- **Configuration**: Extensive use of dataclasses for self-documenting configuration structures

## Dependencies Management
- **No requirements.txt**: Dependencies are installed via the bootstrap script
- **System Dependencies**: Managed through pacman package definitions
- **Python Dependencies**: Installed with `pip install --break-system-packages`