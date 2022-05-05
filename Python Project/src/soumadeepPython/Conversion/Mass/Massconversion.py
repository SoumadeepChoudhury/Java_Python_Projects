KG_TO_TONNE = 0.001
KG_TO_POUND = 2.20462


def kgtotone(kg: float | int) -> float | int:
    """Converts Kilogram to Tonnes"""
    return kg*KG_TO_TONNE


def tonetokg(tonne: float | int) -> float | int:
    """Converts Tonnes to Kilogram"""
    return tonne/KG_TO_TONNE


def kgtopound(kg: float | int) -> float | int:
    """Converts Kilogram to Pound"""
    return kg*KG_TO_POUND


def poundtokg(pound: float | int) -> float | int:
    """Converts Pound to Kilogram"""
    return pound/KG_TO_POUND
