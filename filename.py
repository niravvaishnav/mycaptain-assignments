
# A program to accept a file name from the user and print the extension of that.
 
fn = input('Enter Filename: ')
f = fn.split('.')
print ("Extension of the file is : " + f[-1])
