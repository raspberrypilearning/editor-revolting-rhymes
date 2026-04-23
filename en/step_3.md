<h2 class="c-project-heading--task">Random rhyme key</h2>

Import the `random` library and choose a rhyme key.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

## Step 1

At the top of your code, import the `random` library.

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

## Step 2

Create the variable `rhyme_key` and set it to a random choice from `rhyme_keys`.

## Step 3

Then, print the random rhyme key.
<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 21-22
---
# Make a poem
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
--- /code ---
</div>

## Now run your code

You will see a random rhyming sound each time.
