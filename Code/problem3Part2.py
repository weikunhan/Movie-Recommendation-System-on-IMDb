"""
 EE232E Project 2 Problem 3 Part 2
 Name: Weikun Han, Duzhi Chen
 Date: 5/25/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Show top 20 artist name in pagerank_score.txt
"""

from __future__ import print_function
import string

# Print information
print(__doc__)
print()

# Open the file we create and the file we have
filename1 = open("./pagerank_score.txt", 'r')
filename2 = open("./project_2_data/artist_movies.txt", "r")

# Target file we want to create
filename3 = open("./project_2_data/pagerank_name.txt", 'w')

# Construct artist ID array and pagerank score array
node = []
score = []
for line in filename1.readlines():
    index = 0
    for i in line:
        if i == " ":
            break
        index += 1
    node.append(int(line[1:index - 1]))
    score.append(string.atof(line[index + 1:len(line) - 1]))
#print("Artist ID array has been created successfully with length %d!" % len(node))
#print("Pagerank score array has been created successfully with length %d!" % len(score))


# Search artist ID in origal artist_movies.txt file
count = 0
count1 = 0
number = 20
for line in filename2.readlines():
    tokens = line.split('\t\t')
    for i in range(number):
        artist_id = node[i]
        if artist_id == count:
            node[i] = tokens[0]
            count1 += 1
    count += 1
#print("Decode top %d artist ID in pagerank_score.txt file into name!" % count1)

# Store data into the .txt file
for i in range(number):
    s = "%s\t%s\n" % (node[i], str(score[i]))
    filename3.write(s)
filename1.close()
filename2.close()
filename3.close()

# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Decode pagerank_score.txt for the actor/actress network successfully!")
print("The first col in new dataset is the name for the artiest.")
print("The second col in new dataset is the pagerank score for the artiest")
print("--------------------------------------------------------------------")
print()
