import random

# Rhyme groups (lists of words)
rhymes = {
    "oop": ["poop", "scoop", "droop", "goop"],
    "ug": ["slug", "bug", "mug", "grub"],
    "ash": ["trash", "mash", "splash", "bash"],
    "ice": ["lice", "mice", "dice", "rice"],
    "op": ["slop", "mop", "flop", "plop"],
    "unk": ["skunk", "chunk", "gunk", "junk"],
    "ink": ["ink", "skink", "slink", "clink"],
    "at": ["rat", "gnat", "bat", "cat"],
}

# Word lists
adjectives = ["slimy", "stinky", "gooey", "soggy"]
verbs = ["plops", "squelches", "oozes", "drips"]


# Make a poem
def make_poem():
    emoji = "🤢"
    lines = 4

    # Pick a rhyme group at random
    rhyme_key = random.choice(list(rhymes.keys()))
    rhyme_words = rhymes[rhyme_key]

    print("Your rhyme group is:", rhyme_key)
    print()

    # Print the poem
    for i in range(lines):
        adjective = random.choice(adjectives)
        verb = random.choice(verbs)
        end_word = random.choice(rhyme_words)

        print(emoji, "The", adjective, "thing", verb, "like a", end_word)


make_poem()
