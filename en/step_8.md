<h2 class="c-project-heading--task">Keep it unique</h2>

You code picks a random word every time, but these words can repeat.

This spoils the rhyme.

--- task ---

Shuffle each list of words.

So nothing repeats: 'pop' each word off the shuffled lists and use them each time you print a new line in your for loop.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 20
line_highlights: 25-27, 29-30
---
# Make a poem
rhyme_key = random.choice(list(rhymes.keys()))
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

--- task ---

Run your code a few times to see random lines.

Here is an example of what you will see.

--- /task ---

<div class="c-project-output">
<pre>
Your rhyming sound is: ug
Your rhyming words are: ['slug', 'bug', 'mug', 'grub']
🤢 The mouldy thing dripped like a mug
🤢 The slimy thing squelched like a grub
</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

`pop()` takes the last item from a list and removes it so it can’t be used again.
So, each time the loop runs:
- One adjective is used up
- One verb is used up
- One rhyme word is used up

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If you use a number greater than 4 in your for loop, the code will break because there are only four items in the list of rhyme_words, and you can't 'pop' an item that isn't there!

</div>
