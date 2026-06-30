"""Central test configuration: base URLs and demo credentials.

Values can be overridden with environment variables (or a local .env file),
which is how real frameworks switch between dev/staging/prod.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


def _flag(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in ("1", "true", "yes", "on")


# Demo sites are accessed over networks that may run a TLS-inspection proxy
# (corporate "self-signed certificate in chain"). Default ON so the suite runs
# everywhere; set IGNORE_HTTPS_ERRORS=false to enforce real certificate checks.
IGNORE_HTTPS_ERRORS = _flag("IGNORE_HTTPS_ERRORS", True)


# ---- Target applications -------------------------------------------------- #
SAUCEDEMO_URL = os.getenv("SAUCEDEMO_URL", "https://www.saucedemo.com")
BOOKER_API_URL = os.getenv("BOOKER_API_URL", "https://restful-booker.herokuapp.com")
DUMMYJSON_URL = os.getenv("DUMMYJSON_URL", "https://dummyjson.com")
PARABANK_URL = os.getenv("PARABANK_URL", "https://parabank.parasoft.com/parabank")


# ---- SauceDemo demo users (all use the same password) --------------------- #
SAUCE_PASSWORD = "secret_sauce"
SAUCE_USERS = {
    "standard": "standard_user",
    "locked_out": "locked_out_user",
    "problem": "problem_user",
    "performance_glitch": "performance_glitch_user",
}


# ---- restful-booker admin credentials (public demo) ----------------------- #
BOOKER_ADMIN = {"username": "admin", "password": "password123"}
