# Python Topological Sort
Simple Topological Sorting Algorithm, implemented in Python. 

I completed a coding challenge where you are given a list of strings that are written in a fictional language. You can assume the strings in the array are ordered in alphabetical order. The challenge is to then be able to return a string that represents the order of the alphabet of this fictional language. 

My solution was to first process the words into a programmatic representation of a Directed Acyclic Graph. To accomplish this, I chose to use a dictionary, with each key representing a letter of the alphabet, and the associated value being a list of characters that we know definitely the key comes BEFORE in the alphabet. 
