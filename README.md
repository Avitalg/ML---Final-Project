# ML-Final-Project

##Collaborators
This project presented to you by Avital Glazer (@avitalg) and Nir Shchori (@Shchori).

##Description
Our project contains code in python who analysis the data from data that was given to us by using deep learning and algorithm RNN.
In this project we used Keras package and theano as backend.

We took the 'Peter Pan' book and analyze it, in order to find the next sentence in the book. 
The book is saved in the file "peter_pan.txt".

The main issue in working with this kind of data is to transfer text to data that the computer could work with and get a reliable result.

##Importance 
We found this research interesting because it was challenging to use this data and to see how the algorithm learning it and produce a new data according to the old one. This algorithm, if implemented correctly, could help producing more stories and change the face of literature in the world.

##Preparations
To be able to discover what would be the next sentence, the algorithm need to "understand" the story, in such way that will allow it to create data that make sence. 

To make this story to a data the algorithm cloud work with, we needed to tranfer the data to workalble data.
At first, we change all chars to lower case char. Then we created mapping of unique chars to integers.

```
book_path = "peter_pan.txt"
r_text = open(book_path).read()
r_text = r_text.lower()
chars = sorted(list(set(r_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
```
We needed to split the data set to training data for the network

```
seq_length = 100
dataX = []
dataY = []
for i in range(0, num_chars - seq_length, 1):
	seq_in = r_text[i:i + seq_length]
	seq_out = r_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
```
and define the RNN model 
```
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
```

##Code Description

Train the model and save the network weights, load the last checkpoint and fit it to the model
```
network_weights="weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(network_weights, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
model.fit(X, y, nb_epoch=20, batch_size=128, callbacks=callbacks_list)
```

Generate the new sentence 
```
for i in range(1000):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	x = x / float(num_vocab)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = int_into_char[index]
	seq_in = [int_into_char[value] for value in pattern]
	sys.stdout.write(result)
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
```

##Result
`iar about it, but by and by he remembered that it had not been ticking. at first he thought this eer`
`e ale the boys wfre she lad boen to the boos of the boos, and they were al anr oo the bark of the bark`
`of the boos of the boos afd the nererland thet thet whre hev back on the barkn of the bors. and `
`they were al anr oo the bark of the bark of the boos of the boos of the boos of the boos`
`afd the nererland thet thet whre hev back on the barkn of the bors.`
`and they were al anr oo the bark of the bark of the boos of the boos of the boos of the boos afd the nererland thet`
`thet whre hev back on the barkn of the bors. and they were al anr oo the bark of the bark of`
`the boos of the boos of the boos of the boos afd the nererland thet thet whre hev back on the`
`barkn of the bors. and they were al anr oo the bark of the bark of the boos of the boos of the boos of the`
`boos afd the nererland thet thet whre hev back on the barkn of the bors. and they were al anr oo the bark of the bark`
`of the boos of the boos of the boos of the boos afd the nererland thet thet whre hev back on the barkn of the bors.`


minhash result:
[0.22580645161290322, 0.26666666666666666, 0.20833333333333334, 0.22727272727272727, 0.17391304347826086, 0.24, 0.23076923076923078, 0.18181818181818182, 0.25, 0.20689655172413793, 0.16666666666666666]
