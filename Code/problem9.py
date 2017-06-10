"""
 EE232E Project 2 Problem 9
 Name: Weikun Han, Duzhi Chen
 Date: 6/5/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
  - http://scikit-learn.org/stable/
 Description:
  - Construct a bipartite graph to predict movie rating
"""

from __future__ import print_function
from sklearn.metrics import mean_squared_error
import math

# Print information
print(__doc__)
print()

def clean_str(inp):
    inp1 = inp.replace("(voice)","")
    inp2 = inp1.replace("(VG)","")
    inp3 = inp2.replace("(uncredited)","")
    return inp3.rstrip()


y_true = [6.7, 7.4, 6.4]
new_movies = ["Minions (2015)",
              "Mission: Impossible - Rogue Nation (2015)",
              "Batman v Superman: Dawn of Justice (2016)"]
movie_actor = {}

for n in new_movies:
    movie_actor[n] = []

actor_movie = {}
for line in open("/home/weikun/Documents/project_2_data/artist_movies.txt"):
    actor = line.split("\t\t")[0]
    movies = line[:-1].split("\t\t")[1:]
    for m in new_movies:
        if m in line:
            movie_actor[m].append(actor)
            actor_movie[actor] = map(clean_str,movies)


movie_rating = {}
for line in open("/home/weikun/Documents/project_2_data/movie_rating.txt"):
    movie_rating[line.split("\t\t")[0]] = float(line[:-2].split("\t\t")[1])

actor_rating = {}
for k in actor_movie.keys():
    temp = 0
    number = 0
    for m in actor_movie[k]:
        if m in movie_rating.keys():
            temp += movie_rating[m]
            number += 1
    if number==0:
        actor_rating[k] = 0
    else:
        actor_rating[k] = temp/number

y_pred = []
for movie in movie_actor.keys():
    temp = 0
    number = 0
    for a in movie_actor[movie]:
        if actor_rating[a]!=0:
            temp += actor_rating[a]
            number += 1
    rating = temp/number
    y_pred.append(rating)
    
# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Construct a bipartite graph successfully!")
print("The predict rating of Batman vs Superman: Dawn of Justice (2016): %.1f" % y_pred[0])
print("The predict rating of Mission: Impossible - Rogue Nation (2015): %.1f" % y_pred[1])
print("The predict rating of Minions (2015): %.1f" % y_pred[2])
print("The Root Mean Square Error is: %f" % math.sqrt(mean_squared_error(y_true, y_pred)))
print("The Mean Squared Error is: %f" % mean_squared_error(y_true, y_pred))
print("--------------------------------------------------------------------")
