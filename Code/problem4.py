"""
 EE232E Project 2 Problem 4
 Name: Weikun Han, Duzhi Chen
 Date: 5/26/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Construct a weighted undirected graph for the movie network (problem 5, 6 and 7)
"""

from __future__ import print_function
import re

# Print information
print(__doc__)
print()

# Open the file we create and the file we have
filename1 = open("./project_2_data/artist_movies2.txt", "r")
#filename1 = open("./project_2_data/artist_movies.txt", "r")
filename2 = open("./project_2_data/movie_genre.txt", "r")

# Target file we want to create
filename3 = open("./project_2_data/graph_movie3.txt", "w")
#filename3 = open("./project_2_data/graph_movie2.txt", "w")
#filename3 = open("./project_2_data/graph_movie.txt", "w")

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
movie_dict2 = {}
for movie in movie_dict:
	if(len(movie_dict[movie])) > 20 and len(movie)>0:
	#if(len(movie_dict[movie])) > 10 and len(movie)>0:
	#if(len(movie_dict[movie])) > 5 and len(movie)>0:
		movie_dict2[movie] = movie_dict[movie]
#print("Second movie dictionary has been created successfully with length %d!" % len(movie_dict2))


edgeMovie={}
edgeMovieDenom={}
for key in movie_dict2 :
	for i in range(1,len(movie_dict2 [key])):
		actor =  movie_dict2 [key][i]
		for movie in artist_dict[actor]:
			if movie==key or isinstance(movie,int) or (not movie_dict2 .has_key(movie)):
				continue
			totalAct = len(movie_dict2 [key])+len(movie_dict2 [movie])-2
			if edgeMovie.has_key((movie_dict2 [key][0],movie_dict2 [movie][0])):
				edgeMovie[(movie_dict2 [key][0],movie_dict2 [movie][0])]+=1
				edgeMovieDenom[(movie_dict2 [key][0],movie_dict2 [movie][0])]=totalAct
			elif edgeMovie.has_key((movie_dict2 [movie][0], movie_dict2 [key][0])):
				edgeMovie[(movie_dict2 [movie][0], movie_dict2 [key][0])]+=1
				edgeMovieDenom[(movie_dict2 [movie][0], movie_dict2 [key][0])]=totalAct
			else:
				edgeMovie[(movie_dict2 [key][0],movie_dict2 [movie][0])]=1
				edgeMovieDenom[(movie_dict2 [key][0],movie_dict2 [movie][0])]=totalAct


count=0
for key in edgeMovie:
	numerator = edgeMovie[key]/2
	denominator = edgeMovieDenom[key]-numerator
	weight = 1.0*numerator/denominator
	s = "%d\t%d\t%f\n" % (key[0], key[1], weight)
	filename3.write(s)
	count+=1
filename1.close()
filename2.close()
filename3.close()

# Print information
print("-------------------------Processing Finshed 1--------------------------")
print("Construct a weighted undirected graph for problem 5, 6 and 7 successfully!")
print("This is version of graph for movies which have over 20 actors/actresses")
print("This is version of graph for actors/actresses which have over 10 movies")
print("The total number of edges in graph is: %d" % count)
print("The total number of nodes in graph is: %d" % len(movie_dict2))
print("-----------------------------------------------------------------------")
print()
