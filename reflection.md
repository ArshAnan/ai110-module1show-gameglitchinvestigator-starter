# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

Bugs found and fixed:

1. **Hints were backwards** — the `check_guess` function returned "Go HIGHER!" when the guess was too high and "Go LOWER!" when it was too low. The messages for "Too High" and "Too Low" were swapped, so every hint pointed the player in the wrong direction.

2. **Score was miscalculated on even attempts** — the `update_score` function secretly added 5 points when the outcome was "Too High" on even-numbered attempts, instead of subtracting 5 like every other wrong guess. This caused the score to jump unexpectedly and made the final score inconsistent with what the player expected.

3. **Attempts counter started at 1 instead of 0** — `st.session_state.attempts` was initialized to `1`, so the very first guess incremented it to `2`, and the "Attempts left" display was always off by one before any guess was even made.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude as my preferred AI tool for this. I think when I was playing the game, I realized there were a few problems in the functioning of the application. I referred those parts to Claude and asked it to explain where the function was and what that function was doing to understand if it was serving its intended purpose.

All the "solutions/guidance" that the AI gave me in this case was correct, and it was to the point and did not hallucinate on this codebase. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
