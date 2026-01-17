import subprocess
import traceback

from loguru import logger

from .base import AppConfigurer
from ..package_manager import PackageManager


class BillpanelConfigurer(AppConfigurer):
    def setup(self) -> None:
        if PackageManager.check_package_installed("billpanel"):
            try:
                self._create_hotkeys()
            except Exception:
                logger.error(f"Billpanel main setup error: {traceback.format_exc()}")

    def _create_hotkeys(self) -> None:
        """Логика создания горячих клавиш для billpanel"""
        logger.info("Configuring billpanel keybindings...")
        subprocess.run(
            ["billpanel", "--create-keybindings"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        logger.success("Billpanel keybindings configured successfully!")