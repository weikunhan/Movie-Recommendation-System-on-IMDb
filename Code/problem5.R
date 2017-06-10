# EE232E Project 2 Problem 5
# Name: Weikun Han, Duzhi Chen
# Date: 5/28/2017
# Reference:
#  - https://google.github.io/styleguide/Rguide.xml#indentation
#  - http://www.imdb.com
#  Description:
#  - Find community on the movie network and tag each community 
#    with the genres that appear in 20% or more of the movies

library("igraph")

# Setup the file path to load data
file_path1 <- "/home/weikun/Documents/project_2_data/graph_movie3.txt"
file_path2 <- "/home/weikun/Documents/project_2_data/movie_genre.txt"

# Load the graph from the path
graph <- read.graph(file_path1, format = "ncol", directed = FALSE)

# Get movie genres
file <- file(file_path2, open = "r")

# Initial veriables
community_size <- numeric(0)
community_tag <- numeric(0)
count <- 0

# Use fast greedy method to find the community structure
fc <- fastgreedy.community(graph)

# Find all size for each unique community
for (i in 1:length(fc)) {
    community_size= c(community_size, size(fc)[i])
}

# Print information
print(sizes(fc))
cat("-------------------------Processing Finshed 1-----------------------------------\n",
    "Fast greedy method to find the community structure done.\n",
    "The length of the community structure is: ", length(fc), "\n",
    "The modularity of the community structure is: ", modularity(fc), "\n",
    "--------------------------------------------------------------------------------\n")

# Plot information
barplot(community_size,
        main = "Histogram for community", 
        ylab = "Community sizes",
        col= "blue",
        names.arg = 1:length(community_size))

# Get all lines information
line = readline(file)

Genre = rep("null",vcount(graph))


# Add attribute genre to the graph
for (i in 1:length(line)){
  if(count %in% V(graph)$name){
    list = strsplit(line[i],"\t\t")
    index = which(V(graph)$name == count)
    Genre[index] = list[[1]][2]
    cat(line[count+1],index,list[[1]][2],"\n")
  }
  count = count + 1
}
close(file)
V(graph)$genre = Genre

# Print information
cat("-------------------------Processing Finshed 2-----------------------------------\n",
    "Add movie genre attribute for graph in the movie network successfully.\n",
    "The total number of movies scaned in movie_genre.txt is: ", count, "\n",
    "The total number of vertices in graph added the movie genre is:", vcount(graph), "\n",
    "--------------------------------------------------------------------------------\n")

com_tag = numeric(0)
for (i in 1:length(g_movie_com)){
  com_genre = V(g_movie)[which(g_movie_com$membership ==i)]$genre
  max = 0
  max_index = "null"
  genre_type = unique(com_genre)
  for(genre in genre_type)
  {
    if(length(which(com_genre == genre))>max && length(which(com_genre == genre))>length(com_genre)*0.2 && genre!="null")
    {
      max = length(com_genre[which(com_genre == genre)])
      max_index = genre
    }
  }
  cat(i,"\t",max_index,"\n")
  com_tag = c(com_tag,max_index)
  
}

# Print information
cat("-------------------------Processing Finshed 3-----------------------------------\n",
    "Tag the community with genre that appear more than 20% in the community successfully.\n",
    "The total number of movie genres is: ", unique(V(graph)$genre), "\n",
    "The total number of comunities have been tag is:", length(com_tag), "\n",
    "--------------------------------------------------------------------------------\n")

a <- data.frame(id, community_tag)
colnames(a) <- c("Community ID", "Community Tag")
write.csv(a, file = "/Users/weikun/Documents/project_2_data/community_genre.csv",row.names = FALSE)

# Print information
cat("--------------------------Processing Finshed 4 --------------------------------\n",
    "Successful store community tag result into .csv file.\n",
    "The file store at /home/weikun/Documents/project_2_data/community_tag.csv\n",
    "-------------------------------------------------------------------------------\n")

