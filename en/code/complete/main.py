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
adjectives = ["slimy", "stinky", "mouldy", "soggy", "squelchy", "gooey", "mucky"]
verbs = ["sloshes", "oozes", "plops", "drips", "squelches", "splats", "slurps"]


# Make a poem
def make_poem(lines=4, rhyme_key=None, emoji="🤢"):

    # Pick a rhyme group at random
    if rhyme_key is None:
        rhyme_key = random.choice(list(rhymes.keys()))
    if rhyme_key not in rhymes:
        rhyme_key = random.choice(list(rhymes.keys()))

    rhyme_words = rhymes[rhyme_key]

    # Shuffle everything once
    random.shuffle(rhyme_words)
    random.shuffle(adjectives)
    random.shuffle(verbs)

    poem = []

    for i in range(lines):
        # Use modulo (%) so we never go out of range
        end = rhyme_words[i % len(rhyme_words)]
        adj = adjectives[i % len(adjectives)]
        verb = verbs[i % len(verbs)]

        line = "{} The {} thing {} like a {}".format(emoji, adj, verb, end)
        poem.append(line)

    return poem, rhyme_key


print("Welcome to Revolting Rhymes!\n")

lines_input = input("How many lines would you like? (default 4): ")
try:
    lines = int(lines_input)
    if lines < 1:
        lines = 4
except:
    lines = 4

print("\nAvailable rhyme groups (keys):")
print(", ".join(sorted(rhymes.keys())))
group_choice = input("Pick a group key (or press Enter for random): ").strip()
if group_choice == "":
    group_choice = None

# Make and print the poem
poem, used_group = make_poem(lines=lines, rhyme_key=group_choice)

print("\n--- Your Revolting Poem ---")
print("(Rhyming group used: {})\n".format(used_group))
for line in poem:
    print(line)
print("\nDelightfully revolting! Run again to make a new one.")
