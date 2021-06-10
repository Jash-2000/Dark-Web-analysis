# Source Scripts for the project

  * The files present here include the source code for Node2vec script that hase been used everywhere in the project.
 
  * Other than that a file, Gateway.ipynb is present which predicts the network's gateway points and hence, will help in finding the main dealer of the network. 
  
  ![unnamed](https://user-images.githubusercontent.com/47540320/121583250-a7b6ce00-ca4d-11eb-8114-b036c262bbeb.png)

  * A folder named Drug_Analysis was a practice project using naive NLP algorithms used to analyses and visualizes the drug network from a data dump from Dark Web.

  * Link Prediction folder contains scripts that implemented the Supervised Link Prediction using ANN i.e. the prediction of existance of link between 2 nodes in a network. A similar algorithm called Graph Sage was also tried.
  
  ![Graph Sage](https://user-images.githubusercontent.com/47540320/121584380-0761a900-ca4f-11eb-935c-19a75c5b7517.png)

  * Additioanlly, a tensorboard based visualization tool was used for easing the task - [https://projector.tensorflow.org/](https://projector.tensorflow.org/). 
  
  Steps: For visualisation, we will be required to upload a file of  Tensorflow(TSV) vectors & metadata file for our labels.
  To generate these files from the embeddings directly obtained after running node2vec, the most efficient approach will be to use the following   script in our command line. It will produce both as output,the metadata & the TSV vectors file.
  ```cmd
    python -m gensim.scripts.word2vec2tensor -i emb\karate.emb -o model_file
  ```
