import spacy # Import the spacy module

nlp = spacy.load('en_core_web_sm') # Import the english language data

# Create list with sentences
gardenpathSentences = ["The old man the boat.",
                       "The complex houses married and single soldiers and their families.",
                       "These garden sentences did not get recognised on this 2nd Wednesday of November",
                       "Time magazine will take note of these 14 human rights violations",
                       "I hate the Jonas brothers said Arno"]

# Tokenise every sentence in the list and determine the entities and display result
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print("-"*70)
    print([(word, word.label_) for word in nlp_sentence.ents])

# The first unusual entity is in sentence 3 where I expected "2nd" to be a CARDINAL, but was determined to be a DATE
# The second unusual entity is in sentence 5 where I expected Arno to be a PERSON, but was determined to be a ORG

"""
NOTE TO THE MARKER/COURSE COORDINATORS

I encountered the following problems while trying to do this lesson:

- Installation of Spacy was difficult due to the following issues:
    - Installing current verion of spacy requires a 64 bit installation of python. The provided python installer was 32 bit.
    - Spacy requires Microsoft visual studio C++ build tools. The installation of which was complex
    
- The Garden path sentences in the wikipedia link provided failed to return any entities thus providing confusion regarding issues with spacy
or the sentences themselves. This is seen when running this program with the first two sentences in the list.
"""



