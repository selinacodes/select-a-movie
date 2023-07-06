from csv import DictReader
import sys
import os

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    exit(f"The file {file_path} doesn't exist")

movie_choices = {}

with open(file_path, 'r') as f:
    for row in DictReader(f, delimiter=','):
        genres = row['Genres'].lower()
        genres = genres.split(',')
        for index, genre in enumerate(genres):
            genre = genre.strip(' ')
            genres[index] = genre

        for genre in genres:
            title = row['Title']
            rating = float(row['IMDb Rating'])
            duration = int(row['Runtime (mins)'])
            year = int(row['Year'])
            movie = (title, rating, duration, year)

            if genre in movie_choices:
                movie_choices[genre].append(movie)
            else:
                movie_choices[genre] = [movie]

    genre = input('What genre would you like to watch?')
    if genre not in movie_choices:
        os.abort('Your chosen genre is unavailable.')

    min_rate = float(input('What is the minimum rating of a movie you want to watch?'))
    max_duration = int(input('How much time do you have (in mins?)'))
    min_year = int(input('How recent should the movie be?'))

    to_watch = []

    for movie in movie_choices[genre]:
        if movie[1] < min_rate:
            continue
        if movie[2] > max_duration:
            continue
        if movie[3] < min_year:
            continue
        to_watch.append(movie)

    print(to_watch)
