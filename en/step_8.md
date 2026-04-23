## Challenge: Add some things

Rather than using `thing`, build a list of things.

- Add a word list variable called `things`
- Add some nouns to it
- Shuffle the list
- In your final `print` statement, change `thing` to `things.pop()`

You can comment out, or delete, the first two `print` statements if you like.

You can change the range in the `for` loop to print **up to four** lines of revolting rhymes.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
line_highlights: 18, 27-30, 32-33
---
adjectives = ['slimy', 'stinky', 'mouldy', 'soggy', 'squelchy', 'gooey', 'mucky']
verbs = ['sloshed', 'oozed', 'plopped', 'dripped', 'squelched', 'splats', 'slurps']
things = ['slime', 'muck', 'gunk', 'goo', 'grime', 'filth', 'crud']

# Make a poem
rhyme_keys = list(rhymes.keys())
rhyme_key = random.choice(rhyme_keys)
# print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
# print(f'Your rhyming words are: {rhyme_words}')

random.shuffle(adjectives)
random.shuffle(verbs)
random.shuffle(rhyme_words)
random.shuffle(things)

for i in range(4):
    print(f'🤢 The {adjectives.pop()} {things.pop()} {verbs.pop()} like a {rhyme_words.pop()}')
--- /code ---
</div>

### Run your code
Run this example to see what you could make.

<iframe src="https://editor.raspberrypi.org/en/embed/viewer/editor-revolting-rhymes-complete" width="400" height="710" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
