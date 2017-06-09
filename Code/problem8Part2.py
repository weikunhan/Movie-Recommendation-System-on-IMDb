"""
 EE232E Project 2 Problem 8 Part 2
 Name: Weikun Han, Duzhi Chen
 Date: 6/4/2017
 Reference:
  - https://google.github.io/styleguide/pyguide.html
  - http://www.imdb.com
 Description:
  - Store the features for movies in order to train a regression model 
"""

from __future__ import print_function

# Print information
print(__doc__)
print()


movie={}
movie_file=open('movie_feature.txt','w')

i = 0
with open("/home/weikun/Documents/project_2_data/artist_movies.txt") as f:
    for line in f:
        print i
        act_movies=line.strip().split('\t\t')[1:]
        for movies in act_movies:
            mov=movies.strip()
            if mov=='':
                continue
            if mov in movie:
                movie[mov].append(i)
            else: movie[mov]=[i]
        i=i+1
print len(movie.keys())

movie_2 = {}
dir_2 = {}

i=0
with open("/home/weikun/Documents/project_2_data/director_movies.txt") as f:
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

top100 = []
i=0
with open("/home/weikun/Documents/project_2_data/director_top100.txt") as f:
    for line in f:
        print i
        top100.append(line.split("  ")[3])
        i=i+1


actor_rank=[]
with open("/home/weikun/Documents/project_2_data/pagerank_name.txt") as f:
    for line in f:
        actor_rank.append([float(line)])

movie_rating={}
with open("/home/weikun/Documents/project_2_data/movie_rating.txt") as f:
    for line in f:
        print i
        mv = line.split("\t")[0]
        rating = line.split("\t")[2]
        if mv in movie_rating.keys():
            movie_rating[mv].append(rating)
        else:
            movie_rating[mv] = [rating]
        i=i+1


i=0
j=0
for k in movie_rating.keys():
    print i
    if k in movie.keys():
    if len(movie[k])>=5:
        if k in movie_2.keys():
            actorID=movie[k]
			pgRank = []
			for ind in actorID:
				pgRank.append(actor_rank[ind])
			pgRank.sort(reverse=True)
		
			movie_dir = movie_2[k]
			dir_movie = dir_2[movie_dir[0]]
			top_features = [0]*101
			flag = 0
	
			for m in dir_movie:
				if m+"\n" in movie100:
					top_features[movie100.index(m)] = 1
					flag=1
			if flag==0:
				top_features[100]=1
	
			for f in range(0,5):
                                movie_file.write("%f\t" %pgRank[f][0])
				count += 1
			for f in range(0,101):
                                movie_file.write("%d\t" %top_features[f])

                    
                        movie_file.write("%s\n" %movie_rating[k][0])
			count2 += 1
			j=j+1
    i=i+1

movie_file.close()



# Print information
print("-------------------------Processing Finshed 1----------------------")
print("Construct features to train a regression model successfully!")
print("The total number of pageranks of the actors store is: %d" % count)
print("The total number of director for top 100 movies is: %d" % count2)
print("--------------------------------------------------------------------")
print()
