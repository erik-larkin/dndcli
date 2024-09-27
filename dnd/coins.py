from __future__ import annotations

class Coins:
    def __init__(self) -> None:
        self.copper = 0
        self.silver = 0
        self.electrum = 0
        self.gold = 0
        self.platinum = 0
    
    @property
    def gold_value(self) -> float:
        return ((self.platinum * 10) + self.gold + (self.electrum / 2) +
                (self.silver / 10) + (self.copper / 100))

    def add(self, money: Coins) -> None:
        self.copper += money.copper
        self.silver += money.silver
        self.electrum += money.electrum
        self.gold += money.gold
        self.platinum += money.platinum

    def remove(self, money: Coins) -> None:
        pass

    def __str__(self) -> str:
        return (
            f"Total GP value: {self.gold_value}\n"
            f"PP: {self.platinum}; GP: {self.gold}; EP: {self.electrum}; "
            f"SP: {self.silver}; CP: {self.copper}"
        )