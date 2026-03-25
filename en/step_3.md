## Random rhyme key


Import the random library at the top of your code.



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



Change the variable name `rhyme_keys` to `rhyme_key` and set it to a random choice.

Then print the random rhyme key.



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
rhyme_key = random.choice(list(rhymes.keys()))
print("Your rhyming sound is:", rhyme_key)
--- /code ---
</div>



### Now run your code
Run your code a few times. You will see a random rhyme sound each time.


