import pytest
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

def test_one():
    assert isPalindrome(121) == True

@pytest.mark.parametrize("num",["121","232","343","454"])
def test_two(num):
    assert isPalindrome(num) == True