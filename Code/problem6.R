# EE232E Project 2 Problem 6
# Name: Weikun Han, Duzhi Chen
# Date: 5/30/2017
# Reference:
#  - https://google.github.io/styleguide/Rguide.xml#indentation
#  - http://www.imdb.com
#  Description:
#  - Add the nodes into the movie network and find each node top 5
#    nearest neighbors

library("igraph")

# Setup the file path to load data
file_path1 <- "/home/weikun/Documents/project_2_data/graph_movie3.txt"
file_path2 <- "/home/weikun/Documents/project_2_data/movie_genre.txt"

# Load the graph from the path
graph <- read.graph(file_path1, format = "ncol", directed = FALSE)


target<-c("Batman v Superman: Dawn of Justice (2016)",
          "Mission: Impossible - Rogue Nation (2015)",
          "Minions (2015)")
filename="/Users/Ke/Desktop/Eclipse/232/fastgreedy/mem_name.txt"
f=file(filename,open='r')
name_list=readLines(f)
close(f)
V(g)$movieName<-name_list
nb<-list()
community_id<-rep(0,3)
for(i in 1:3){
  nodeID<-(1:vcount(g))[V(g)$movieName==target[i]]
  temp<-neighborhood(g,1,V(g)[nodeID])
  nb[[i]]<-temp[[1]][2:length(temp[[1]])]
  print(target[i])
  community_id[i]<-ans$membership[nodeID]
  print("It belongs to the community")
  print(community_id[i])
}
write.table(nb[[1]],file='nb1.txt',row.names=FALSE,col.names=FALSE)


a <- data.frame(id, movie_name, community_id)
colnames(a) <- c("Node ID", "Movie Name", "Community ID")

write.csv(a, file = "/home/weikun/Documents/project_2_data/node1_neighbour.csv",row.names = FALSE)

# Print information
cat("--------------------------Processing Finshed 1 --------------------------------\n",
    "Successful store top 5 nearest neighbours of Batman v Superman: Dawn of Justice (2016) into .csv file.\n",
    "The file store at /home/weikun/Documents/project_2_data/node1_neighbour.csv\n",
    "-------------------------------------------------------------------------------\n")
a <- data.frame(id, movie_name, community_id)
colnames(a) <- c("Node ID", "Movie Name", "Community ID")
write.csv(a, file = "/home/weikun/Documents/project_2_data/node2_neighbour.csv",row.names = FALSE)

# Print information
cat("--------------------------Processing Finshed 2 --------------------------------\n",
    "Successful store top 5 nearest neighbours of Mission: Impossible - Rogue Nation (2015) into .csv file.\n",
    "The file store at /home/weikun/Documents/project_2_data/node2_neighbour.csv\n",
    "-------------------------------------------------------------------------------\n")

a <- data.frame(id, movie_name, community_id)
colnames(a) <- c("Node ID", "Movie Name", "Community ID")
write.csv(a, file = "/home/weikun/Documents/project_2_data/node3_neighbour.csv",row.names = FALSE)

# Print information
cat("--------------------------Processing Finshed 3 --------------------------------\n",
    "Successful store top 5 nearest neighbours of Minions (2015) into .csv file.\n",
    "The file store at /home/weikun/Documents/project_2_data/node3_neighbour.csv\n",
    "-------------------------------------------------------------------------------\n")

