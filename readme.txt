Coded by Raymond Shen for my ENEX project
Date: May 26, 2020

Libraries used:
Cryptography
Easy Gui

Steps to use this program:
Must be running windows 10
Program must be in the same folder as the text files
Launch the program
Select the options presented to you

Encryption Type:
AES 128 bit in CBC mode (form key)
Approved by the US goverment and still widely used today

What you can encrypt:
Any file containing normal characters. (txt, py, cfg)


Following is found from rigorous testing of the application

If you get an error message when encrypting:
Requested file(s) not found
Attempting to encrypt a file with special characters
Attempting to encrypt something that is not a text file (jpg, png, exe)
Attempting to encrypt a file that is too large, over 25mb (about 1 million rows of text)

If you get an error message when decrypting:
Requested file(s) not found
Wrong key used


What I was going for:

A program that can encrypt and decrypt files efficiently

1. User can choose to encrypt or decrypt
2. Asks user for the plain text or encrypted file
3. Askes user for the key file
4. Askes user for new name to save new file as
5. Returns an error message if something went wrong.

user friendly interface
encrypts an email for school demo
encryption for sharing information
upload to github share code to community. build responsibility and contribution to industry
https://cryptography.io/en/latest/fernet/

