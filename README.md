# Image to Caption Generator
This Artificial Neural Network (ANN) can generate a text description for a given image :0

## Model
The model uses an encoder-decoder architecture:
  - ### Encoder
    The encoder extracts the image information as a high-dimensional vector (image embedding) by using the pre-trained "Xception" convolutional neural network (CNN).
  - ### Decoder
    The image embedding is used as the hidden state for a type of recurrent neural network (RNN) called gated recurrent unit (GRU), then for every time step the GRU model uses the hidden state and the previous token prediction (words in this case) to predict the next word. This is done until the model decides to end the description. The model knows when to end the description based on its training.

The model used for the decoder was trained Google Colab's free tier which limited the amount of time and compute power used.

## Dataset
The dataset used to train the decoder model was the Flicker 8k dataset.

## Model Workflow
  1. ## Feature Extraction
      The input image is loaded and resized to 299x299. It is then preprocessed and passed through the pre-trained Xception model to extract the image embedding, which serve as the foundation for generating the image description.
    
   2. ## Inference
      Using the extracted image features and the loaded tokenizer, the model predicts the next word in the caption. Starting with an empty string, the model appends one word at a time to build a complete description until it reaches the maximum length or encounters an end token.

## How to use

  1. Clone this repository:
     ```bash
     git clone https://github.com/juanmartin8a/Image2Caption-Generator.git
     cd Image2Caption-Generator

  2. Make sure to add the weights to the "weights" directory. To add the weights:
     
      1. Download the [model.h5](https://drive.google.com/file/d/1JTPG_yqsB4ToMlAH11jlUaUjPxUhV4Ri/view?usp=sharing) file as this is the file that contains the weights.
     
      2. Add the file to the "weights" directory :)

  3. Run the program: `python test.py`.
