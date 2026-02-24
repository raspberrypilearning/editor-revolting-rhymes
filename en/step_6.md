<h2 class="c-project-heading--task">Build your first line</h2>

--- task ---

Choose random words.

Then build a sentence that uses the words.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 27-29, 31
---
# Make a poem
rhyme_keys = list(rhymes.keys())
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
print(f'Your rhyming words are: {rhyme_words}')

adjective = random.choice(adjectives)
verb = random.choice(verbs)
end_word = random.choice(rhyme_words)

print(f'🤢 The {adjective} thing {verb} like a {end_word}')


--- /code ---
</div>

--- task ---

Run your code a few times to see random lines.

Here is an example of what you will see.

--- /task ---

<div class="c-project-output">
<pre>The mouldy thing oozes like a poop</pre>
</div>
