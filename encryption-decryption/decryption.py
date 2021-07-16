import  numpy as np

alphabet = ['a','b','c','d','e','f','g','h','i','g','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x',
            'y','z','A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T','U','V',
            'W','X','Y','Z','?','/','.',',',':',';','!','@',
            '#','$','%','^','&','*','(',')','-','_','+','=',
            '1','2','3','4','5','6','7','8','9','0',' ', ' ']
key = [[19,7], [-11,9]]
inverse_key = np.linalg.inv(key)
decrypted_text = ""
decrypted_matrix = []

def main():  
    #Open FIle
    f = open("encrypted_message.txt", "r")
    encrypted_string = f.read()
    Counter = 0
    for i in encrypted_string:
        if i == " ":
            Counter += 1
    number = ""
    x = []
    for i in encrypted_string:
        if i != " ":
            number += i
        elif i == " ":
            x.append(int(number))
            number = ""

    encrypted_message = ""
    encrypted_message = np.reshape(x, [int((Counter)/2) ,2])

    #decryption
    for i in encrypted_message:
        decrypted_matrix.append(np.matmul(i, inverse_key).astype(int))
    decrypted_array = np.asarray(decrypted_matrix).reshape(-1)

    if(decrypted_array[-1] == alphabet.index(' ') or decrypted_array[-1] == alphabet.index(' ') + 1):
        decrypted_array_new = decrypted_array[:-1]
    else:
        decrypted_array_new = decrypted_array
    print(decrypted_array)

    decrypted_text = ''
    for i in decrypted_array_new:
        if i < len(alphabet):
            decrypted_text += alphabet[i-1]
    print(decrypted_text)

main()
