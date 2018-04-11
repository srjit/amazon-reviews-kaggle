

# amazon-reviews-kaggle

* LSTM model for sentiment analysis on kaggle's [Amazon Review](https://www.kaggle.com/bittlingmayer/amazonreviews/) dataset.

## Scripts

1. amazon-review.py - Training the model, and saving the model after 10k iterations

2. test_model.py - Testing the model for a mini batch of 2k reviews

## Vectorization 

* [Google's Word2Vec](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) has been used for the embedding layer and is interfaced through gensim (as usual).

## Notes

* The vocabulary, word encodings and word vectors will be saved in the ~/.kaggle/datasets/bittlingmayer/amazonreviews/resources folder during first run.



