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
line_highlights: 24-25
---
# Make a poem
rhyme_keys = list(rhymes.keys())
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
print(f'Your rhyming words are: {rhyme_words}')
--- /code ---
</div>

--- task ---

Run your code a few times. The words that rhyme with the random sound will appear each time.

Here is an example of what you will see.

--- /task ---

<div class="c-project-output">
<pre>Your rhyming sound is: unk
Your rhyming words are: ['skunk', 'chunk', 'gunk', 'junk']</pre>
</div>

