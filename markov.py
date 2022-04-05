"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_file = open(file_path).read()
    text_string = full_file.split()
    
    print(text_string)
    return text_string
    
    #'Contents of your file as one long string'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    pairs = ()
    
    #words = text_string.split()d
    for i in range(0,len(text_string)-2):
        #create pair in tuple
        found = []
        pairs = (text_string[i], text_string[i+1]) 
        #add tuple as a key to the chains dictionary
        if text_string[i] == pairs[0] and text_string[i+1] == pairs[1]:
            value_to_add = text_string[i+2]
            found.append(value_to_add)
        chains[pairs] = found


        

    # your code goes here
    print(f'this be the {chains}')
    return chains

    #make keys for the chain pairs
    #key values are possible next word (sequence) to both values in key
    #how to find next word after
    #iterate and check next word
    # for key in chains:
    #     if key in text_string:
    #         chains[key] = 

    # for i in range(0,len(text_string)):
        
    #     if chains[key] == text_string[i]
    #         chains[value] == text_string[i+1]

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
open_and_read_file(input_path)