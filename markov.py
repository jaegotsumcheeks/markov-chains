"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    read_file = open(file_path).read()
    return read_file

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

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
    text_list = text_string.split()
#    for i,word in enumerate(text_list):
#        empty_list = chains.get((word, text_list[i+1]),[])
#        chains[(word,text_list[i+1])] = empty_list
    for i in range(len(text_list)-2):
        #print(text_list[i])      
        new_list = chains.get((text_list[i],text_list[i+1]),[])
        #print(new_list)
        new_list.append(text_list[i+2])
        chains[(text_list[i],text_list[i+1])] = new_list
        print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    
    current_words = ('Would', 'you')
    words = ['Would']  
    valid_key = chains.get(current_words,False)
    while (valid_key is not False):
        first_random_word = choice(chains[current_words])
        next_step = (current_words[1],first_random_word)
        words.append(first_random_word)
        current_words = next_step
        valid_key = chains.get(current_words,False)
        
        print(next_step)
    
    
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
