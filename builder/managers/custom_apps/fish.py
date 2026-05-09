import subprocess
import traceback

from loguru import logger

from .base import AppConfigurer


class FishConfigurer(AppConfigurer):
    def setup(self) -> None:
        logger.info("Starting Fish shell configuration...")
        self._install_fisher()
        self._install_nvm_plugin()
        logger.success("Fish shell configuration is complete!")

    def _install_fisher(self) -> None:
        error_msg = "Fisher installation failed: {err}"
        try:
            subprocess.run(
                [
                    "fish",
                    "-c",
                    "curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher",
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            logger.error(error_msg.format(err=e.stderr))
        except Exception:
            logger.error(error_msg.format(err=traceback.format_exc()))

    def _install_nvm_plugin(self) -> None:
        error_msg = "nvm.fish plugin installation failed: {err}"
        try:
            subprocess.run(
                ["fish", "-c", "fisher install jorgebucaran/nvm.fish"],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            logger.error(error_msg.format(err=e.stderr))
        except Exception:
            logger.error(error_msg.format(err=traceback.format_exc()))