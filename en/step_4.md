## Random rhyming words

Print the rhyming words.


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



### Run your code
Run your code a few times. Each time, as well as a random sound, the words that rhyme with it will appear.


