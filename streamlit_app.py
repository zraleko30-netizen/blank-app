#SS = start script (to encode somthing)
#US = to unscript (to decode somthing)
#Password = start of code to eneter into the system



print("Welcome to the PFACA")
password = input("What is the accese code:")
if password == "392326":
    Start = input("script or unscript:")
    if Start == "script":
        alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz" # "zyxwvutsrqponmlkjihgfedcba" 
        get_letter,  keyword = 0, []
        text = str(input("Enter the text:")).strip().lower() 
        key = int(input("Enter the key:"))
        
        if 0 < key <= 26:
            for letter in text:
                get_letter = alphabet.index(letter) + key 
                keyword.append(alphabet[get_letter])
            print("".join(keyword)) 
        else:
            print("Key must be between 1 and 26")
        
    if Start == "unscript":
        US = input("What would you like to decode:")
        alphabet = "zyxwvutsrqponmlkjihgfedcba" # " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"
        get_letter, keyword = 0, []
        
        text = str(input("Enter the text: ")).strip().lower()
        key = int(input("Enter the key: "))
        
        if 0 < key <= 26:
            for letter in text:
                get_letter = alphabet.index(letter) + key	
                keyword.append(alphabet[get_letter])
            print("".join(keyword))
        else:
            print("Key must be between 1 and 26!")

        
        
else:
    print("Incorrect")
