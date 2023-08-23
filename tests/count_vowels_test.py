import re
import count_vowels

def test_count_vowels_city(capsys):
    output = "Philadelphia"
    count_vowels.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)

def test_count_vowels_num(capsys):
    output = "5"
    count_vowels.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)