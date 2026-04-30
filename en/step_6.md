<h2 class="c-project-heading--task">Two lines that rhyme</h2>

Repeat the process to print two rhyming lines.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Use a `for` loop to repeat your random sentence code a set number of times.
<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 26-29, 31
---
# Make a poem
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
print(f'Your rhyming words are: {rhyme_words}')

for i in range(2):
    adjective = random.choice(adjectives)
    verb = random.choice(verbs)
    end_word = random.choice(rhyme_words)

    print(f'🤢 The {adjective} thing {verb} like a {end_word}')

--- /code ---
</div>

## Now run your code

You will see two random rhyming sentences each time.

Sometimes, you might see some words repeat, like `slink` here:

<div class="c-project-output">
<pre>
Your rhyming sound is: ink
Your rhyming words are: ['mink', 'skink', 'slink', 'clink']
🤢 The stinky thing squelched like a slink
🤢 The gooey thing dripped like a slink
</pre>
</div>
