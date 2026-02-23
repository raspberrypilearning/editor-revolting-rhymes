<h2 class="c-project-heading--task">Print a specific rhyming sound</h2>

You can use an 'index' to print a specific item in a list.

--- task ---

Print the first item in the list.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 20
---
# Make a poem
rhyme_keys = list(rhymes.keys())
print(f'{rhyme_keys[0]}')

--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- Indexing starts at 0, so 0 is the index of the **first** item.

</div>

--- task ---

Run your code.

--- /task ---

<div class="c-project-output">
<pre>oop</pre>
</div>
