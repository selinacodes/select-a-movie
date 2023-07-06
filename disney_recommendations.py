from csv import DictReader
from datetime import datetime
import sys
import os
import re

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    exit(f"The file {file_path} doesn't exist, try again.")

movie_choices = {}

with open(file_path, 'r') as f:
    for row in DictReader(f, delimiter=','):
        genres = row['listed_in'].lower()
        genres = genres.split(',')
        for index, genre in enumerate(genres):
            genre = genre.strip(' ')
            genres[index] = genre

        for genre in genres:
            title = row['title']

            type = row['type'].lower()
            if type == 'tv show':
                type = 'show'

            duration = row['duration']
            year = int(row['release_year'])

            choice = (title, type, duration, year)

            if genre in movie_choices:
                movie_choices[genre].append(choice)
            else:
                movie_choices[genre] = [choice]

    genre = input('What genre would you like to watch?')
    if genre not in movie_choices:
        print('Your chosen genre is unavailable.', file=sys.stderr)
        sys.exit()

    media = input('Do you want a movie ("movie") or a tv show ("show")?')
    if media != 'show' and media != 'movie':
        print('Your chosen media is unavailable.', file=sys.stderr)
        sys.exit()

    years = input('Enter earliest release year and latest release year (e.g.: "1990, 2010"):').split(',')
    if len(years) != 2:
        print('Enter only two years.', file=sys.stderr)
        sys.exit()
    for index, date in enumerate(years):
        years[index] = int(date.strip(' '))
    date_start = years[0]
    date_end = years[1]
    print('Your chosen date range is {} to {}'.format(date_start, date_end))

    to_watch = []
    for movies_genre, movies in movie_choices.items():
        if movies_genre != genre:
            continue
        for movie in movies:
            if movie[1] != media:
                continue
            if movie[3] < date_start or movie[3] > date_end:
                continue
            to_watch.append(movie)

    print(to_watch)



    # # to_watch = []

    # # for choice in movie_choices[genre]:
    # #     if choice[1] == media:
    # #         continue
    # #     if choice[3] < range_year:
    # #         continue
    # #     to_watch.append(choice)

    # print(to_watch)
