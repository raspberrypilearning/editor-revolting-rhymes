<h2 class="c-project-heading--task">Keep it unique</h2>

Your code picks a random word every time, but these words can repeat.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

This spoils the rhyme.

Shuffle each list of words.

Then, so that nothing repeats, `pop` each word off the shuffled lists and use the updated lists each time you print a new line in your `for` loop.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 26-28, 30-31
---
# Make a poem
rhyme_key = random.choice(rhyme_keys)
print(f'Your rhyming sound is: {rhyme_key}')
rhyme_words = rhymes[rhyme_key]
print(f'Your rhyming words are: {rhyme_words}')

random.shuffle(adjectives)
random.shuffle(verbs)
random.shuffle(rhyme_words)

for i in range(2):
    print(f'🤢 The {adjectives.pop()} thing {verbs.pop()} like a {rhyme_words.pop()}')

--- /code ---
</div>

## Now run your code

You will see two random rhyming sentences each time.

Here is an example of what you will see.

<div class="c-project-output">
<pre>
Your rhyming sound is: ug
Your rhyming words are: ['slug', 'bug', 'mug', 'grub']
🤢 The mouldy thing dripped like a mug
🤢 The slimy thing squelched like a grub
</pre>
</div>

### Tip

<div class="c-project-callout c-project-callout--tip">

`pop()` takes the last item from a list and removes it so it cannot be used again.
So, each time the loop runs:
- One adjective is used up
- One verb is used up
- One rhyming word is used up

</div>

### Debugging

<div class="c-project-callout c-project-callout--debug">

If you use a number greater than 4 in your `for` loop, the code will not work, because there are only 4 items in each possible list of `rhyme_words` and you cannot `pop` an item that is not there!

</div>
