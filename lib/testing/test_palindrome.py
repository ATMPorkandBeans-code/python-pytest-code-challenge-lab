from lib.palindrome import longest_palindromic_substring

def test_longest_palindromic_substring_1():
    input_str= "racecar"
    expected_output = ("racecar")

    actual_output = longest_palindromic_substring(input_str)
    assert actual_output == expected_output

def test_longest_palindromic_substring_2():

    input_str= "cbbd"
    expected_output = ("bb")

    actual_output = longest_palindromic_substring(input_str)
    assert actual_output == expected_output

def test_longest_palindromic_substring_3():

    input_str= "babad"
    expected_output_1 = ("bab")
    expected_output_2 = ("aba")

    actual_output = longest_palindromic_substring(input_str)
    assert actual_output == expected_output_1 or actual_output == expected_output_2

