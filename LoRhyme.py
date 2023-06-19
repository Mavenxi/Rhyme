import requests
from bs4 import BeautifulSoup

def find_rhyming_words(word):
    url = f'https://www.rhymezone.com/r/rhyme.cgi?Word={word}&typeofrhyme=perfect&org1=syl&org2=l&org3=y'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rhyme_dict = {}
    rhyme_list = soup.find_all('a', attrs={'class': 'r'})
    for rhyme in rhyme_list:
        syllables = len(rhyme['href'].split('=')[-1].split('_'))
        if syllables in rhyme_dict:
            rhyme_dict[syllables].append(rhyme.text)
        else:
            rhyme_dict[syllables] = [rhyme.text]
    return rhyme_dict

word = input("Enter a word: ")
rhyme_dict = find_rhyming_words(word)

# Sort the dictionary by key
rhyme_dict = dict(sorted(rhyme_dict.items()))

# Print out the rhyming words by syllable count
for syllables, words in rhyme_dict.items():
    print(f"{syllables}-syallable words: {', '.join(words)}")
