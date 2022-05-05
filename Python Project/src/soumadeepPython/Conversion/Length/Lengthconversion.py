MILE_TO_KILOMETER = 1.609344
FEET_TO_INCHES = 12


def miletokm(miles: float | int) -> float | int:
    """Convert Miles to Kilometer"""
    return miles*MILE_TO_KILOMETER


def kmtomile(km: float | int) -> float | int:
    """Converts Kilometer to Miles"""
    return km/MILE_TO_KILOMETER


def feettoinches(feet: float | int) -> float | int:
    """Converts Feet to Inches"""
    return feet*FEET_TO_INCHES


def inchestofeet(inch: float | int) -> float | int:
    """Converts Inches to Feet"""
    return inch/FEET_TO_INCHES
