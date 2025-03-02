import pytest

from prompt_tdd.prompt import example_one, example_two


def test_example_one():
    assert example_one("Quick brown fox") == {"message": "Quick brown fox"}


# We can use Parametrization to test multiple inputs
# https://docs.pytest.org/en/7.1.x/example/parametrize.html
@pytest.mark.parametrize(
    "content,expected",
    [
        ("Texas", "Austin"),
        ("California", "Sacramento"),
        ("Japan", "Tokyo"),
    ],
)
def test_example_two(content: str, expected: str):
    assert example_two(content) == expected
