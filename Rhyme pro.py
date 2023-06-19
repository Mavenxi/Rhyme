import requests

def find_rhyming_words(word):
    # Make a request to the Datamuse API to find rhyming words
    url = 'https://api.datamuse.com/words'
    params = {'rel_rhy': word}
    response = requests.get(url, params=params)
    rhyming_words = [f"[{word['word']}]" for word in response.json()]
    if response is None:
        return []

    # Return the 50 closest rhyming words
    return rhyming_words[:50]

# Ask the user for a word
word = input("Enter a word: ")

# Find rhyming words for the input word
rhyming_words = find_rhyming_words(word)

# Print the rhyming words
print(f"Rhyming words for '{word}': {', '.join(rhyming_words)}")

