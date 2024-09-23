class Ability:
	def __init__(self, score: int) -> None:
		self.score = score
	
	@property
	def modifier(self) -> int:
		return (self.score - 10) // 2
	
	def __str__(self) -> str:
		return f"{self.score} ({self.modifier:+})"