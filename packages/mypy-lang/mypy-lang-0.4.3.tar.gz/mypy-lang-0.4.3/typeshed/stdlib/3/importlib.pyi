# Stubs for importlib

# NOTE: These are incomplete!

from typing import Any

# TODO more precise type?
def import_module(name: str, package: str = ...) -> Any: ...
def invalidate_caches() -> None: ...
