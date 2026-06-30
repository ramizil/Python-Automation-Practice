"""Layer 1 — a tiny shared logging helper.

Real frameworks log what they do so failures are diagnosable from CI output
alone. ``get_logger`` returns a process-wide logger configured once; set the
level with the ``LOG_LEVEL`` env var (default INFO).
"""

from __future__ import annotations

import logging
import os

_CONFIGURED = False


def _configure() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)-5s %(name)s | %(message)s")
    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    _configure()
    return logging.getLogger(name)
