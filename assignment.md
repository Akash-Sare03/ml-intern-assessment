# AI/ML Intern Assignment

(** Task 2 is completely optional **)

## Task 1: Build an N-Gram Language Model

The implementation is the real test. You must design a clean and efficient system from scratch.

It tests your core Python skills:
- How do you store the n-gram counts (e.g., a nested dictionary like `counts[w1][w2][w3]`)?
- How do you handle text cleaning, padding, and unknown words?

The hardest part is the `generate` function. You must correctly convert counts to probabilities and then probabilistically sample from that distribution (not just pick the single most-likely word).

The ideal source for this is Project Gutenberg, which offers thousands of free, public-domain e-books.

 We recommend using one of these classic (and popular for NLP) books. They are large enough to produce interesting results but small enough to train quickly.
    1. Alice's Adventures in Wonderland by Lewis Carroll
    2. Pride and Prejudice by Jane Austen
    3. Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley
    4. A Tale of Two Cities by Charles Dickens

## Requirements 

The goal of this assignment is to test your foundational understanding of probabilistic language modeling and your practical Python skills. Your task is to build a trigram (N=3) language model from scratch.(Use N = 3)
- Your implementation should be able to handle text cleaning, padding, and unknown words.
- The `generate` function should be able to generate new text based on the trained model.
- Your code should be well-documented and easy to understand.
- You should provide a 1-page summary of your design choices in `evaluation.md`.
- Write code extracting and cleaning data

## Hints

- Start by implementing the `fit` method to train the model on a given text.
- Then, implement the `generate` method to generate new text.
- Use a nested dictionary to store the n-gram counts.
- Think about how to handle the beginning and end of sentences.
- Consider using a special token for unknown words.
- For the `generate` function, you will need to convert the counts to probabilities and then use a probabilistic sampling method to choose the next word.



## Task 2: Implement Scaled Dot-Product Attention (Optional)

This task tests your deep understanding of the core mechanism behind the Transformer architecture ("Attention Is All You Need"). It is a pure math-to-code translation.
We want to see if you can implement the Scaled Dot-Product Attention formula from scratch using only numpy. This tests your grasp of the underlying linear algebra and data flow that powers models like BERT and GPT.

## Requirements

1. You must create a Python function scaled_dot_product_attention(Q, K, V, mask=None).
2. Allowed Libraries: You may only use numpy for all numerical computations. You may not use scipy, tensorflow, pytorch, or any other ML library for this task.
3. Input: The function should accept three numpy arrays: Q (Queries), K (Keys), and V (Values), and an optional mask.
4. Output: The function should return two numpy arrays: the final attended output and the attention weights (the result of the softmax).
5. Your code must be well-documented with comments explaining each step.You must provide a small demonstration (e.g., in a separate script or notebook) showing your function working with sample Q, K, and V matrices.
6. Add a brief explanation of your attention implementation (and the demonstration) to your evaluation.md file.

*For Task 2 create a new directory within and implement*