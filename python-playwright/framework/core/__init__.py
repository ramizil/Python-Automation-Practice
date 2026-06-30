"""Layer 1 — infrastructure: product-agnostic building blocks reused by every
product (logging, base API client with auth + logging interceptor)."""

from .base_api_client import BaseApiClient
from .logger import get_logger

__all__ = ["BaseApiClient", "get_logger"]
