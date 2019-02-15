fin1 =open('Book1.txt','r')
fin2 =open('Book2.txt','r')
fin3 =open('Book3.txt','r')
line =fin.readline()
word =line.strip()
def unique_words(Book1,Book2,Book3):
	input_words =open(Book1,'r')
	words_contents =fin.readline()
	input_words.close()
	words =open(Book2,'w')
	for line in fin1:
		if line not in fin1:
			words.write(str(word) + "\n")
	words.close()
		for line in fin2:
			if line not in fin2:
				words.write(str(word) + "\n")
		words.close()	
			for line in fin3:
				if line not in fin3:
			words.write(str(word)) + "\n")
			words.close()
print(uique_words(Book1,Book2,Book3))
		


fin1 =open('Book1.txt','r')
fin2 =open('Book2.txt','r')
fin3 =open('Book3.txt','r')
line = fin.readline()
word = line.strip()
def count_the_article(Book1,Book2,Book3):
	for line in fin1:
		for  line in fin2:
			for line in fin3:
				count={}
				for of in fin1:
					if  of in count:
						count[word]+=1
					else:
						count[word] =1
				for a in fin2:
					if a in count:
						count[word]+=1
					else:
						count[word] =1
				for x in fin3:
					if  x in count:
						count[word]+=1
					else:
						count[word]=1
print(count_the_article(Book1,Book2,Book3))



def sorted_words(Book1,Book2,Book3):
list_of_words =[]
	for word in fin1:
		if all(word[0]<=c for c in word[1:]):
			list_of_words.append(word)
	list_of_words.sort()
	print(list_of_words)
	for word i fin2:
		if all(word[0]<=c for c in word[1:]);
			list_of_words.append(word)
	list_of_words.sort()
	print(list_of_words)
	for word in fin3:
		if all(word[0]<=c for c in word[1:]):
		list_of_words.append(word)
	list_of_words.sort()
	print(list_of_words)

print(sorted_words(Book1,Book2,Book3))

