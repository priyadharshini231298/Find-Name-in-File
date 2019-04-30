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
                       # if tag=='JJ' or tag=='NNP':
		lst.append(words)
		#print(lst)
print("Document Name:",lst[0],lst[1],lst[2])
for i in range(0,10):
	blob1=TextBlob(lst[i])
	for wrd,tag1 in blob1.tags:
		#print(wrd)
		#print(tag1)
		if tag1=='NN' or tag1=='NNP':
			print(lst[i],end=" ")
		else:
			sys.exit(1)


