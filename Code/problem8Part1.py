"""
 EE232E Project 2 Problem 8 Part 1
 Name: Weikun Han, Duzhi Chen
 Date: 6/4/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Find the top 100 directors base on the top 100 movies rating 
"""

from __future__ import print_function

# Print information
print(__doc__)
print()

count = 0
count2 = 0


# Target file we want to create
filename3 = open("./project_2_data/director_top100.txt", "w")

i=0
with open("./project_2_data/director_movies.txt") as f:
    for line in f:
        print i
        movies=line.strip().split('\t\t')[1:]
        for mov in movies:
            mov=movies.strip()
            if mov=='':
                continue
            if mov in movie_2:
                movie_2[mov].append(i)
            else: movie_2[mov]=[i]
            if i in dir_2:
                dir_2[i].append(mov)
            else: dir_2[i] = [mov]
        i=i+1
        count += 1
        

movie_rating={}
with open("./project_2_data/movie_rating.txt") as f:
    for line in f:
        print i
        mv = line.split("\t")[0]
        rating = line.split("\t")[2]
        if mv in movie_rating.keys():
            movie_rating[mv].append(rating)
        else:
            movie_rating[mv] = [rating]
        i=i+1
        count2 += 1



# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Construct the data set for top 100 director successfully!")
print("The total number of rating scaned in movie_rating.txt is: %d" % count)
print("The total number of director scaned in director_movies.txt is: %d" % count2)
print("--------------------------------------------------------------------")
print()
