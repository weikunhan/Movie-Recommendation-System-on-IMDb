library("igraph")
filePath = "Desktop/graphAct2.txt"
g_actor = read.graph(file = filePath ,format = "ncol",directed = T)
print("done")
pageRank = page.rank(g_actor, directed = T, damping = 0.85)
sorted_pageRank = sort(pageRank$vector,decreasing=T,index.return=T)
#top 10 pagerank # the vertex ID start from 0, so line x+1 in the text file should be the actor
#run processAct_top_10.py to get a file with top 10 actors
print(sorted_pageRank$ix[1:10])

##############################
#      problem 3            #
##############################
library("igraph")
edgelistFile<-read.table("/Users/Ke/Desktop/Eclipse/232/graph_act.txt")
g=graph.data.frame(edgelistFile, directed=T)
pg=page.rank(g)
ans=pg[[1]]
write.table(ans, file='page_rank.txt', col.names=FALSE)
