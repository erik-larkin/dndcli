from enum import Enum

class Order(Enum):
    NEUTRAL = "neutral"
    LAWFUL = "lawful"
    CHAOTIC = "chaotic"

class Morality(Enum):
    NEUTRAL = "neutral"
    GOOD = "good"
    EVIL = "evil"

class Alignment:
    """Class representing character alignments such as Lawful Good, Chaotic
    Neutral, etc."""

    def __init__(self, order: Order, morality: Morality) -> None:        
        self.morality = morality
        self.order = order
    
    def __str__(self) -> str:
        if self.morality == Morality.NEUTRAL and self.order == Order.NEUTRAL:
            return "Neutral"
        return f"{self.order.title()} {self.morality.title()}"