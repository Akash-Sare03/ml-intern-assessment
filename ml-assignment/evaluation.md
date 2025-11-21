# Evaluation

## Trigram Model - My Design Choices

### What I Built
I created a trigram language model from scratch that can read text, learn word patterns, and generate new sentences. It works with both small example texts and full books.

### How I Store Word Patterns :

I used nested dictionaries to remember how words follow each other:

```python
self.counts["the"]["cat"]["sat"] = 5  # "the cat sat" appeared 5 times
```

**Why I chose this** :

- It feels natural - like how we actually think about word sequences

- Python handles missing words automatically

- It's fast and doesn't waste memory

- I considered using tuples like ("the", "cat", "sat") but the nested dictionaries felt more intuitive for looking up patterns.

### How I Clean and Prepare Text :
**Cleaning**:

- Make everything lowercase so "The" and "the" are treated the same

- Keep basic punctuation (., !, ?) but remove complicated symbols

- Split text into individual words

**Padding**:
- I add special tokens to mark where sentences start and end:

- [<'start'>, <'start'>] at the beginning (we need 2 words to start predicting)

- [<'end'>] at the end to know when to stop

**Unknown Words**:
If the model encounters words it hasn't seen before during generation, it simply stops rather than guessing. For this project, this approach worked well enough.

### How Text Generation Works :
The generation process is like a word-by-word chain:

- Start with: [<'start'>, <'start'>]

- Look at the last 2 words and see what words usually follow them

- Pick the next word randomly, but give more common words higher chances

- Repeat until we hit <end> or reach the maximum length

**Why random instead of always picking the most common word?**

- It makes the output more varied and interesting

- It sounds more natural - in real language, we don't always use the most common next word

- Each run produces different results

### Other Decisions I Made :

#### Added Book Download Feature :

- I added an optional download_book.py file that can download "Alice in Wonderland" from Project Gutenberg.

- **How it works**:

- Checks if the book already exists (so you don't download it twice)

- Cleans up the text by removing the Gutenberg header/footer

- Saves just the story content

- have two options:

- With book: Run download_book.py first, then generate.py will automatically use the book

- Without book: Just run generate.py and it uses the example corpus

- This shows the model can handle both small examples and real books.

**Output Formatting**:

- Fix spacing around punctuation (remove space before periods, etc.)

- Capitalize the first letter of generated text

- Add a period if the text ends without proper punctuation

**Error Handling**:

- The code handles empty files gracefully

- Works no matter where you run it from

- Gives clear messages about what's happening


### What Works Well
- The model learns patterns accurately.

- With small texts, it generates sensible sentences using the vocabulary it learned

- With books like Alice in Wonderland, it captures the author's unique style

- The probabilistic sampling creates different outputs each time

- All the tests pass successfully