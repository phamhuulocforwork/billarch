from pathlib import Path
from typing import Optional
from os.path import expandvars

HOME = Path.home()
BILLARCH_DIR = Path(__file__).resolve().parent
BILLARCH_THEMES: Path = BILLARCH_DIR / "themes"
OOMOX_TEMPLATES = BILLARCH_DIR / "oomox_templates"
BASE_CONFIGS: Path = BILLARCH_DIR / "base_configs" 
BILLARCH_ASSETS: Path = BILLARCH_DIR / "utils" / "assets"

BILLARCH_CONFIG: Path = BILLARCH_DIR / "config.yaml"
WALLPAPER_SYMLINC: Path = BILLARCH_DIR / "current_wallpaper"

ROFI_SELECTING_THEME: Path = Path.home() / ".config" / "rofi" / "selecting.rasi"

WALLPAPERS_CACHE_DIR: Path = HOME / ".cache" / "billarch" / "wallpaper_thumbnails"
THEMES_CACHE_DIR: Path = HOME / ".cache" / "billarch" / "themes_thumbnails"

OOMOX_COLORS: Path = lambda theme_name: BILLARCH_THEMES / theme_name / "oomox-colors"  # noqa: E731

THEME_GEN_SCRIPT: Path = Path("/opt/oomox/plugins/base16/cli.py")

SESSION_TYPE: Optional[str] = (lambda s: s if s != "$XDG_SESSION_TYPE" else None)(expandvars("$XDG_SESSION_TYPE"))

GTK2_CFG: Path = HOME / ".config" / "gtk-2.0" / "gtkrc"
GTK3_CFG: Path = HOME / ".config" / "gtk-3.0" / "settings.ini"
GTK4_CFG: Path = HOME / ".config" / "gtk-4.0" / "settings.ini"