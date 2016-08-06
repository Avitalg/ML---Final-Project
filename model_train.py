
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
book_path = "peter_pan.txt"
r_text = open(book_path).read()
r_text = r_text.lower()
chars = sorted(list(set(r_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
num_chars = len(r_text)
num_vocab = len(chars)
print "Total Characters: ", num_chars
print "Total Vocab: ", num_vocab
seq_length = 100
dataX = []
dataY = []
for i in range(0, num_chars - seq_length, 1):
	seq_in = r_text[i:i + seq_length]
	seq_out = r_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print "Total Patterns: ", n_patterns
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(num_vocab)
y = np_utils.to_categorical(dataY)
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
network_weights="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(network_weights, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(X, y, nb_epoch=20, batch_size=128, callbacks=callbacks_list)
