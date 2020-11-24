#Program that can encrypt and decrypt files

#import decryptor, encryptor
#import keyGenerator
from cryptography.fernet import Fernet
from easygui import *
import sys

newKey = False
onlyTxt = False

def checkTxt(fileName):
    if onlyTxt:
        if ".txt" in fileName:
            notTxt = False
            return fileName
        else:
            notTxt = False
            return fileName + ".txt"
    else:
        notTxt = True
        if "." in fileName:
            return fileName
        else:
            return fileName

############################################################################

def keyGenerator(newKeyName):
    # Generates key
    key = Fernet.generate_key()

    # Saves key to file (testKey.key)
    keyFile = open(newKeyName, "wb")
    keyFile.write(key)
    keyFile.close()
    
    #Returns the name of the new key file
    return newKeyName

############################################################################

def encryptor(fileName, keyName, newFile):
    import sys
    
    try:
      open(fileName, "rb")
      open(keyName, "rb")
#      open(newFile, "rb")
    except FileNotFoundError:
      print("1 or more specified files could not be found")
      print("Make sure files are located in the same directory as this program.")
      print("Please terminate then restart this program")
      sys.exit()
    except:
      print("Something else went wrong")
        
    # Opens testKey file and saves the key as the var key
    keyFile = open(keyName, "rb")
    key = keyFile.read()
    keyFile.close()
    
    # Opens message file and saves the message in the str message
    messageFile = open(fileName, "rt")
    message = messageFile.read()
    messageFile.close()

    # Encodes message
    encodedMsg = message.encode()

    # Encrypts the message
    f = Fernet(key)
    encryptedMsg = f.encrypt(encodedMsg)
    
    # Saves encoded message to file
    encodedMsgFile = open(newFile, "wb")
    encodedMsgFile.write(encryptedMsg)
    encodedMsgFile.close()


############################################################################

def decryptor(fileName, keyName, newFile):
    
    try:
      open(fileName, "rb")
      open(keyName, "rb")
#      open(newFile, "rb")
    except FileNotFoundError:
      print("1 or more specified files could not be found")
      print("Make sure files are located in the same directory as this program.")
      print("Please terminate then restart this program")
      sys.exit()
    except:
      print("Something else went wrong")
        
    # Opens testKey file and saves the key as the var key
    keyFile = open(keyName, "rb")
    key = keyFile.read()
    keyFile.close()
    
    # Opens encrypted message file and saves the message in the str message
    messageFile = open(fileName, "rb")
    encryptedMsg = messageFile.read()
    messageFile.close()
    
    # Decrypts the message
    f = Fernet(key)
    decryptedMsg = f.decrypt(encryptedMsg) 

    # Decode the message
    originalMsg = decryptedMsg.decode()
    
    # Saves encoded message to file (encodedMessage)
    originalMsgFile = open(newFile, "wt")
    originalMsgFile.write(originalMsg)
    originalMsgFile.close()
    
###########################################################################

message = "How would you like to modify a file today?"
title = "Cryptography"
if boolbox(message, title, ["Encrypt", "Decrypt"]):
    taskName = "encrypt"
    
    message = "Would you like to generate a new key?"
    title = "Cryptography"
    
    if boolbox(message, title, ["Yes", "No (already have pre existing key)"]):
        newKey = True
    else:
        newKey = False

else:
    taskName = "decrypt"


if taskName == "encrypt":
    fieldNames = ["Plain Text File", "Key File", "New File Name"]
    
elif taskName == "decrypt":
    fieldNames = ["Encrypted File", "Key File", "New File Name"]

if newKey == True:
    fieldNames.pop(1)
    fieldNames.append("New Key File")
    


###########################################################################

#Multi Choice Box
msg = "Enter the names of files. Include (.txt)"
title = taskName.capitalize() + "or"
fileNames = multenterbox(msg, title, fieldNames)
if fileNames is None:
    sys.exit(0)
# make sure that none of the fields were left blank
while True:
    errormsg = ""
    for i, name in enumerate(fieldNames):
        if fileNames[i].strip() == "":
          errormsg += "{} is a required field.\n\n".format(name)
    if errormsg == "":
        break # no problems found
    fileNames = multenterbox(errormsg, title, fieldNames, fileNames)
    if fileNames is None:
        break
#print("Reply was:{}".format(fileNames))


if taskName == "encrypt":
    if newKey:
        newKeyName = fileNames[2]
        keyGenerator(newKeyName)
        keyName = newKeyName
        
        file = fileNames[0]
        newFile = fileNames[1]
        encryptor(file, keyName, newFile)
        
        msgbox("Encryption Complete", ok_button="Finish")
        
    else:
        file = fileNames[0]
        keyName = fileNames[1]
        newFile = fileNames[2]
        encryptor(file, keyName, newFile)
        
        msgbox("Encryption Complete", ok_button="Finish")

        
 
elif taskName == "decrypt":
    file = fileNames[0]
    keyName = fileNames[1]
    newFile = fileNames[2]
    decryptor(file, keyName, newFile)
    
    msgbox("Decryption Complete", ok_button="Finish")

#############################################################

#try:
#  open(fileName, "rb")
#  open(keyName, "rb")
#except FileNotFoundError:
#  print("1 or more specified files could not be found")
#  print("Make sure files are located in the same directory as this program.")
# print("Please terminate then restart this program")
#except:
#  print("Something else went wrong")