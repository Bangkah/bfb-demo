from bfbutils import (
    RunningAverage,
    binary_search,
    clamp,
    flatten,
    format_money,
    parse_duration,
    slugify,
)


def test_slugify_joint_words():
    assert slugify("hello_world") == "hello-world"


def test_clamp_inside():
    assert clamp(5, 0, 10) == 5


def test_format_money_whole():
    assert format_money(2000) == "$2000"


def test_parse_duration_minutes_and_hours():
    assert parse_duration("90s") == 90
    assert parse_duration("3h") == 10800


def test_running_average_multi():
    ra = RunningAverage()
    ra.add(10)
    ra.add(30)
    assert ra.avg() == 20


def test_binary_search_middle():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_flatten_flat_input():
    assert flatten({"a": 1, "b": 2}) == {"a": 1, "b": 2}


def test_is_palindrome_symmetric_ascii():
    assert is_palindrome("abba") is True
    assert is_palindrome("abcd") is False
