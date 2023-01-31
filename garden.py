#I.D 1
# This is an NLP example program that takes 5 garden path like sentences and uses
# Tokenise and perform Entity recognition for each of the sentences
# after they have been stored in a list called 'gardenpathSentences'.
# look up and write the entities spaCy has categorised these in these sentences
# that I don't understand

# Tokenisation is a foundational step in many NLP tasks. Tokenising text is the
# process of splitting a piece of text into words, symbols, punctuation, spaces,
# and other elements, thereby creating “tokens”. A naive way to do this is to
# simply split the string on white space:

import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentences = ("""Helen is expecting tomorrow to be a bad day. 
India gave the child the dog bit a Band-Aid. 
When Fred eats food gets thrown. 
That Jill is never here hurts.
The man who marks walls out on weekends.""")

doc = nlp(garden_path_sentences)

print([token.orth_ for token in doc if not token.is_punct | token.is_space])  # splits the text in the sentence

# for loop below identifies stop words
for word in doc:
    if word.is_stop == True:
        print(word)


nlp_garden_path_sentences = nlp(garden_path_sentences)

# This performs the entity recognition
print([(i, i.label_, i.label) for i in nlp_garden_path_sentences.ents])

# two unusual entities:
# - a bad day = 'Date' is not an actual date
# - india = 'GPE' when we would know it is a name and not a reference to a country
