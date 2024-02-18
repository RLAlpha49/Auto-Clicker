"""
This module defines an enumeration for preset clicks per second (CPS) options. 
The user can choose from these preset options when setting the CPS speed for 
the auto-clicker.
"""

from enum import Enum


# Enum for presets
class Presets(Enum):
    """
    An enumeration for preset clicks per second (CPS) options. The user can
    choose from these preset options when setting the CPS speed for the auto-clicker.
    """

    OPTION_1 = 50
    OPTION_2 = 100
    OPTION_3 = 250
    OPTION_4 = 500
    OPTION_5 = 1000
