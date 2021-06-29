
'''A program to create a function called most_frequent that takes
 a string and prints the letters in decreasing order of frequency.''' 

s = input('Enter a string: ')

def most_frequent(string):
    dict = {}
    for key in string:
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1
    return dict

print(most_frequent(s))
