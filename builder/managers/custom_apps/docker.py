import subprocess
import traceback

from loguru import logger

from .base import AppConfigurer


class DockerConfigurer(AppConfigurer):
    def setup(self) -> None:
        logger.info("Starting Docker configuration...")
        self._setup_group()
        self._start_and_enable_service()
        logger.success("Docker configuration is complete!")

    def _setup_group(self) -> None:
        error_msg = "Docker group setup failed: {err}"
        try:
            subprocess.run(["sudo", "groupadd", "docker"], check=False, capture_output=True)
            subprocess.run(["sudo", "usermod", "-aG", "docker", subprocess.os.getenv("USER")], check=True)
            subprocess.run(["newgrp", "docker"], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(error_msg.format(err=e.stderr))
        except Exception:
            logger.error(error_msg.format(err=traceback.format_exc()))

    def _start_and_enable_service(self) -> None:
        error_msg = "Docker service setup failed: {err}"
        try:
            subprocess.run(["sudo", "systemctl", "start", "docker.service"], check=True)
            subprocess.run(["sudo", "systemctl", "enable", "docker.service"], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(error_msg.format(err=e.stderr))
        except Exception:
            logger.error(error_msg.format(err=traceback.format_exc()))