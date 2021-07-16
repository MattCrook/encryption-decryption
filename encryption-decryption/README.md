## Encryption / Decryption 
This is not a perfect encryption code that would make the data trasfer safe. However, I think it perfectly illustrates how encryption works. It is simple, understandable, and usable

WHAT IT DOES:

encryption.py: In order to run this you will need Python 3.0 and numpy installed. When you run this, it will ask for input/text. Once the user types an input and hits enter, the program looks through every letter and converts it to an index number in "alphabet" array. After that, it converts an array to a matrix, the dimentions of a matrix are NUMBER OF LETTERS/2 rows and 2 columns. Once we got a matrix, we multiply it by a key and we get a very complex matrix. Finally, we write what we got to "encryption_message.txt" file.

encryption_message.txt: this is where we keep our encrypted message

decryption.py: In order to run this you will need Python 3.0 and numpy installed. Once you run this, It will open "encryption_message.txt" file and reads the message. After that, it converts the message to an array, and afterwards converts an array to a matrix. Once we got the matrix, it multiplies the matrix by an inverse of a key. Finally, it looks at the index numbers of a matrix and converts it to a text and prints it.
