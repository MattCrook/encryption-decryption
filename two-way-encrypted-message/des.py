import tables
'''
Looking into DES
Considering the Key
    1. The Key needs to be 8 bytes precisely,
    2. A parity drop is done to convert it into 56 bit Key
    3. There are 16 rounds, hence, 16 keys would be needed
    4. In each round, the key is broken into two halfs, a
    left circular left is done and then compressed to 48 bits
    5. The shift is done by 1 bit for rounds 1,2,9,16 and for
    others it is done by 2
'''

class DES_Algorithm():

    def __init__(self, text, key, encrypt=True):
        self.text = text
        self.key = key
        self.encrypt = encrypt
        self.roundKeys = []

    def string_to_bit_array(self, text):
        '''
        Convert a string into a list of bits. Note that the MSB "0"
        are omitted by default so they need to be appended.
        Also the other assumption is that the characters are of 8 bits,
        so we are following the ASCII represenatation.
        Input: A string of characters
        Output: A string of 0s and 1s
        '''
        res = []
        for letter in text:
            d = format(ord(letter), 'b')
            d = "0" * (8 - len(d)) + d
            res.append(d)
        return "".join(res)

    def bit_array_to_string(self, array):
        '''
        Recreate the string from the bit array. It is assumed that the
        characters are of 8 bits, so we are following the ASCII represenatation
        '''
        res = []
        for i in range(0, len(array), 8):
            res.append(chr(int(array[i:i + 8], 2)))
        return "".join(res)

    def permut(self, key, table):
        '''
        Here we are shuffling the input key as per the table
        provided in the argument
            1. Compressing and shuffling the input key from 64bits to 56bits
            2. Compressing and shuffling the shifted key from 56 bits to 48bits
            3. Expanding the text from 32 bits to 48 bits
        input: Key as a string of 0s and 1s and Table as a list of indexes
        Output: A string of 0s and 1s
        '''
        res = [0] * len(table)
        for index_in_result, index_in_key in enumerate(table):
            res[index_in_result] = key[index_in_key]

        return "".join(res)

    def xor(self, text, key):
        '''
        Here we are XORing the two arguments: The expanded text
        and the key.
        Input: A string of 0s and 1s as text and key
        Output: A string of 0s and 1s
        '''
        res = []
        for i, j in zip(text, key):
            if i == j:
                res.append("0")
            else:
                res.append("1")

        return "".join(res)

    def int_to_binary(self, number):
        '''
        Here we are converting thhe input number into a 4bit string
        '''
        string = str(bin(number).replace("0b", ""))
        return "0" * (4 - len(string)) + string

    def subsitution(self, key, table):
        '''
        Here we are compressing the key from 32 bits to 48 bits. The boxes are
        of the size 4*16 and each containing a 4bit data. So, the first and
        last bit of the 6bit blocks of the key are taken as row number and
        remainder as the column number.
        '''
        # Splitting the key into 8 blocks of 6bits
        blocks = []
        for i in range(0, len(key), 6):
            blocks.append(key[i:i + 6])

        # Making use of each box for a block sequentially
        res = []
        for index, block in enumerate(blocks):
            rowNumber = int(str(block[0]) + str(block[5]), 2)
            columnNumber = "".join(list(map(lambda x: str(x), block[1:5])))
            columnNumber = int(columnNumber, 2)
            res.append(self.int_to_binary(
                table[index][rowNumber][columnNumber]))

        return "".join(res)

    def keyGeneration(self):
        '''
        The input key is assumed to be character array.
        The points to be considered are:
                1. The Key needs to be 8 bytes precisely,
                2. A parity drop is done to convert it into 56 bit Key
                3. There are 16 rounds, hence, 16 keys would be needed
                4. In each round, the key is broken into two halfs, a
                left circular left is done and then compressed to 48 bits
                5. The shift is done by 1 bit for rounds 1,2,9,16 and for
                others it is done by 2
        '''
        # Checking for Key Length
        if len(self.key) < 8:
            print("The key should be of atleast 8 bytes/characters")
            exit(0)
        else:
            self.key = self.key[:8]

        # Setting the Shift Counts
        shift_count = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        # Converting the key to binary
        key = self.string_to_bit_array(self.key)

        # The parity drop to convert to 56 bits
        key = self.permut(key, tables.keyCompression64_56)

        # Breaking the key into halves
        keyLeft = key[:28]
        keyRight = key[28:]
        for count in shift_count:
            # Applying Left Circular Shift
            keyLeft = keyLeft[count:] + keyLeft[:count]
            keyRight = keyRight[count:] + keyRight[:count]
            self.roundKeys.append(self.permut(keyLeft + keyRight,
                                              tables.keyCompression56_48))

    def DES(self, viewSteps=False):
        '''
        The main algorithm is implemented here. The steps are:
            1. Generate Round Keys if not done yet
            2. Convert the string to binary
            3. Do the initial permutation
            4. Slice the text into two halves
            5. Expland the right half to 48 bits
            6. XOR this half with the round key
            7. Compress the result to 32 bits
            8. Shuffle the result to get the Feistel Cipher Key
            9. XOR the left half with this Feistel Cipher Key
            10. Swap the right and left halves
            11. After the 16 rounds, swap the halves once again
            12. Final Shuffling is done on this to get the result
            13. Convert the output to plaintext
        We do the above for every 64bit blocks of character string.
        In order to make this possible, trailing white space is added
        as padding to meet this condition
        '''
        if len(self.roundKeys) == 0:
            self.keyGeneration()

        if self.encrypt:
            keys = self.roundKeys
        else:
            keys = self.roundKeys[::-1]

        if viewSteps:
            print(f"Initial Text: {self.text}")
            print(f"Secret Key: {self.key}\n")

        text = self.text
        if len(text) % 8 != 0:
            text += " " * (8 - (len(text) % 8))

        result = []
        for i in range(0, len(text), 8):
            block = text[i:i + 8]
            block = self.string_to_bit_array(block)
            block = self.permut(block, tables.initialPermutation)

            for roundNumber in range(16):
                if viewSteps:
                    print(f"Round {roundNumber + 1}")
                    print(f"Plaintext: {hex(int(block, 2))}")
                    print(f"Key: {hex(int(keys[roundNumber]))}\n")

                # Breaking the text into two halfs
                blockLeft = block[:32]
                blockRight = block[32:]

                # Expanding the key from 32 bits to 48 bits
                expandedRight = self.permut(
                    blockRight, tables.textExpansion32_48)

                # Generating the key to be used according to
                # the Feistel Cipher logic
                key = self.xor(expandedRight, keys[roundNumber])

                # Compressing the key back to 32 bits to xor
                # with the left part
                key = self.subsitution(key, tables.subsitutionBox)

                # Shuffling the key before the XOR
                key = self.permut(key, tables.keyShuffle)

                # XORing the key of the Feistel Cipher
                blockLeft = self.xor(blockLeft, key)

                # Swapping the two halves for the next round
                blockLeft = "".join(blockLeft)
                blockLeft, blockRight = blockRight, blockLeft
                block = blockLeft + blockRight

            block = self.permut(block[32:] + block[:32],
                                tables.finalPermutation)

            if viewSteps:
                print(f"\nFinal Block Text for Round {roundNumber + 1}: {repr(self.bit_array_to_string(block))}\n")

            result.append(self.bit_array_to_string(block))

        result = "".join(result)

        if viewSteps:
            print(f"\nFinal Text: {repr(self.bit_array_to_string(result))}\n")

        return result
        # print(self.bit_array_to_string(text))


if __name__ == '__main__':
    d = DES_Algorithm("abcdeabcdeabcdeaq", "qwertyuio")
    encryptedText = d.DES(False)
    c = DES_Algorithm(encryptedText, "qwertyuio", False)
    decryptedText = c.DES(False)

    print(encryptedText)
    print(decryptedText.strip(" "))
