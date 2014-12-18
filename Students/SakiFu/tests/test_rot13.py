
from rot13 import rot13


def test_basic():
    assert rot13("ABCDE") == "NOPQR"
    assert rot13("vwxyz") == "ijklm"
    assert rot13("AEKjSCpw") == "NRXwFPcj"


def test_whitespace_period():
    assert rot13("Good morning.") == "Tbbq zbeavat."
    assert rot13("I like chocolate.") == "V yvxr pubpbyngr."
    assert rot13("I need tea.") == "V arrq grn."
    assert rot13("She lives in SLU.") == "Fur yvirf va FYH."
    assert rot13("He bought a beer.") == "Ur obhtug n orre."
    assert rot13("This is interesting.") == "Guvf vf vagrerfgvat."
    assert rot13("It will rain tomorrow.") == "Vg jvyy enva gbzbeebj."
    assert rot13("I wish I knew it.") == "V jvfu V xarj vg."
    assert rot13("My cat is hairless.") == "Zl png vf unveyrff."
    assert rot13("I should go to bed.") == "V fubhyq tb gb orq."
    assert rot13("But you said so.") == "Ohg lbh fnvq fb."
    assert rot13("How wrinkly it is.") == "Ubj jevaxyl vg vf."
    assert rot13("Look at that dog.") == "Ybbx ng gung qbt."

