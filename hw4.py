'''
The function any_lowercase1(s) only checks if the first char of the string is lowercase. 
It is is lowercase, the function will return True, else False.  

The function any_lowercase2(s) will only loop once and check is the character "c" is lowercase. 
Since it is lowercase, the function will always return the string "True". 

The function any_lowercase3(s) will iterate through each char in the string and check if it is lowercase. 
However, the function will only return True if the last character in the string is lowercase.  

The function any_lowercase4(s) successfully checks if the string contains any lowercase characters.
It will iterate through each char in the string and flag will remain false if there are no lowercase letters in the string. 
Once there is a lowercase letter, flag will be updated to True and will remain True, thus doing the task correctly. 

The function any_lowercase5(s) checks if there are any uppercase letters in the string. 
The function will iterate through each character and if the char is uppercase, the function will stop and return False. 
Otherwise the function will return True, meaning that the string is all lowercase letters. 
'''

def rotate_word(string, int):
    encryptedWord = ""
    for c in string:
        encryptedWord += chr(ord(c) + int)
    return encryptedWord

print(rotate_word("cheer", 7))