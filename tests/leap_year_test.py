import re
import leap_year

def test_leap_year_1996(capsys, monkeypatch):
    inputs, outputs = ("1996", [r"^((?!not).)*$", r"^((?!n't).)*$"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out.lower(), re.IGNORECASE)

def test_leap_year_2000(capsys, monkeypatch):
    # reverse negative look up for word not
    inputs, outputs = ("2000", [r"^((?!not).)*$", r"^((?!n't).)*$"])
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out.lower(), re.IGNORECASE)

def test_leap_year_1800(capsys, monkeypatch):
    inputs, output = ("1800", r"[not|n't]")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out.lower(), re.IGNORECASE)

def test_leap_year_1999(capsys, monkeypatch):
    inputs, output = ("1999", r"[not|n't]")
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out.lower(), re.IGNORECASE)

def test_leap_year_str(monkeypatch):
    # test that program works with a non valid input
    inputs = "hello"
    monkeypatch.setattr('builtins.input', lambda _: inputs)
    leap_year.main()
    assert True