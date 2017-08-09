# HanziCNN 汉字网
A simple convolutional neural network which takes 100x100 black and white images of Chinese characters as inputs and then outputs their pronunciation.

There are over 10,000 commonly-used chinese characters, each made up of certain reusable elements. However, even a fluent Chinese speaker would struggle to decipher the pronunciation of a character they had never seen before. This project aims to train a computer to see in these symbols what a human cannot. It is also a first attempt at putting into practice the machine learning theory I have been studying over the last 6 months and was inspired by my study of the Chinese language over that same period.

There are in fact three seperate networks: one to determine the initials (leading consonants), one to determine the finals (trailing letters), and one more to determine the tone. This is partly because this is a natural way to break down all Chinese syllables but also because this allows insights into how information about each part of the syllable is encapsulated in the characters.

Work in progress...
