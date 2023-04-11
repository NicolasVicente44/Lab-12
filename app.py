# import PyPDF2

# pdfFileObj = open('encryptedWord.pdf', 'rb')

# pdfReader = PyPDF2.PdfReader(pdfFileObj)

# if pdfReader.is_encrypted: 
#     pdfReader.decrypt('apple123')
    
# pageObject = pdfReader.pages[0]

# print(pageObject.extract_text())





# import PyPDF2

# pdfFileObj = open('encryptedWord.pdf', 'rb')

# pdfReader = PyPDF2.PdfReader(pdfFileObj)

# passwords = ['helloworld', 'bus', 'car', 'apple123', 'router999']

# if pdfReader.is_encrypted: 
#     for password in passwords:
#         try:
#             pdfReader.decrypt(passwords[0])
#             pdfReader.decrypt(passwords[0])
#             pdfReader.decrypt(passwords[1])
#             pdfReader.decrypt(passwords[2])
#             pdfReader.decrypt(passwords[3])
#             pdfReader.decrypt(passwords[4])
#         except ValueError:
#             print("All of those passwords were invalid")
            
    
# pageObject = pdfReader.pages[0]

# print(pageObject.extract_text())




import PyPDF2
import os

fileOne = open('dictionary.txt')

fileContent = fileOne.read()

wordList = fileContent.splitlines()

pdfFileObj = open('encryptedWordPartner2.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)


foundPassword = False


if pdfReader.is_encrypted:
    for word in wordList:
        try:
            
            
            if pdfReader.decrypt(word) > 0: 
                foundPassword = True
                print(word)

                break
            
            
        except ValueError:
            continue



if foundPassword:
    
    pageObject = pdfReader.pages[0]
    print(pageObject.extract_text())
    
else:
    
    print("All of those passwords were invalid")



pdfFileObj.close()

fileOne.close()

