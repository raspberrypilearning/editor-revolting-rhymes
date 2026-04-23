<h2 class="c-project-heading--task">Build your first line</h2>

Choose random words.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Then, build a sentence that uses those words.
<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 26-28, 30
---
# Make a poem
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

## Now run your code

You will see random lines.

Here is an example of what you will see.

<div class="c-project-output">
<pre>The mouldy thing oozed like a poop</pre>
</div>
