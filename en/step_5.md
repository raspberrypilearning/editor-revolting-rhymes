## Build your first line
Choose random words.

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
rhyme_key = random.choice(list(rhymes.keys()))
print("Your rhyming sound is:", rhyme_key)
rhyme_words = rhymes[rhyme_key]
print("Your rhyming words are:", rhyme_words)

adjective = random.choice(adjectives)
verb = random.choice(verbs)
end_word = random.choice(rhyme_words)

print("🤢 The", adjective, "thing", verb, "like a", end_word)


--- /code ---
</div>



### Run your code
Run your code a few times to see random sentences.

Here is an example of what you will see.


<div class="c-project-output">
<pre>The mouldy thing oozed like a poop</pre>
</div>
