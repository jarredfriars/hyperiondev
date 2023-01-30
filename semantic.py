import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# This output is interesting as the monkey has a higher similarity with banana than apple, however the cat has equally
# low similarity to both fruit. The model understands that monkeys eat bananas and cats do not eat fruit.
# it also notices that the banana and apple are fruits and that cat and monkey are animals but knows they are different
# and not the same species with just different spellings

# en_core_web_md output:

# cat cat 1.0
# cat apple 0.2036806046962738
# cat monkey 0.5929930210113525
# cat banana 0.2235882580280304
# apple cat 0.2036806046962738
# apple apple 1.0
# apple monkey 0.2342509925365448
# apple banana 0.6646699905395508
# monkey cat 0.5929930210113525
# monkey apple 0.2342509925365448
# monkey monkey 1.0
# monkey banana 0.4041501581668854
# banana cat 0.2235882580280304
# banana apple 0.6646699905395508
# banana monkey 0.4041501581668854
# banana banana 1.0

print("\n")

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# This output was only able to accurately guess the similarities between exactly identical items.
# The similarity between the monkey was actually higher with the apple than the banana and the cat surprisingly had
# a very high similarity to an apple

# en_core_web_sm output:

# cat cat 1.0
# cat apple 0.7018378973007202
# cat monkey 0.6455236077308655
# cat banana 0.2214718759059906
# apple cat 0.7018378973007202
# apple apple 1.0
# apple monkey 0.7389943599700928
# apple banana 0.36197030544281006
# monkey cat 0.6455236077308655
# monkey apple 0.7389943599700928
# monkey monkey 1.0
# monkey banana 0.4232020080089569
# banana cat 0.2214718759059906
# banana apple 0.36197030544281006
# banana monkey 0.4232020080089569
# banana banana 1.0
