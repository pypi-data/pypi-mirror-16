
"""
    This module provides a client library for cloudfoundry_client v2.
"""

__version__ = "0.0.13"

from main import main, build_client_from_configuration
from client import CloudFoundryClient
from entities import InvalidStatusCode
