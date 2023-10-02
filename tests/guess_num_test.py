import random
import re
import guess_the_number

inputs = iter(random.sample(range(1, 101), 15))

def test_check_guess(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    guess_the_number.main()
    captured = capsys.readouterr()
    assert re.search(r"high|low", captured.out, re.IGNORECASE)

def test_play(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    guess_the_number.main()
    captured = capsys.readouterr()
    assert re.search(r"congrat|win|sorry|lose", captured.out, re.IGNORECASE)