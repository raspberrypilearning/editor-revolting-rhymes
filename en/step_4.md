<h2 class="c-project-heading--task">Random rhyme key</h2>

--- task ---

Import the random library at the top of your code.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1
---
import random

# Rhyme groups
rhymes = {

--- /code ---
</div>

--- task ---

Create the variable `rhyme_key` and set it to a random choice.

Then print the random rhyme key.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 22-23
---
# Make a poem
rhyme_keys = list(rhymes.keys())
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
--- /code ---
</div>

--- task ---

Run your code a few times. You will see a random rhyme sound each time.

--- /task ---
