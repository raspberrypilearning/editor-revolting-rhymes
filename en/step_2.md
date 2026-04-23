<h2 class="c-project-heading--task">Print a specific rhyming sound</h2>

You can use an **index** to print a specific item in a list.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>
Print the first item in the list.

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

### Tip

<div class="c-project-callout c-project-callout--tip">

Indexing starts at 0, so 0 is the index of the **first** item.

</div>

## Now run your code

You should see `oop`.

<div class="c-project-output">
<pre>oop</pre>
</div>
