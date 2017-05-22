"""
 EE232E Project 2 Problem 1 Part 1
 Name: Weikun Han, Duzhi Chen
 Date: 5/21/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Prepare data sets
"""

from __future__ import print_function
import os
import json

# Print information
print(__doc__)
print()

# Determin which document you want to process
folder = "project_2_data"
dataset1 = "actor_movies.txt"
dataset2 = "actress_movies.txt"
dataset3 = "artist_movies.txt"
filename1 = os.path.join(folder, dataset1)
filename2 = os.path.join(folder, dataset2)
filename3 = os.path.join(folder, dataset2)

# Setup the split and count to determine number of movies we want process
split = "\t\t"
count = 0
count1 = 0
count2 = 0


# Open one file in the dataset under the folder
with open(filename1) as fp1:

    # Check each infomation in selected file in the dataset
    for line in fp1:

        # 2 tab in front of moive so make this as conditon
        if(line.count(split) >= 5):
            with open(filename3, "w") as file:
                file.write(str(line) + "\n")
                file.close()
                count1 += 1
                print("Line %d has %d movies" % (count1, line.count(split)))
    fp1.close()

# Open one file in the dataset under the folder
with open(filename2) as fp2:

    # Check each infomation in selected file in the dataset
    for line in fp2:

        # 2 tab in front of moive so make this as conditon
        if(line.count(split) >= 5):
            with open(filename3, "w") as file:
                file.write(str(line) + "\n")
                file.close()
                count2 += 1
                print("Line %d has %d movies" % (count2, line.count(split)))
    fp2.close()

# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Prepared the number actor with great or equal to 5 movies is: %d" % count1)
print("Prepared the number actresses with great or equal to 5 movies is: %d" % count2)
print("The total number of artiest with great or equal to 5 movies is: %d" % (count1 + count2))
print("--------------------------------------------------------------------")
print()
