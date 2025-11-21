import random
from collections import defaultdict

class TrigramModel:
    def __init__(self):
        """
        Initializes the Trigram Model.
        We're using nested dictionaries to track how often sequences of three words appear together.
        For example, if counts["the"]["cat"]["sat"] = 3, it means "the cat sat" occurred 3 times in our text.
        """
        # Using defaultdict here saves us from checking if keys exist - it automatically creates new entries
        self.counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        self.vocab = set()  # Keeping track of all unique words we encounter
    
    def clean_and_tokenize(self, text):
        """
        Prepares the text for processing by cleaning and breaking it into words.
        We convert everything to lowercase for consistency and remove most punctuation,
        keeping only what's needed for basic sentence structure.
        """
        # Handle empty text right away
        if not text or text.strip() == "":
            return []
        
        # Start by making everything lowercase - this helps with pattern matching
        text = text.lower()
        
        # Build our cleaned text character by character
        # We want to keep letters, numbers, spaces, and basic sentence punctuation
        cleaned_chars = []
        for char in text:
            # We're keeping the essentials: words, spaces, and meaningful punctuation
            if char.isalnum() or char.isspace() or char in ['.', '!', '?']:
                cleaned_chars.append(char)
            # Note: We're intentionally skipping quotes, dashes, and other special characters
            # to keep things simple for this version
        
        cleaned_text = ''.join(cleaned_chars)
        
        # Simple word splitting - in a more advanced version we might handle
        # punctuation that's attached to words differently
        words = cleaned_text.split()
        
        return words

    def fit(self, text):
        """
        Trains our model on the provided text.
        
        The process involves:
        1. Cleaning and breaking the text into individual words
        2. Adding special tokens to mark where sentences start and end
        3. Counting how often each three-word sequence appears
        """
        # First, let's clean and split our text into manageable pieces
        words = self.clean_and_tokenize(text)
        if not words:
            print("No valid text found to train on.")
            return
        
        # We need to pad our text with special tokens
        # Using two <start> tokens because we always look at the previous two words
        # to predict the third one in our trigram approach
        padded_words = ['<start>', '<start>'] + words + ['<end>']
        
        # Now we'll slide through the text with a three-word window
        # and count every sequence we encounter
        for i in range(len(padded_words) - 2):
            first_word = padded_words[i]
            second_word = padded_words[i + 1] 
            third_word = padded_words[i + 2]
            
            # Record this three-word sequence in our counts
            self.counts[first_word][second_word][third_word] += 1
            
            # Keep track of all unique words we've seen
            self.vocab.update([first_word, second_word, third_word])
        
        # Let the user know how the training went
        unique_word_count = len(self.vocab)
        print(f"Training finished! The model learned {unique_word_count} unique words and their patterns.")

    def generate(self, max_length=100):
        """
        Creates new text by following the patterns learned during training.
        
        We start with beginning markers and repeatedly:
        1. Look at the last two words
        2. Choose the next word based on what typically followed similar pairs
        3. Continue until we hit an end marker or reach our length limit
        """
        # Start with our beginning context - we need two words to get started
        current_words = ['<start>', '<start>']
        output_words = []
        
        # Keep generating until we hit our limit or naturally end
        for step in range(max_length):
            # Our current context is the last two words we have
            prev_word = current_words[-2]
            current_word = current_words[-1]
            
            # Check if we know what words typically follow this pair
            if (prev_word in self.counts and 
                current_word in self.counts[prev_word] and 
                self.counts[prev_word][current_word]):
                
                # Get all possible next words and how often they appear
                possible_next_words = self.counts[prev_word][current_word]
                word_options = list(possible_next_words.keys())
                frequency_counts = list(possible_next_words.values())
                
                # Convert raw counts to probabilities
                total_occurrences = sum(frequency_counts)
                likelihoods = [count / total_occurrences for count in frequency_counts]
                
                # Choose the next word randomly, but weighted by how common it was in training
                chosen_word = random.choices(word_options, weights=likelihoods, k=1)[0]
                
                # If we hit the end marker, we're done
                if chosen_word == '<end>':
                    break
                    
                # Add our chosen word to the output and update our context
                output_words.append(chosen_word)
                current_words.append(chosen_word)
            else:
                # If we don't know what comes next, it's time to stop
                break
        
        # Now let's clean up our generated text for better readability
        final_text = ' '.join(output_words)
        
        # Fix spacing around punctuation - words should touch their punctuation
        final_text = final_text.replace(' .', '.')
        final_text = final_text.replace(' ,', ',')
        final_text = final_text.replace(' !', '!')
        final_text = final_text.replace(' ?', '?')
        
        # Make sure our text starts with a capital letter
        #if final_text:
         #   final_text = final_text[0].upper() + final_text[1:]
        
        # If we ended without proper punctuation, add a period
        # but only if we have at least a short sentence
        if final_text and final_text[-1] not in ['.', '!', '?']:
            if len(final_text.split()) >= 3:
                final_text += '.'
        
        return final_text
    
    