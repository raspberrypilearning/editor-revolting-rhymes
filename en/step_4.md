<h2 class="c-project-heading--task">Fix the formatting</h2>
--- task ---
Use `.lower()` and `.title()` on the words inside the f-strings.
--- /task ---

<h2 class="c-project-heading--explainer">Make the words readable</h2>

Some words are in uppercase. Let’s make them nicer to read!

- Use `.lower()` to make letters lowercase
- Use `.title()` to make the creature name look special

Update each of the `print()` lines. Two lines have been done for you below.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 10
line_highlights:
---
f'{emoji}In the {place.lower()} I found a {creature.title()}'
f'The air smelled like {smell.lower()}'
--- /code ---
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure your parentheses and curly braces match correctly when calling methods inside a string.

</div>
