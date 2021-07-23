## Encryption / Decryption
This is not a perfect encryption code that would make the data transfer safe. However, it is an example that illustrates how encryption works.

### What it does:

#### `encryption.py`

In order to run this you will need Python 3.0 and numpy installed.

When you run this, it will ask for input/text. Once the user types an input and hits enter, the program looks through every letter and converts it to an index number in "alphabet" array.

After that, it converts an array to a matrix, the dimensions of the matrix are NUMBER OF LETTERS/2 rows and 2 columns.

Once we have a matrix, we multiply it by a key, and finally, we write the output to `encryption_message.txt` file.

#### `encryption_message.txt`

This is where we keep our encrypted message.

#### `decryption.py`

Running this file will open `encryption_message.txt` and reads the message.

After that, it converts the message to an array, and afterwards converts an array to a matrix.

Once we have the matrix, it multiplies the matrix by an inverse of the key, and finally, looks at the index numbers of the matrix and converts it to a text and prints it.
