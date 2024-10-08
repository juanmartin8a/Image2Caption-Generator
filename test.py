from pickle import load
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception, preprocess_input
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import Model
from keras.models import load_model

def extract_features(filename):
	model = Xception()
	model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
	image = load_img(filename, target_size=(299, 299))
	image = img_to_array(image)
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	image = preprocess_input(image)
	feature = model.predict(image, verbose=0)
	return feature

def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

def generate_desc(model, tokenizer, photo, max_length):
	in_text = ''
	for _ in range(max_length):
		sequence = tokenizer.texts_to_sequences([in_text])[0]
		sequence = pad_sequences([sequence], maxlen=max_length)
		yhat = model.predict([photo,sequence], verbose=0)
		yhat = argmax(yhat)
		word = word_for_id(yhat, tokenizer)
		if word is None:
			break
		if word == 'end':
			break
		if in_text == '':
			in_text = word
		else:
			in_text += ' ' + word

	return in_text

tokenizer = load(open('tokenizer.pkl', 'rb'))
max_length = 37
model = load_model('weigths/model.h5')
path_to_picture = input('Path to picture: ')
photo = extract_features(path_to_picture)
description = generate_desc(model, tokenizer, photo, max_length)
print(description)
