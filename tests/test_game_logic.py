from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# --- Bug 1 fix: hints direction ---
# The original bug had "Too High" and "Too Low" swapped. These tests confirm
# the correct direction is returned for guesses on either side of the secret.

def test_too_high_not_too_low():
    # A guess above the secret must never return "Too Low"
    result = check_guess(90, 10)
    assert result != "Too Low"

def test_too_low_not_too_high():
    # A guess below the secret must never return "Too High"
    result = check_guess(10, 90)
    assert result != "Too High"

# --- Bug 2 fix: score deduction ---
# The original bug added 5 points on even-numbered "Too High" attempts instead
# of subtracting. These tests confirm the score always goes down on wrong guesses.

def test_score_decreases_on_too_high():
    # Wrong guess (Too High) should always subtract 5 points
    result = update_score(100, "Too High", 2)
    assert result == 95

def test_score_decreases_on_too_low():
    # Wrong guess (Too Low) should always subtract 5 points
    result = update_score(100, "Too Low", 3)
    assert result == 95

def test_score_decreases_on_even_attempt():
    # Even-numbered attempt should still subtract, not add
    result = update_score(100, "Too High", 4)
    assert result == 95

# --- parse_guess ---

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_guess_non_number():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
