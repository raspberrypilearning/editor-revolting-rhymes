import random

# Rhyme groups
rhymes = {
    "oop": ["poop", "coop", "droop", "goop"],
    "ug": ["slug", "bug", "mug", "grub"],
    "ash": ["rash", "mash", "splash", "bash"],
    "ouse": ["louse", "mouse", "grouse", "workhouse"],
    "op": ["slop", "mop", "flop", "plop"],
    "unk": ["skunk", "chunk", "gunk", "junk"],
    "ink": ["mink", "skink", "slink", "clink"],
    "at": ["rat", "gnat", "bat", "cat"],
}

# Word lists
adjectives = ["slimy", "stinky", "mouldy", "soggy", "squelchy", "gooey", "mucky"]
verbs = ["sloshed", "oozed", "plopped", "dripped", "squelched", "splats", "slurps"]

# Make a poem
rhyme_key = random.choice(list(rhymes.keys()))
print("Your rhyming sound is:", rhyme_key)
rhyme_words = rhymes[rhyme_key]
print("Your rhyming words are:", rhyme_words)

random.shuffle(adjectives)
random.shuffle(verbs)
random.shuffle(rhyme_words)

for i in range(2):
    print("🤢 The", adjectives.pop(), "thing", verbs.pop(), "like a", rhyme_words.pop())
