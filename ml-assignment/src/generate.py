
from ngram_model import TrigramModel
import os

def main():
    # Create our trigram model
    model = TrigramModel()

    # let's figure out where our data folder is located
    # We need to be careful about file paths since the script might run from different locations
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_script_dir, "..", "data")
    
    # First, let's see what text files we have available to train on
    # We'll look for any .txt files in the data folder, but skip the small example corpus
    # if we can find something more substantial to work with
    book_file = None
    for file in os.listdir(data_folder):
        # We're looking for text files
        # if there are actual books available
        if file.endswith('.txt') and file != 'example_corpus.txt':
            book_file = file
            break  # We'll just use the first book we find
    
    # Load our training text - either a proper book or the example corpus
    if book_file:
        book_path = os.path.join(data_folder, book_file)
        print(f"Found a book to train on: {book_file}")
        print("Loading the book text...")
        with open(book_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        # Fall back to the example corpus if no books found
        example_path = os.path.join(data_folder, "example_corpus.txt")
        if os.path.exists(example_path):
            print("No book files found, using the example corpus instead...")
            with open(example_path, "r") as file:
                text = file.read()
        else:
            print("Couldn't find any text files to train on!")
            print("Please make sure there are .txt files in the data folder.")
            return
    
    # Train our model on the selected text
    model.fit(text)

    # Generate new text
    generated_text = model.generate()
    
    print("\n" + "="*50)
    print("Generated Text:")
    print("="*50)
    print(generated_text)
    print("="*50)

if __name__ == "__main__":
    main()