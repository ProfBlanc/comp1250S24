fav_movies = {
    "comedy": "Monty Python",
    "action": "Terminator",
    "horror": "IT",
    "sci-fi": "Interstellor"
}

fav_movies['musical'] = "Phantom Of The Opera"

print(fav_movies)
print(fav_movies['sci-fi'])
print(fav_movies['comedy'])

# ask user for their fav {genre} movie
# and determine if it's the same as yours
print()
for movie_genre in fav_movies:  # keys(), values(), items()
    question = "Enter your fav " + movie_genre + " movie: "
    answer = input(question)
    if answer == fav_movies[movie_genre]:
        print("Nice! We have the same favourite", movie_genre, "movie")
    else:
        print("Thanks for your answer. My favourite",movie_genre,
              "movie is", fav_movies[movie_genre])
