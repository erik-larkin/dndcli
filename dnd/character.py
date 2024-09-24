from enum import Enum
from bisect import bisect_right

class Order(Enum):
    NEUTRAL = "neutral"
    LAWFUL = "lawful"
    CHAOTIC = "chaotic"

class Morality(Enum):
    NEUTRAL = "neutral"
    GOOD = "good"
    EVIL = "evil"

class Ability(Enum):
    STRENGTH = "str"
    DEXTERITY = "dex"
    CONSTITUTION = "con"
    INTELLIGENCE = "int"
    WISDOM = "wis"
    CHARISMA = "cha"

class Skill(Enum):
    ACROBATICS = "acrobatics"
    ANIMAL_HANDLING = "animal_handling"
    ARCANA = "arcana"
    ATHLETICS = "athletics"
    DECEPTION = "deception"
    HISTORY = "history"
    INSIGHT = "insight"
    INTIMIDATION = "intimidation"
    INVESTIGATION = "investigation"
    MEDICINE = "medicine"
    NATURE = "nature"
    PERCEPTION = "perception"
    PERFORMANCE = "performance"
    PERSUASION = "persuasion"
    RELIGION = "religion"
    SLEIGHT_OF_HAND = "sleight of hand"
    STEALTH = "stealth"
    SURVIVAL = "survival"

SKILL_ABILITIES = {
    Skill.ACROBATICS: Ability.DEXTERITY,
    Skill.ANIMAL_HANDLING: Ability.WISDOM,
    Skill.ARCANA: Ability.INTELLIGENCE,
    Skill.ATHLETICS: Ability.STRENGTH,
    Skill.DECEPTION: Ability.CHARISMA,
    Skill.HISTORY: Ability.INTELLIGENCE,
    Skill.INSIGHT: Ability.WISDOM,
    Skill.INTIMIDATION: Ability.CHARISMA,
    Skill.INVESTIGATION: Ability.INTELLIGENCE,
    Skill.MEDICINE: Ability.WISDOM,
    Skill.NATURE: Ability.INTELLIGENCE,
    Skill.PERCEPTION: Ability.WISDOM,
    Skill.PERFORMANCE: Ability.CHARISMA,
    Skill.PERSUASION: Ability.CHARISMA,
    Skill.RELIGION: Ability.INTELLIGENCE,
    Skill.SLEIGHT_OF_HAND: Ability.DEXTERITY,
    Skill.STEALTH: Ability.DEXTERITY,
    Skill.SURVIVAL: Ability.WISDOM
}

LEVEL_EXP_THRESHOLDS = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 
                        48000, 64000, 85000, 100000, 120000, 140000,
                        165000, 195000, 225000, 265000, 305000, 355000]

class Alignment:
    """Class representing character alignments such as Lawful Good, Chaotic
    Neutral, etc."""

    def __init__(self, order: Order, morality: Morality) -> None:        
        self.morality = morality
        self.order = order
    
    def __str__(self) -> str:
        if self.morality == "neutral" and self.order == "neutral":
            return "Neutral"
        return f"{self.order.title()} {self.morality.title()}"

class Character:
    def __init__(self) -> None:
        self.name = None
        self.character_class = None
        self.background = None
        self.race = None
        self.alignment = None
        self.exp = None

        self.abilities = {
            Ability.STRENGTH: 0,
            Ability.DEXTERITY: 0,
            Ability.CONSTITUTION: 0,
            Ability.INTELLIGENCE: 0,
            Ability.WISDOM: 0,
            Ability.CHARISMA: 0
        }

        self.inspiration = 0
        self.skills = set()
        self.saving_throws = set()
        self.armor_class = 0
        self.speed = 0
        
        self.max_max = 0
        self.current_hp = 0
        self.temp_hp = 0
    
    @property
    def level(self) -> int:
        return bisect_right(LEVEL_EXP_THRESHOLDS, self.exp)

    @property
    def proficiency_bonus(self) -> int:
        return 2 + ((self.level - 1) // 4)

    @property
    def passive_perception(self) -> int:
        return 10 + self.skill_modifier(Skill.PERCEPTION)

    @property
    def initiative(self) -> int:
        return self.ability_modifier(Ability.DEXTERITY)

    def ability_modifier(self, ability: Ability) -> int:
        return (self.abilities[ability] - 10) // 2

    def skill_modifier(self, skill: Skill) -> int:
        result = self.ability_modifier(SKILL_ABILITIES[skill])
        if skill in self.skills:
            result += self.proficiency_bonus
        return result
