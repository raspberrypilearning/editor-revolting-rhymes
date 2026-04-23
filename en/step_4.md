<h2 class="c-project-heading--task">Random rhyming words</h2>

Print the rhyming words.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Add the code below to print the words that match the random rhyme key.
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
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
print(f'Your rhyming words are: {rhyme_words}')
--- /code ---
</div>

## Now run your code

You will see a random sound and the words that rhyme with it.
