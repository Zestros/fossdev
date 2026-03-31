from text_utils.app import reverse_text


def test_reverse():
    assert reverse_text("abc") == "cba"