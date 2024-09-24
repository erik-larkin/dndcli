import sys
sys.path.append("./")
from dnd.character import *

class AlignmentTest:
	def test_alignment_init() -> None:
		sut = Alignment("lawful", "good")
		assert sut.order == "lawful"
		assert sut.morality == "good"

		sut = Alignment("CHAOTIC", "EVIL")
		assert sut.order == "chaotic"
		assert sut.morality == "evil"

		sut = Alignment("neUTral", "nEutral")
		assert sut.order == "neutral"
		assert sut.morality == "neutral"