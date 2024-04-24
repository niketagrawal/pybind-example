from __future__ import annotations

from pybind_project_example import _core

__doc__ = _core.__doc__
__version__ = _core.__version__
add = _core.add
subtract = _core.subtract

__all__ = ["__doc__", "__version__", "add", "subtract"]
