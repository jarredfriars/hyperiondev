# I.D. 1
# This programs takes the description of a movie the user has watched and finds
# the most similar movie from a list of movies in the file 'movies.txt'
# IMPORTANT - Install 'en_core_web_md' by typing 'python -m spacy download en_core_web_md' into your command line

import spacy  # imports the spacy library

nlp = spacy.load('en_core_web_md')  # creates the nlp variable to compare the similarities

# below is the movie title we will be comparing the list of movies against
movie_to_compare = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator"""

movies_file = open("movies.txt", "r")

movies_file = movies_file.readlines()

movies_list = []

for line in movies_file:
    movies_file = line.strip().split(":")
    movies_list.append(movies_file)

print(movies_list)


# The function below
# uses the movie_to_compare and checks it's similarity with each movie from the movies.txt file (movies_list)
# it then outputs the movie with the highest similarity
def find_movie_most_similar(movie_to_compare):
    if movies_list and movie_to_compare:
        nlp_movie_to_compare = nlp(movie_to_compare)
        for index, movie in enumerate(movies_list):
            similar_score = nlp(movie[1]).similarity(nlp_movie_to_compare)
            movies_list[index].append(similar_score)
        movies_list.sort(key=lambda x:x[2], reverse=True)
    return movies_list[0][0]


movie_to_watch = find_movie_most_similar(movie_to_compare)

print(f"The movie '{movie_to_watch}' has the highest similarity score")
