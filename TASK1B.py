file1=set(line.strip() for line in open('Book1.txt')
file2=set(line.strip() for line in open('Book2.txt')
file3=set(line.strip() for line in open('Book3.txt')
fin1=set(line.split() for line in open('Book1.txt')
fin2=set(line.split() for line in open('Book2.txt')
fin3=set(line.split() for line in open('Book3.txt')
def common_words(Book1,Book2,Book3, top=20):
	"""return the comon words in the lines of the text"""
	words=collectons.Counter()
	for line in fin1:
		words.update(line.lower().split())
	return words.common_words(top)

top_ten_words = common_words(file1.input(), 10)
	for line  in fin2:
		words.update(line.lower().split())
	return words.common_words(top)
top_ten_words = common_words(file2.input(), 10)
	for line in fin3:
		words.update(line.lower().split())
	return words.comon_words(top)
top_ten_words = common_words(file3.input(), 10)

