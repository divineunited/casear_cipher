def casear(message, n, encrypt=True):
    '''This casear encryption allows for undercase and capital letters. Pass a message to encrypt or decrypt, n number of positions (must be less than 26) where n will add to the alphabet for encryption and subtract for decryption, and optional encrypt=False to allow for decryption of a message. The message must not include any non alphabetic characters besides a space'''

    # creating our dictionary with number key and letter value
    num_let = {i:let for i, let in enumerate('abcdefghijklmnopqrstuvwxyz')}
    # creating our dictionary with corresponding letter key and number value
    let_num = {let:i for i, let in enumerate('abcdefghijklmnopqrstuvwxyz')}
    # creating versions for the capital letters
    NUM_LET = {i:let for i, let in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    LET_NUM = {let:i for i, let in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    
    final = ''

    # encryption
    if encrypt:

        # going through our message and replacing each letter with a coded number by adding n to each letter and using the dictionary.
        for letter in message:
            # if this letter is a space, leave it
            if letter in ' ':
                final += letter
            # if letter is non capital
            elif letter in let_num.keys():
                # if this is one of the later numbers at the end of the dictionary, loop around to the beginning
                if let_num[letter] + n > 25:
                    final += num_let[let_num[letter]+n-26]
                else:
                    final += num_let[let_num[letter]+n]
            # if letter is capitalized
            else:
                if LET_NUM[letter] + n > 25:
                    final += NUM_LET[LET_NUM[letter]+n-26]
                else:
                    final += NUM_LET[LET_NUM[letter]+n]
        return final
        
    # decryption
    else:
        for letter in message:
            if letter == ' ':
                final += letter
            elif letter in let_num.keys():
                if let_num[letter] - n < 0:
                    final += num_let[let_num[letter]-n+26]   
                else:
                    final += num_let[let_num[letter]-n]
            else:
                if LET_NUM[letter] - n < 0:
                    final += NUM_LET[LET_NUM[letter]-n+26]
                else:
                    final += NUM_LET[LET_NUM[letter]-n]
        return final

# main testing:

message = 'This is a test of the excellent Casear Cipher'
print(casear(message, 3))

cipher = 'Wklv lv d whvw ri wkh hafhoohqw Fdvhdu Flskhu'
print(casear(cipher,3,encrypt=False))