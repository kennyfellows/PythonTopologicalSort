# Python Topological Sort
Simple Topological Sorting Algorithm, implemented in Python. 

I completed a coding challenge where you are given a list of strings that are written in a fictional language. You can assume the strings in the array are ordered in alphabetical order. The challenge is to then be able to return a string that represents the order of the alphabet of this fictional language. 

My solution was to first process the words into a programmatic representation of a Directed Acyclic Graph. To accomplish this, I chose to use a dictionary, with each key representing a letter of the alphabet, and the associated value being a list of characters that we know definitely the key comes BEFORE in the alphabet. 

We can then process this dictionary, by visiting each key, and traversing each of its "children" (each character in its array), until we reach a node that does NOT have any children. When we reach a node that does not have children, we can add that key to our string, and then continue to process other nodes, each time prepending the children-less nodes to our output string. 
