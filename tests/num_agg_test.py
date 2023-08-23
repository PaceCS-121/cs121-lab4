import re
import num_agg

def test_num_agg_answers(capsys):
    answers = ['1', '51', '1', '1', '9', '21', '6561', '925', '73', '3', '45903']
    num_agg.main()
    captured = capsys.readouterr()
    for a in answers:
        assert re.search(a, captured.out, re.IGNORECASE)

