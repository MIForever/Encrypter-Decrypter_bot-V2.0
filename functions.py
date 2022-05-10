
printable = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \t\n"
printable+= '"' 
char_list = []
for i in printable:
    char_list.append(i)

def encrypter(message,password):

    cipher =''

    index_password = 0

    for char in message:
        movement = int(password[index_password])
        if int(password[index_password])==0:
            movement = 10
        
        if len(char_list)-(char_list.index(char)+1)<=movement:
            charid = char_list.index(char)
            extra = movement-(len(char_list)-(char_list.index(char)+1))
            movement = -(charid-extra)

        cipher=cipher+char_list[char_list.index(char)+movement] 
          
        if index_password+1==len(password):
            index_password=-1
        index_password+=1
    return cipher


def decrypter(cipher,password):

    message = ''

    index_password = 0
    for c in cipher:
        movement = int(password[index_password])
        if int(password[index_password])==0:
            movement = 10

        if char_list.index(c)<movement:
            
            charid = char_list.index(c)
            extra = movement-(len(char_list)-(char_list.index(c)+1))
            movement = -(charid-extra)
            
        message=message+char_list[char_list.index(c)-movement] 

        if index_password+1==len(password):
            index_password=-1

        index_password+=1

    return message
