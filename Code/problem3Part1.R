# EE232E Project 2 Problem 3 Part 1
# Name: Weikun Han, Duzhi Chen
# Date: 5/25/2017
# Reference:
#  - https://google.github.io/styleguide/Rguide.xml#indentation
#  - http://www.imdb.com
#  Description:
#  - Run pagerank algorithm on the actor/actress network

library("igraph")

# Setup the file path to load data
file_path <- read.table("~/Documents/project_2_data/artist_graph.txt")

# Load the graph from the path
graph <- graph.data.frame(file_path, directed = TRUE)

# Run pagerank algorithm
pr <- page.rank(graph)
sorted_pr <- sort(pr$vector, decreasing = TRUE, index.return = TRUE)

# Store data into .txt file
write.table(sorted_pr[[1]], file="~/Documents/project_2_data/pagerank_score.txt", col.names = FALSE)

# Print information
cat("-------------------------Processing Finshed 1----------------------------------\n",
    "Run pagerank algorithm on the actor/actress network successfully!\n",
    "The first col in the dataset is the ID for the artiest\n",
    "The second col in the dataset is the pagerank score for the artiest\n",
    "-------------------------------------------------------------------------------\n")
