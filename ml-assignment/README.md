# Trigram Language Model

This is my implementation of a trigram language model built from scratch. The model can read text, learn patterns, and generate new sentences that sound like the original writing.

## How to Run 

### Quick Start :

**(Using Example Text(Example_corpus.txt file))**

```bash
# Run the model with the included example text
python src/generate.py
```

**Enhanced Version (Using Real Books)**

```bash
# First, download a book (optional)
python src/download_book.py

# Then generate text - it will automatically use the book
python src/generate.py
```

**Testing**
```bash
# Run tests to make sure everything works
pytest tests/test_ngram.py -v
```

#### What to Expect

- With example text: The model generates short, meaningful sentences

- With books: The model captures the author's style and creates longer, more creative text

- Different each time: Due to probabilistic sampling, you get unique outputs on each run

## Design Choices

**I've documented all my design decisions in the evaluation.md file, including**:

- How I store word patterns

- How text cleaning and generation work

- Why I chose probabilistic sampling

- How I handle different text sizes