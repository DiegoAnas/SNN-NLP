

# Self Normalizing Neural Networks for Natural Language Processing

## Introduction
Self-Normalizing Neural Networks (SNNs) were introduced by [Klambauer et al.](https://arxiv.org/abs/1706.02515), to enable high-level abstract representations in Feed-forward neural networks (FNNs).  This type of networks use a novel activation function called "scaled exponential units" (SELUs), which induce self-normalizing properties.  Consequently, SNNs do not face vanishing and exploding gradient problems. This allows SNNs to train deep networks with many layers, employ strong regularization, and to make learning highly robust. 



## Related works

In their publication, [Eger et al.](https://arxiv.org/abs/1901.02671), conduct a compar ison of activation functions across several different NLP tasks (and task types) and using different neural network types: MLP, CNN, RNN and LSTM networks.

[Madasu et al.](https://arxiv.org/abs/1905.01338), also study the effectiveness of SNNs for different text classification tasks. They test two CNNs architectures, Self-normalizing Convolutional Neural Networks (SCNN) with ELU as activation function, and SCNN with SELU as activation function.

## Goal
The goal of this project is to test SELU activation function in different architectures and apply it to different sentiment analysis tasks. If time allows it, other activation functions such as swish can be tested.

### Sentiment Analysis 
Sentiment analysis is the task of classifying the polarity of a given text. For this task there are several data sets available to which state of the art algorithms have been applied and to which we can compare the results obtained:
 - [IMDB Movie Reviews Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
 - [Stanford Sentiment Treebank](https://nlp.stanford.edu/sentiment/index.html)
 - [Subjectivity dataset](http://www.cs.cornell.edu/people/pabo/movie-review-data/)

Additionally:
- [Amazon Reviews Dataset](https://drive.google.com/file/d/0Bz8a_Dbh9QhbaW12WVVZS2drcnM/view?usp=sharing)
- [Yelp Reviews Dataset](https://drive.google.com/open?id=0Bz8a_Dbh9QhbNUpYQ2N3SGlFaDg)

## Estimated Timeline
 1. Network design: 25h
 2. Network training and tuning: 15h
 3. Implementation: 8h
 4. Report writing: 4h

# Second Delivery Update

## Neural Networks for Sentiment Analysis
We have researched, built and tested several architectures:
- Convolutional Neural Network
	- We tested simple and multi branch convolutional neural networks. 
	- Implemented and tested the Very Deep Convolutional Network model from [VDCNN, EACL2017](http://www.aclweb.org/anthology/E17-1104)
	- Implemented and tested the  Deep Pyramid Convolutional Network model from [DPCNN, ACL2017](https://ai.tencent.com/ailab/media/publications/ACL3-Brady.pdf)
- Recurrent Neural Networks: we designed and tested LSTM networks, both simple and bidirectional. 
- Hybrid Neural networks: we designed different networks that use LSTM and Convolutional layers. 

All these models are built and implemented using Tensorflow 2 on Google Collab and the links to those files on Google Drive can be found in their respective Python Notebooks. Notebooks show the results obtained in these preliminary experiments.
### Results
Models were evaluated on the IMDB reviews dataset for Sentiment Classification, using a 5-CV method. 

The loss metric used is ***Binary Cross-Entropy***, although for the IMDB dataset the site [NLP Progress](http://nlpprogress.com/english/sentiment_analysis.html) only reports the accuracy those publications obtained.

**Our goal** is to achieve at least a **91.8 accuracy**, as high as the lowest paper reported in that page. Our highest accuracy is **90.4** (validation set accuracy), unexpectedly obtained by one of the simplest models, the ***simple CNN*** model.

Preliminary results show that SELU activation actually worsens the quality of the models, and this negative effect is increased on deeper networks (such as DPCNN or VDCNN).
In order to expand the results obtained we plan to run tests on both Amazon reviews and Yelp reviews dataset.

