# Task Completion Checklist

## When Working on Billarch

### Before Making Changes
1. **Understand the impact**: Changes to package definitions affect user installations
2. **Check dependencies**: Ensure any new packages exist in Arch repos or AUR
3. **Consider window manager compatibility**: Some packages are WM-specific (Hyprland vs BSPWM)

### Code Quality Checks
1. **Syntax Check**: Run `python -m py_compile` on modified Python files
2. **Import Validation**: Ensure all imports are available and correct
3. **Logic Validation**: Test questionnaire flow and package selection logic
4. **Path Validation**: Verify file paths in dotfiles and configurations

### Testing Considerations
- **No automated tests**: This project lacks formal testing infrastructure
- **Manual testing required**: Test on actual Arch Linux system or VM
- **Backup verification**: Ensure backup functionality works before destructive operations
- **Package verification**: Verify package names exist in repos before adding to lists

### Before Committing
1. **Review changed files**: Ensure no temporary or personal files are included
2. **Check .gitignore**: Verify build artifacts and personal configs are excluded
3. **Validate package lists**: Double-check any new packages added to `packages.py`
4. **Update documentation**: If adding new features or changing behavior

### Deployment Notes
- **User impact**: Changes directly affect user system configuration
- **Rollback plan**: Users should always backup before running
- **Distribution method**: Users clone repository and run install script
- **Version management**: No formal versioning system in place

### System Integration
- **Service management**: Verify systemd service configurations
- **Permission requirements**: Most operations require sudo access
- **File system impact**: Operations modify user home directory and system files