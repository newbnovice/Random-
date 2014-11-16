#from sys import argv

#first, second, third = argv #Here for no reason. I don't know.
prompt = '> '

counter = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #This is how you initialize a list.

class Books(object):
	
	def method(self):
		print "Who is coming?"
		oneinput = raw_input(prompt) #asks for user input with a > next to it to look nice.
		for number in counter:
			print "#%d: The %s are Coming!" % (number, oneinput) #replaces %d (decimal) 
																 #replaces %s (string)

class HistoryBook(Books):

	def method(self):
		print "Who is swole?"
		whoisswole = raw_input(prompt)
		for number in counter:
			print "#%d: %s is swole?!" % (number, whoisswole) #The same thing as the above, just different text.
		#super(HistoryBook, self).method() #This basically just calls class Books
										  #.method().
		#print "Books.altered!"

library = Books()
specifics = HistoryBook()

specifics.method()
#ibrary.method()
