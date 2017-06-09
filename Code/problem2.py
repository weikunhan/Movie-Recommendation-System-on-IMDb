"""
 EE232E Project 2 Problem 2
 Name: Weikun Han, Duzhi Chen
 Date: 5/21/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Construct a weighted directed graph for the actor/actress network (problem 3)
"""

from __future__ import print_function
import re

# Print information
print(__doc__)
print()

# Open the file we create and the file we have
filename1 = open("./project_2_data/artist_movies.txt", "r")
filename2 = open("./project_2_data/movie_genre.txt", "r")

# Target file we want to create
filename3 = open("./project_2_data/artist_graph.txt", "w")

# Construct movie dictionary
movie_dict = {}
movie_id = 1
for line in filename2.readlines():
    tokens = line.split("\t\t")
    moive = tokens[0]
    movie_dict[moive] = [movie_id]
    movie_id += 1
#print("Movie dictionary has been initialized successfully with length %d!" % len(movie_dict))

# Construct actor dictionary
artist_dict = {}
artist_id = 1
for line in filename1.readlines():
    tokens = line.split("\t\t")
    name = tokens[0]
    tokens[0] = artist_id

    # Start from 1 because the index 0 is artist ID (the node ID in graph)
    # movie_dict = {'movie_name1':[ID, artist1, artist2], 'movie_name2':[],...}
    # artist_dict = {'artist_name1':[ID, movie1, movie2], 'artist_name2':[]...}
    for i in range(1, len(tokens)):
        movie = tokens[i]
        year = re.search(r'\(\d\d\d\d\)|\(\?\?\?\?\)', movie)
        if year:
            end = movie.find(year.group())
            tokens[i] = movie[:end + 6]
        if movie_dict.has_key(tokens[i]):
            movie_dict[tokens[i]].append(name)
        else:
            movie_dict[tokens[i]] = [len(movie_dict)]
            movie_dict[tokens[i]].append(name)
    artist_dict[name] = tokens
    artist_id += 1
#print("Artist dictionary has been created successfully with length %d!" % len(artist_dict))
#print("New movie dictionary has been created successfully with length %d!" % len(movie_dict))

# Construct edge dictionary
edge_dict = {}
for people1 in artist_dict:
    for i in range(1,len(artist_dict[people1])):
        movie = artist_dict[people1][i]
        for people2 in movie_dict[movie]:
            if people2 == people1 or isinstance(people2, int):
                continue
            if edge_dict.has_key((artist_dict[people1][0], artist_dict[people2][0])):
                edge_dict[(artist_dict[people1][0], artist_dict[people2][0])] += 1.0 / (len(artist_dict[people1]) - 1)
            else:
                edge_dict[(artist_dict[people1][0], artist_dict[people2][0])] = 1.0 / (len(artist_dict[people1]) - 1)
#print("Edge dictionary has been created successfully with length %d!" % len(edge_dict))

# Store data into the .txt file
count = 0
for key in edge_dict:
    s = "%d\t%d\t%f\n" % (key[0], key[1], edge_dict[key])
    filename3.write(s)
    count += 1
filename1.close()
filename2.close()
filename3.close()

# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Construct a weighted directed graph for problem 3 successfully!")
print("The total number of edges in graph is: %d" % count)
print("The total number of nodes in graph is: %d" % len(movie_dict))
print("--------------------------------------------------------------------")
print()
