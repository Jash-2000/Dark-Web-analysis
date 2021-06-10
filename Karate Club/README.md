# ZACHARY’S KARATE CLUB

Zachary’s Karate Club is a well-known dataset that describes the relationships in a university karate club, used by Wayne W. Zachary in his paper “An Information Flow Model for 
Conflict and Fission in Small Groups.” This dataset is famous for its clear depiction of community structure, which occurs when nodes of a network can be grouped into densely 
connected sets. In the case of Zachary’s Karate Club, the network can be split into two groups centered around Mr. Hi, the karate teacher, and John A, the club president, and the 
network accurately predicts how the karate club splits into two new clubs after an argument regarding pay causes a divide between Hr. Hi and John A. By recording the meetings of 
group members outside the context of the club itself, the network shows which club members will join which new club in 33 of 34 cases.

  * The data points represent people enrolled in the Karate club. 
  * Nodes 1 and 34 represent the Sensei and Owner respectively. 
  * The motivation for the analysis was the fact that they wanted to separate and hence, had to analysis as to how many students would join whom.
  * The 3 - step algorithm is to make the graph embeddings ( preparation step ) and then make clusters ( analysis step ) and then plotting them ( visualization step ).

The visualization graph for the entire network was as follows ( Source : [Wikipedia](https://en.wikipedia.org/wiki/Zachary%27s_karate_club) ):

![Original Network](https://user-images.githubusercontent.com/47540320/121556630-ae374c80-ca31-11eb-8de2-944929308d95.png)

For conversion of nodes to embeddings, I used the master script of Node2Vec present in the source path. My goal was to use unsupervised learning to cluster the Nodes that would be close to Node 1 and Node 34. Used method was **Node2vec** that converted the nodes into a 128 
dimmension embedding vector. This was later clusterred into 2 clusters using K-means clusterring. The final distribution looked as follows:

![Distributed Network](https://user-images.githubusercontent.com/47540320/121558008-e55a2d80-ca32-11eb-96fd-5ac9f235e06a.png)
