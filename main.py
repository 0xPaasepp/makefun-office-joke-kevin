# One office joke, one line: the boss calls the team a family, the
# employee asks when family starts paying overtime, and ends up the
# black sheep of the quarterly review. Setup first, turn in the
# middle, punchline at the end.
import os

LINE = "My boss said 'we're a family here,' so I asked when family starts paying overtime — now I'm the black sheep of the quarterly review."

OUT = "/output/entry.txt"

# The gate wants plain UTF-8 text, 1 to 200 characters, not blank.
assert 1 <= len(LINE) <= 200, "joke must fit the 1-200 character gate"
assert LINE.strip(), "joke must not be blank"
assert LINE == LINE.encode("utf-8").decode("utf-8"), "joke must survive a UTF-8 round trip"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
# The file is the joke and nothing else: no newline at the end.
with open(OUT, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Check what actually landed on disk instead of trusting the write.
with open(OUT, "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "entry.txt on disk is not the joke"
