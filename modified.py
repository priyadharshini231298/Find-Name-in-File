import docx
import sys
from textblob import TextBlob
doc = docx.Document('Naveen_Senior-Trainer_Profile.docx')
lst=[]
tg=[]
for para in doc.paragraphs:
	print(para.text)
	blob=TextBlob(para.text)
	for words,tag in blob.tags:
		lst.append(words)

print("Document Name : ",end="")
for i in range(0,len(lst)):
	blob1=TextBlob(lst[i])
	for wrd,tag1 in blob1.tags:
		if tag1=='NN' or tag1=='NNP':
			print(lst[i],end=" ")
		else:
			sys.exit(1)


