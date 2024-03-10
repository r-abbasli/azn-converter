import pytest
from project import ask_which_way, convert, ounces_prepend, rates


def test_ask_which_way(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr('builtins.input', lambda _: "to")
    assert ask_which_way() == "to"
    monkeypatch.setattr('builtins.input', lambda _: "from")
    assert ask_which_way() == "from"
    monkeypatch.setattr('builtins.input', lambda _: "fRoM")
    assert ask_which_way() == "from"
    monkeypatch.setattr('builtins.input', lambda _: "exit")
    assert ask_which_way() == "exit"


def test_ounces_prepend():
    assert ounces_prepend("XAU", "to", "100", "100") == "troy ounces of "
    assert ounces_prepend("XAU", "to", "1", "1") == "troy ounce of "
    assert ounces_prepend("XAU", "from", "100", "100") == "troy ounces of "
    assert ounces_prepend("XAU", "from", "1", "1") == "troy ounce of "
    assert ounces_prepend("USD", "from", "1", "1") == ""
    assert ounces_prepend("USD", "to", "100", "100") == ""
    

def test_convert(monkeypatch: pytest.MonkeyPatch):
    inputs = iter(["100", "EUR"])
    monkeypatch.setattr('builtins.input', lambda _:next(inputs))
    test_rate = [{'unit': '1', 'code': 'EUR', 'currency_value': 1.8}]
    monkeypatch.setattr("project.rates", test_rate)
    assert convert("to") == "\n100.00 EUR is 180.00 AZN"

    inputs = iter(["35000", "XAU"])
    monkeypatch.setattr('builtins.input', lambda _:next(inputs))
    test_rate = [{'unit': '1', 'code': 'XAU', 'currency_value': 3500}]
    monkeypatch.setattr("project.rates", test_rate)
    assert convert("from") == "\n35000.00 AZN is 10.00 troy ounces of XAU"
    

    inputs = iter(["1", "EXIT"])
    monkeypatch.setattr('builtins.input', lambda _:next(inputs))
    with pytest.raises(SystemExit):
        convert("to")