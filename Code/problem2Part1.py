"""
 EE232E Project 2 Problem 2 Part1
 Name: Weikun Han, Duzhi Chen
 Date: 5/21/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Construct a weighted directed graph for problem 3
"""

from __future__ import print_function
import re
# Open the file we create and the file we have
filename1 = open("./project_2_data/artist_movies.txt", "r")
filename2 = open("./project_2_data/movie_genre.txt", "r")

# Target file we want to create
file1 = open("./project_2_data/artist_graph.txt", "w")
file2 = open("./project_2_data/moive_graph.txt", "w")

#construct movie dictionary
movieDict={}
movieId=0
for line in filename2.readlines():
    tokens = line.split("\t\t")
    movieDict[tokens[0]]=[movieId]
    movieId+=1
print('movie dictionary has been initialized successfully with length %d!'%len(movieDict))

#construct actor dictionary
actDict={}
actId=0
for line in filename1.readlines():
	tokens = line.split("\t\t")
	name = tokens[0]
	# the starting element of the array is set as the actor's ID, which is also used as node ID
	tokens[0] = actId

	for i in range(1,len(tokens)):
		movie = tokens[i]
		year = re.search(r'\(\d\d\d\d\)|\(\?\?\?\?\)', movie)
		if year:
			end = movie.find(year.group())
			tokens[i] = movie[:end+6]

		if movieDict.has_key(tokens[i]):
			movieDict[tokens[i]].append(name)
		else:
			movieDict[tokens[i]]=[len(movieDict)]
			movieDict[tokens[i]].append(name)
	actDict[name] = tokens
	if actId%5000==0:
		print('construct actDict: %d'%actId)
	actId += 1
# print actDict
print('actDict has been loaded successfully with length %d'%len(actDict))
print('movieDict have been loaded successfully with new length %d'%len(movieDict))


# old method to construct graphAct, which is really really really really slow so is deprecated
# could be used to testify the correctness of graphAct
# print "finished loading data, processing the graph edge..."
count=0
for outterkey in actDict:
 	for innerkey in actDict:
 		if outterkey == innerkey:
 			continue
 		intersect = len(set(actDict[outterkey]) & set(actDict[innerkey]))
 		if intersect > 0:
 			weight = 1.0*intersect/(len(actDict[outterkey])-1)
 			Edge = "%d\t%d\t%f\n"%(actDict[outterkey][0],actDict[innerkey][0],weight)
 			file1.write(Edge)
 	count +=1
 	if count%10 == 0 :
 		print(count)

filename1.close()
filename2.close()
file1.close()
file2.close()
