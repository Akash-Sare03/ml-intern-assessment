import pytest
import sys
import os

# Fix the import path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from ngram_model import TrigramModel

def test_fit_and_generate():
    model = TrigramModel()
    text = "I am a test sentence. This is another test sentence."
    model.fit(text)
    generated_text = model.generate()
    assert isinstance(generated_text, str)
    assert len(generated_text.split()) > 0

def test_empty_text():
    model = TrigramModel()
    text = ""
    model.fit(text)
    generated_text = model.generate()
    assert generated_text == ""

def test_short_text():
    model = TrigramModel()
    text = "I am."
    model.fit(text)
    generated_text = model.generate()
    assert isinstance(generated_text, str)