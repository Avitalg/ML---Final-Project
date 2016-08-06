# ML-Final-Project

##Collaborators
This project presented to you by Avital Glazer (@avitalg) and Nir Shchori (@Shchori).

##Description
Our project contains code in python who analysis the data from XXXX by using deep learning and algorithm RNN.
In this project we used Keras package and theano as backend.

We took the 'Peter Pan' book and analyze it, in order to find the next sentence in the book. 
The book is saved in the file "peter-pan_story.txt".

The main issue in working with this kind of data is to transfer text to data that the computer could work with and get a reliable result.
To be able to discover what would be the next sentence, the algorithm need to "understand" the story, in such way that will alow it to create data that make sence. 

To make this story to a data the algorithm cloud work with, we needed to tranfer the data to workalble data.
At first, we change all chars to lower case char. Then we created mapping of unique chars to integers.
