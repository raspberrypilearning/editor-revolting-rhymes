<h2 class="c-project-heading--task">Random rhyme words</h2>

--- task ---

Print the rhyming words

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 23-24
---
# Make a poem
rhyme_key = random.choice(list(rhymes.keys()))
print("Your rhyming sound is:", rhyme_key)
rhyme_words = rhymes[rhyme_key]
print("Your rhyming words are:", rhyme_words)
--- /code ---
</div>

--- task ---

Run your code a few times. The words that rhyme with the random sound will appear each time.

--- /task ---
