import urllib.request
import os

def download_alice_in_wonderland():
    """
    Downloads Alice in Wonderland from Project Gutenberg if we don't already have it.
    We'll clean up the text by removing the Gutenberg header and footer sections,
    then save just the story content for our model to learn from.
    """
    # First, let's make sure we have a data folder to put our book in
    # We need to figure out the right path since the script might run from different locations
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(current_script_dir, "..", "data")
    book_filename = "alice_in_wonderland.txt"
    book_path = os.path.join(data_folder, book_filename)
    
    # Create the data folder if it doesn't exist yet
    # This prevents those pesky "folder not found" errors
    os.makedirs(data_folder, exist_ok=True)
    
    # Check if we already downloaded this book - no need to do it twice!
    if os.path.exists(book_path):
        print(f"Great! '{book_filename}' is already in our data folder.")
        print("We can use it directly without downloading again.")
        return True
    
    print("Downloading Alice in Wonderland from Project Gutenberg...")
    
    try:
        # Project Gutenberg makes these classic books available for free
        # We're using their direct file link for Alice in Wonderland
        url = "https://www.gutenberg.org/files/11/11-0.txt"
        response = urllib.request.urlopen(url)
        text = response.read().decode('utf-8')
        
        print("Download complete! Now cleaning up the text...")
        
        # The downloaded file has some extra Gutenberg information at the start and end
        # Let's find where the actual story begins and ends
        lines = text.split('\n')
        
        # We'll look for the beginning of Chapter 1 to find where the story really starts
        start_index = 0
        end_index = len(lines)
        
        for i, line in enumerate(lines):
            if "CHAPTER I" in line and "Down the Rabbit-Hole" in line:
                start_index = i
                print("Found the start of the story at Chapter 1")
                break
                
        # Look for the Gutenberg footer that marks the end of the book content
        for i, line in enumerate(lines):
            if "End of the Project Gutenberg" in line:
                end_index = i
                print("Found the end of the story content")
                break
        
        # Extract just the story part, leaving behind the metadata
        story_lines = lines[start_index:end_index]
        clean_text = '\n'.join(story_lines)
        
        # Save our cleaned-up story to a file
        # We're using UTF-8 encoding to handle any special characters properly
        with open(book_path, "w", encoding="utf-8") as f:
            f.write(clean_text)
        
        print(f"Success! Saved the book to: {book_filename}")
        print(f"We now have {len(clean_text)} characters of classic literature to work with!")        
        return True
        
    except Exception as e:
        # If anything goes wrong
        print(f"Oops! We ran into a problem while downloading the book: {e}")
        return False

if __name__ == "__main__":
    download_alice_in_wonderland()