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

garden_path_sentences = ("""I know the words to that song about the queen don’t rhyme. 
She told me a little white lie will come back to haunt me. 
The dog that I had really loved bones. 
That Jill is never here hurts.
The man who whistles tunes piano.""")

doc = nlp(garden_path_sentences)

print([token.orth_ for token in doc if not token.is_punct | token.is_space])  # splits the text in the sentence

# for loop below identifies stop words
for word in doc:
    if word.is_stop == True:
        print(word)


nlp_garden_path_sentences = nlp(garden_path_sentences)

# This performs the entity recognition
print([(i, i.label_, i.label) for i in nlp_garden_path_sentences.ents])

# I didn't get any unusual entities when printing my sentences, only the number '380' after person
