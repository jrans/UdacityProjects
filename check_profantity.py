def read_text():
    quotes = open("C:\Users\Joe\Desktop\Joe\Udacity\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    
read_text()
