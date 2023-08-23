import re
import triangle_checker

def test_triangle_checker_right(capsys, monkeypatch):
    inputs = iter(['3', '4', '5'])
    outputs = ["Valid Triangle", "Right Triangle"]
    missing = ["Not"]
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    triangle_checker.main()
    captured = capsys.readouterr()
    for o in outputs:
        assert re.search(o, captured.out, re.IGNORECASE)
    for m in missing:
        assert not re.search(m, captured.out, re.IGNORECASE)

def test_triangle_checker_equilateral(capsys, monkeypatch):
    inputs = iter(['4', '4', '4'])
    outputs = ["Valid Triangle", "Not a Right Triangle"]
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    triangle_checker.main()
    captured = capsys.readouterr()
    for o in outputs:
        assert re.search(o, captured.out, re.IGNORECASE)

def test_triangle_checker_invalid(capsys, monkeypatch):
    inputs = iter(['1', '2', '8'])
    outputs = ["Not a Triangle"]
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    triangle_checker.main()
    captured = capsys.readouterr()
    for o in outputs:
        assert re.search(o, captured.out, re.IGNORECASE)