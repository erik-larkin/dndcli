class Ability:
    """Class representing ability scores and modifiers, such as Strength,
    Charisma, Dexterity, etc."""

    def __init__(self, score: int) -> None:
        self.score = score
    
    @property
    def modifier(self) -> int:
        return (self.score - 10) // 2
    
    def __str__(self) -> str:
        return f"{self.score} ({self.modifier:+})"

_ORDERS = set(["neutral", "lawful", "chaotic"])
_MORALITIES = set(["neutral", "good", "evil"])

class Alignment:
    """Class representing character alignments such as Lawful Good, Chaotic
    Neutral, etc."""

    def __init__(self, order: str, morality: str) -> None:
        if order.lower() not in _ORDERS:
            raise ValueError(f"order must be one of {_ORDERS}")
        if morality.lower() not in morality:
            raise ValueError(f"morality must be one of {_MORALITIES}")
        
        self.morality = morality.lower()
        self.order = order.lower()
    
    def __str__(self) -> str:
        if self.morality == "neutral" and self.order == "neutral":
            return "Neutral"
        return f"{self.order.title()} {self.morality.title()}"