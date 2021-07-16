import  numpy as np

#41 characters
alphabet = ['a','b','c','d','e','f','g','h','i','g','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x',
            'y','z','A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z','?','/','.',',',':',';','!','@',
            '#','$','%','^','&','*','(',')','-','_','+','=',
            '1','2','3','4','5','6','7','8','9','0',' ', ' ']
numbers = []
encrypted_matrix = []
key = [[19,7], [-11,9]]

def main():
    #Ask For input
    input_text = input("Enter text: ")
    #Parse through the text an assign the index number to each letter
    for i in input_text:
        if i in alphabet:
            numbers.append(alphabet.index(i)+1)
        else:    
            return

    if(len(numbers) % 2 == 1):
        numbers.append(len(alphabet)-1)

    matrix = np.reshape(numbers, [int(np.ceil(len(numbers)/2)),2 ])
    num_rows, num_cols = matrix.shape
    for i in matrix:
        encrypted_matrix.append(np.matmul(i, key))
    #convert an array to a matrix
    encrypted_message = np.asmatrix(encrypted_matrix)
    print(encrypted_message)
    #Write to a file
    f = open("encrypted_message.txt", "w")
    size = np.prod(encrypted_message.shape)
    for i in range(size):
        f.write(str(encrypted_message.item(i)) + " ")
    f.close

main()
