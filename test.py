import string
text="Hey! What's up bro?,jibii"
text=text.replace('!',' ')
text=text.replace('?',' ')
text=text.replace(',','')
test_text=text.translate(str.maketrans('','',string.punctuation))
text=test_text.split()
print(text)