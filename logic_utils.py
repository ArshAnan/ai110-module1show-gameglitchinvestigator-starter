def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored from app.py into logic_utils.py using Copilot Agent mode.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored from app.py into logic_utils.py using Copilot Agent mode.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome string.

    Returns: "Win", "Too High", or "Too Low"
    """
    # FIX: Bug 1 — hints were backwards in the original code. "Too High" was
    # returning "Go HIGHER!" and "Too Low" was returning "Go LOWER!", pointing
    # the player in the wrong direction. Fixed by correcting the message mapping.
    # Refactored from app.py into logic_utils.py using Copilot Agent mode.
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Bug 2 — on even-numbered attempts, "Too High" was adding 5 points
    # instead of subtracting them, causing the score to jump unexpectedly.
    # Fixed by always subtracting 5 for any wrong guess regardless of attempt number.
    # Refactored from app.py into logic_utils.py using Copilot Agent mode.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
