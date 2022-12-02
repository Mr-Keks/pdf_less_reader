import PyPDF2
import re
from googletrans import Translator
from spellchecker import SpellChecker


def translate_text():
    with open("clear_text.txt", "r", encoding='utf8') as file:
        text = file.read()

    translator = Translator()
    with open("transtated_text.txt", "w", encoding='utf8') as file:
        file.write(translator.translate(text, dest='uk').text)


def get_page(num):
    pdfFileObj = open('1.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(num)

    # extracting text from page
    text = pageObj.extract_text()
    pdfFileObj.close()

    with open("original_text.txt", "w", encoding='utf8') as file:
        file.write(text)

def clean_text():
    with open("original_text.txt", 'r', encoding='utf-8') as file:
        text = file.read()
       
    # delete enter`s
    white_text = []
    
    for word in text.split("\n"):
        white_text.append(word.rstrip())

    # text without enter`s
    text = " ".join(white_text)
  
 
    # find all smile symbols and replace for '-'
    text = re.sub(chr(2), "-", text)
    ture = re.findall(r'[\w]+[-]+[\w]+', text)
 
    
    spell = SpellChecker()
     
    # check correct words with '-'
    # for word in [se for se in spell.unknown(ture)]:
    #     correct = spell.unknown(word)
    #     print(word, correct, spell.correction(word.split("-")[0]))
    #     print(word, correct, spell.correction(word.split("-")[1]))
    #     text = re.sub(f'{word}', f'{spell.correction(word)}', text)
    
    
    with open("clear_text.txt", "w", encoding='UTF-8') as file:
        file.write(text) 

    return text    

#num = int(input('enter number of book: '))
#page = get_page(260)
clean_text()
translate_text()