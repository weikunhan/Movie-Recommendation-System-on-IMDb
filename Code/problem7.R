# EE232E Project 2 Problem 7
# Name: Weikun Han, Duzhi Chen
# Date: 6/3/2017
# Reference:
#  - https://google.github.io/styleguide/Rguide.xml#indentation
#  - http://www.imdb.com
#  Description:
#  - Predict the ratings of movies using the movie network

library("hydroGOF")
library("igraph")

# Setup the file path to load data
file_path1 <- "/home/weikun/Documents/project_2_data/graph_movie3.txt"
file_path2 <- "/home/weikun/Documents/project_2_data/movie_genre.txt"
file_path3 <- "/home/weikun/Documents/project_2_data/movie_rating.txt"

# Load the graph from the path
graph <- read.graph(file_path1, format = "ncol", directed = FALSE)

# Get movie name
file1 <- file(file_path2, open = "r")
line1 <- readLines(file1)

# Get movie rating
file2 <- file(file_path3, open = "r")
line2 <- readLines(file2)

# Initial veriables
count <- 0
movie_rating <- rep(0, vcount(graph))
movie_name <- rep("null", vcount(graph))
real_rating <- c(6.7, 7.4, 6.4)

# Add attribute name to the graph
for (i in 1:length(line1)) {
    if (count %in% V(graph)$name) {
        token <- strsplit(line1[i], "\t\t")
        index <- which(V(graph)$name == count)
        movie_name[index] <- token[[1]][1]
        cat(line1[count + 1], index, token[[1]][1],"\n")
    }
    count <- count + 1
}
close(file1)
V(graph)$movie_name <- movie_name

# Print information
cat("--------------------------Processing Finshed 1 --------------------------------\n",
    "Add movie name attribute for graph in the movie network successfully.\n",
    "The total number of movies scaned in movie_genre.txt is: ", count, "\n",
    "The total number of vertices in graph added the movie name is:", length(movie_name), "\n",
    "--------------------------------------------------------------------------------\n")

# Add attribute rating to the graph
for (i in 1:length(line2)) {
    token <- strsplit(line2[i], "\t\t")
    index <- which(V(graph)$movie_name == token[[1]][1])
    if (identical(index, integer(0))) {
        cat("\n")
    } else {
        movie_rating[index] <- token[[1]][2] 
        cat(line2[i], index, token[[1]][2],"\n")
    }
}
close(file2)
V(graph)$movie_rating <- movie_rating

# Print information
cat("--------------------------Processing Finshed 2 --------------------------------\n",
    "Add movie rating attribute for graph in the movie network successfully.\n",
    "The total number of movies scaned in movie_rating.txt is: ", count1, "\n",
    "The total number of vertices in graph added the movie name is:", unique(movie_rating), "\n",
    "--------------------------------------------------------------------------------\n")

# Predict the rating for the movies
ind=1
i=1
while(i < 10){
  if(!is.null(map[[v_name[movie1[i]]]])){
    movie1_rating<-c(movie1_rating,map[[v_name[movie1[i]]]])
    ID = get.edge.ids(g,c(V(g)[movieID],V(g)[movie1[i]]))
    neighbour_rating=c(neighbour_rating,as.double(movie1_rating[ind]))
    neighbour_wt=c(neighbour_wt,edgeWeight[ID])
    temp1=temp1+(as.double(movie1_rating[ind])*edgeWeight[ID])
    temp2=temp2+edgeWeight[ID]
    ind=ind+1
    predict_rating <- c(predict_rating, ind)
  }
  i=i+1
}



# Print information
cat("--------------------------Processing Finshed 3 --------------------------------\n",
    "Successful predict rating for Batman vs Superman: Dawn of Justice (2015).\n",
    "The predict rating for this movie is:", predict_rating[1], "\n",
    "The real rating for this movie is:", real_rating[1],"\n",
    "-------------------------------------------------------------------------------\n")

# Print information
cat("--------------------------Processing Finshed 4 --------------------------------\n",
    "Successful predict rating for Mission Impossible – Rogue Nation (2015).\n",
    "The predict rating for this movie is:", predict_rating[2], "\n",
    "The real rating for this movie is:", real_rating[2],"\n",
    "-------------------------------------------------------------------------------\n")

# Print information
cat("--------------------------Processing Finshed 5 --------------------------------\n",
    "Successful predict rating for Minions (2015).\n",
    "The predict rating for this movie is:", predict_rating[3], "\n",
    "The real rating for this movie is:", real_rating[3],"\n",
    "-------------------------------------------------------------------------------\n")

RMSE <- rmse(predict_rating, real_rating)
MSE <- mse(predict_rating, real_rating)

# Print information
cat("--------------------------Processing Finshed 6 --------------------------------\n",
    "Successful use two ways to evaluate the errors for prediction.\n",
    "The Root Mean Square Error is:", RMSE, "\n",
    "The Mean Squared Error is:", MSE,"\n",
    "-------------------------------------------------------------------------------\n")
