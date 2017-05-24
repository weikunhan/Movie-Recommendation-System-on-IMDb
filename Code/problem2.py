"""
 EE232E Project 2 Problem 2
 Name: Weikun Han, Duzhi Chen
 Date: 5/21/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Construct a weighted directed graph
"""

from __future__ import print_function
import re

# Print information
print(__doc__)
print()

# Open the file we create and the file we have
filename1 = open("./project_2_data/processedAct.txt", "r")
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
print 'movie dictionary has been initialized successfully with length %d!'%(len(movieDict))

#construct actor dictionary
actDict={}
actId=0
for line in filename2.readlines():
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
		print 'construct actDict: %d'%(actId)
	actId += 1
# print actDict
print 'actDict has been loaded successfully with length %d'%(len(actDict))
print 'movieDict have been loaded successfully with new length %d'%(len(movieDict))

# #---------------------------------------#
# ###########for problem 1-3#############
# #---------------------------------------#
# #add edge into edgeAct, which is a dict
 count = 0
 edgeAct={}
 for key in actDict:
 	for i in range(1,len(actDict[key])):
		movie = actDict[key][i]
 		for people in movieDict[movie]:
 			# don't count the actor himself
 			# 1st element of value of movieDict is set as movieId, skip this value
 			if people==key or isinstance(people,int):
 				continue
 			if edgeAct.has_key((actDict[key][0],actDict[people][0])):
 				edgeAct[(actDict[key][0],actDict[people][0])]+=1.0/(len(actDict[key])-1)
 			else:
 				edgeAct[(actDict[key][0],actDict[people][0])]=1.0/(len(actDict[key])-1)
 	if count%1000==0:
 		print 'construct edgeAct: %d'%(count)
 	count+=1
 print 'edgeAct has been construct successfully with %d records!'%(len(edgeAct))

# #write to file graphAct
 count = 0
 for key in edgeAct:
 	s = '%d\t%d\t%f\n'%(key[0],key[1],edgeAct[key])
 	file1.write(s)
 	if count%10000==0:
 		print 'write to file graphAct: %d'%(count)
 	count+=1
 # print edgeAct
 print "Act graph edge processed successfully!"
 #---------------------------------------#
 ############end of this part#############
 #---------------------------------------#
