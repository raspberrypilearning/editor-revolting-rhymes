<h2 class="c-project-heading--task">Stop words repeating</h2>
--- task ---

Avoid boring repeats.

--- /task ---

At the moment, the computer chooses words randomly, but sometimes that means repeats.

Shuffling puts the words in a random order, without repeating them.

--- task ---

Make copies of the lists and shuffle them.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 22
line_highlights: 27-30, 32-35
---
def make_poem(lines=4, rhyme_key=None, emoji="🤢"):
    
    # Pick a rhyme group at random
    rhyme_key = random.choice(list(rhymes.keys()))
    rhyme_key = random.choice(list(rhymes.keys()))

    # Make COPIES of the lists so we don’t break the originals
    rhyme_words = rhymes[rhyme_key][:]
    adj_list = adjectives[:]
    verb_list = verbs[:]

    # Shuffle everything once
    random.shuffle(rhyme_words)
    random.shuffle(adj_list)
    random.shuffle(verb_list)
--- /code ---
</div>


