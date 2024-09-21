# Image to Caption Generator
This Artificial Neural Network (ANN) can generate a text description for a given image :o

The model works with an encoder and decoder:
  - ## Encoder
    The encoder extracts the image information as a high-dimensional vector (image embedding) by using the "Xception" convolutional neural network (CNN).
  - ## Decoder
    The image embedding is used as the hidden state for a type of recurrent neural network (RNN) called gated recurrent unit (GRU), then for every time step the GRU model uses the hidden state and the previous token prediction (words in this case) to predict the next word. This is done until the model decides to end the description.The model knows when to end the description based on its training.

The self-made model used for the decoder was trained in the GPUs of Google Colab's free tier. The dataset used to train the decoder model was the Flickr 8k dataset.

## Disclaimer
Sadly it appears that I deleted the weights of the model and the "test.py" file (Script where you can play with the model) won't work without them. However, you can get your own weights by training the model yourself by using the jupiter notebook in this repository.
