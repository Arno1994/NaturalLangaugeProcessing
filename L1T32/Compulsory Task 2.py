import spacy # Import spacy for NLP
nlp = spacy.load('en_core_web_md')# Import advanced english model

def movie_recommend(current_movie_desc):
    """ In this function a description of the current movie is received.
        The function will take every line in the movies.txt document and add them to a new list
        The current movie description is tokenised and then loops through every description
        in the movie list and tokenise each and checks similairty to the current
        movie. The similarity score is then compared to the previous similarity score and if
        it is higher it is then replaced with the current one and the associated movie overwrites
        the previous movie. When it is done looping the movie with the highest similarity is
        printed out."""
    
    movie_list = [] # Creat and empty list
    # Open movies.txt file and loop through every line
    with open('movies.txt', 'r') as movie:
        for line in movie:
            line_strip = line.strip()
            movie_list.append(line_strip)

    current_similarity = 0
    current_movie_description_token = nlp(current_movie_desc)
    for movie in movie_list:
        # Cut out the "Movie A :" section of every line before tokenising the string
        movie_token = nlp(movie[9:]) 
        similarity_score = movie_token.similarity(current_movie_description_token)
        if similarity_score > current_similarity:
            current_similarity = similarity_score
            movie_str = movie

    print("Your recommended movie is:")
    print(movie_str)
    
movie_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the\
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk\
can live in peace. Unfortunately, Hulk land on the net Sakaar where he is sold into slavery\
and trained as a gladiator."

movie_recommend(movie_desc)
