# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

Bugs found and fixed:

1. **Hints were backwards**
   - **Expected:** When my guess was too high, the hint should say "Go LOWER!" to guide me down toward the secret number.
   - **Actual:** The hint said "Go HIGHER!", pointing me in the wrong direction. The messages for "Too High" and "Too Low" were swapped inside `check_guess`, so every hint was the opposite of what it should have been.

2. **Score was miscalculated on even attempts**
   - **Expected:** Every wrong guess (whether too high or too low) should subtract 5 points from my score consistently.
   - **Actual:** On even-numbered attempts where the guess was "Too High", the `update_score` function added 5 points instead of subtracting them. This caused the score to jump up unexpectedly and made the final score inconsistent with what I had earned.

3. **Attempts counter started at 1 instead of 0**
   - **Expected:** Before making any guess, the "Attempts left" display should show the full number of allowed attempts (e.g., 8 for Normal difficulty).
   - **Actual:** `st.session_state.attempts` was initialized to `1` instead of `0`, so the counter was already off by one before the first guess. The display showed one fewer attempt remaining than was actually the case from the very start.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude (via Claude Code) as my primary AI tool for this project. When I noticed strange behavior while playing, I shared `app.py` with Claude and asked it to explain specific functions step-by-step to understand whether they were working as intended.

**Correct AI suggestion:** When I described that the hints felt backwards, I asked Claude to explain the `check_guess` function line by line. It correctly identified that the emoji-message pairs for "Too High" and "Too Low" were swapped — "📉 Go LOWER!" was being returned for a "Too High" outcome and vice versa. I verified this by manually tracing through the function with a guess of 90 against a secret of 50: `90 > 50` is true, so it should return "Too High" with "Go LOWER!", but the code returned "Go HIGHER!" instead. That confirmed the AI's explanation was right.

**Misleading AI suggestion:** I highlighted the `TypeError` exception block inside `check_guess` (lines 41–47 in `app.py`) and asked Claude what it was for. Claude explained it as a useful defensive safety guard — "in case a non-integer value slips through, this block handles string comparisons as a fallback." That sounded reasonable, but it was misleading. I checked `parse_guess`, which already ensures only valid integers ever reach `check_guess` — so that block is dead code that can never actually run. The AI framed it as intentional defensive programming when it was really just confusing noise. I verified this by tracing the full call path: `parse_guess` returns `(False, None, error)` for any non-integer input, and the submit handler only calls `check_guess` when `ok` is `True`, meaning a valid integer is always guaranteed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I used two layers of verification for each fix: automated pytest tests and manual play in the live Streamlit app. A bug wasn't considered fixed until both layers agreed — a passing test confirmed the logic was correct, and a manual play-through confirmed the UI reflected that logic correctly.

For the hints bug, I wrote `test_too_high_not_too_low` and `test_too_low_not_too_high` in `tests/test_game_logic.py`. These tests call `check_guess` directly with extreme values (e.g., guess of 90 against a secret of 10) and assert that the outcome is never swapped. When I ran `pytest` after moving `check_guess` into `logic_utils.py`, all 11 tests passed, which confirmed that the fix was correct and that the refactor didn't break anything. For the score bug, I wrote `test_score_decreases_on_even_attempt`, which calls `update_score(100, "Too High", 4)` — an even-numbered attempt — and asserts the result is 95, not 105. This directly targeted the original misbehavior.

Claude helped design the test structure by suggesting that the best way to catch the hints bug was to assert the *negation* (e.g., "Too High must never return Too Low") rather than just checking the happy path. That made the tests more robust because they would catch the bug even if the exact message text changed in the future.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
