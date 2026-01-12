"""
Example API module for Youva.

This module exists purely to test how Sphinx AutoAPI generates
documentation for:

- Module docstrings
- Constants
- Functions
- Classes
- Class inheritance
- Type hints
- Private members
- Exceptions

You SHOULD NOT treat this module as production code.
"""

from __future__ import annotations

from typing import List, Optional, Dict, Any


# ============================================================
# Module-level constants
# ============================================================

DEFAULT_TIMEOUT: int = 30
"""
Default timeout in seconds used by Youva operations.
"""

PI: float = 3.141592653589793
"""
Approximate value of π.
"""


# ============================================================
# Custom exceptions
# ============================================================

class YouvaError(Exception):
    """
    Base exception for all Youva-related errors.
    """


class InvalidInputError(YouvaError):
    """
    Raised when invalid input is passed to a Youva function.
    """


# ============================================================
# Module-level functions
# ============================================================

def add(a: int, b: int) -> int:
    """
    Add two integers.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        Sum of ``a`` and ``b``.

    Raises
    ------
    InvalidInputError
        If either input is negative.
    """
    if a < 0 or b < 0:
        raise InvalidInputError("Negative numbers are not supported.")
    return a + b


def mean(values: List[float]) -> float:
    """
    Compute the arithmetic mean of a list of numbers.

    Parameters
    ----------
    values : list of float
        List of numeric values.

    Returns
    -------
    float
        The average of the values.

    Raises
    ------
    ValueError
        If the list is empty.
    """
    if not values:
        raise ValueError("Cannot compute mean of empty list.")
    return sum(values) / len(values)


# ============================================================
# Base class
# ============================================================

class Processor:
    """
    Base class for all Youva processors.

    This class demonstrates:
    - Instance attributes
    - Public and private methods
    - Type hints
    """

    def __init__(self, name: str):
        """
        Initialize the processor.

        Parameters
        ----------
        name : str
            Name of the processor.
        """
        self.name: str = name
        self.enabled: bool = True

    def process(self, data: Any) -> Any:
        """
        Process input data.

        This method should be overridden by subclasses.

        Parameters
        ----------
        data : Any
            Input data.

        Returns
        -------
        Any
            Processed data.
        """
        raise NotImplementedError("Subclasses must implement process().")

    def disable(self) -> None:
        """
        Disable this processor.
        """
        self.enabled = False

    def _internal_helper(self) -> str:
        """
        Internal helper method.

        This should ideally NOT be exposed to users.
        """
        return "internal"


# ============================================================
# Derived class (inheritance test)
# ============================================================

class NumberProcessor(Processor):
    """
    Processor specialized for numeric data.

    Demonstrates:
    - Inheritance
    - Method overriding
    - Additional attributes
    """

    def __init__(self, name: str, scale: float = 1.0):
        """
        Initialize a NumberProcessor.

        Parameters
        ----------
        name : str
            Processor name.
        scale : float, optional
            Scaling factor, by default 1.0
        """
        super().__init__(name)
        self.scale: float = scale

    def process(self, data: float) -> float:
        """
        Scale numeric input data.

        Parameters
        ----------
        data : float
            Numeric input.

        Returns
        -------
        float
            Scaled value.
        """
        if not self.enabled:
            raise YouvaError("Processor is disabled.")
        return data * self.scale


# ============================================================
# Data container class
# ============================================================

class Config:
    """
    Configuration container for Youva.

    Demonstrates:
    - Default arguments
    - Optional types
    - Dictionary attributes
    """

    def __init__(
        self,
        retries: int = 3,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize configuration.

        Parameters
        ----------
        retries : int, optional
            Number of retry attempts, by default 3.
        metadata : dict, optional
            Arbitrary metadata.
        """
        self.retries = retries
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to dictionary.

        Returns
        -------
        dict
            Configuration values.
        """
        return {
            "retries": self.retries,
            "metadata": self.metadata,
        }


# ============================================================
# Private function (noise test)
# ============================================================

def _debug_only_function() -> None:
    """
    Debug-only function.

    This function exists to test whether AutoAPI
    exposes private helpers.
    """
    pass


# ============================================================
# Public API declaration (IMPORTANT for AutoAPI)
# ============================================================

__all__ = [
    "DEFAULT_TIMEOUT",
    "PI",
    "YouvaError",
    "InvalidInputError",
    "add",
    "mean",
    "Processor",
    "NumberProcessor",
    "Config",
]
