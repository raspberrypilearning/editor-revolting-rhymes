<h2 class="c-project-heading--task">Pick random words</h2>
--- task ---
Create lists of words and use `random.choice()` to pick a different poem each time.
--- /task ---

<h2 class="c-project-heading--explainer">Let Python surprise you</h2>

Let’s make the poem change every time you run it!

1. Import the `random` module.
2. Make lists of options (creatures, places, smells, slimes).
3. Use `random.choice()` to pick one item from each list.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights:
---
import random

creatures = ['SNAIL', 'WORM', 'SLUG']
places = ['DRAIN', 'SINK', 'BIN']
smells = ['CHEESE', 'MOLD', 'ONION']
slimes = ['GLOOP', 'OOZE', 'SLIME']

creature = random.choice(creatures)
place = random.choice(places)
smell = random.choice(smells)
slime = random.choice(slimes)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Run the program a few times to see different combinations!

</div>
