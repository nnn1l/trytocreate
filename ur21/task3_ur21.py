import pytest
from task1_ur21 import CustomOpen

@pytest.fixture
def sample_file():
    file_content = "hello\nworld\npytest\n"
    file_name = "test_file.txt"
    with CustomOpen(file_name, "w") as f:
        f.write(file_content)
    with CustomOpen(file_name, "r") as f:
        yield f



def test_process_file_logic(sample_file):
    result = [line.strip().upper() for line in sample_file]

    # Expected result
    expected = ["HELLO", "WORLD", "PYTEST"]

    # Assert the result matches the expectation
    assert result == expected, f"Expected {expected}, but got {result}"