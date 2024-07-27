import sys  
sys.path.append("./")
from dndcli.character import *

def test_init() -> None:
	sut = Ability(10)
	assert sut.score == 10
	assert sut.modifier == 0

	sut = Ability(15)
	assert sut.score == 15
	assert sut.modifier == 2

	sut = Ability(7)
	assert sut.score == 7
	assert sut.modifier == -2

def test_str() -> None:
	sut = Ability(10)
	assert str(sut) == "10 (+0)"

	sut = Ability(13)
	assert str(sut) == "13 (+1)"

	sut = Ability(5)
	assert str(sut) == "5 (-3)"
