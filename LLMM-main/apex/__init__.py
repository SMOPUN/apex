"""Webscout.

Search for words, documents, images, videos, news, maps and text translation 
using the DuckDuckGo.com search engine.
"""

import logging

# ruff: noqa: F401
# from .webscout_search import WEBS

from apex.version import __version__

__all__ = [ "__version__", "cli"]

# A do-nothing logging handler
# https://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger("apex").addHandler(logging.NullHandler())
