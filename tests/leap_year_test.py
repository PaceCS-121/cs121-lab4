import re
import leap_year

def test_leap_year_1996(capsys, monkeypatch):
    inputs, output = ("1996", "leap year")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    assert output in captured.out.lower()

def test_leap_year_2000(capsys, monkeypatch):
    inputs, output = ("2000", "leap year")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    assert output in captured.out.lower()

def test_leap_year_1800(capsys, monkeypatch):
    inputs, outputs = ("1800", ["not", "a leap year"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert output in captured.out.lower()

def test_leap_year_1999(capsys, monkeypatch):
    inputs, outputs = ("1999", ["not", "a leap year"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert output in captured.out.lower()

def test_leap_year_str(monkeypatch):
    # test that program works with a non valid input
    inputs = "hello"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    assert True