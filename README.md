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

## Estimated Timeline
 1. Network design: 25h
 2. Network training and tuning: 15h
 3. Implementation: 8h
 4. Report writing: 4h
