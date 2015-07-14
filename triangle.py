import io

def triangle(datalist):
    """method that processes a tree diagram of values (whole numbers), and calculates the total for the highest path"""
    #to keep track of the rolling total
    total = 0 
    with open(datalist, 'r') as f:
        #to keep track of the list position so you know which one to compare next
        position = 0
        for line in f:
            #print position
            #remove the pesky newline
            noNewLine = line.replace('\n', '')   
            #make the string into a list.
            currentline = noNewLine.split(' ')

            if len(currentline)> 0:
               currentline.pop() #so, pop that last Null element.

            if len(currentline) > 1:
                if int(currentline[position]) > int(currentline[position +1]):
                    total = total + int(currentline[position])
                elif int(currentline[position]) < int(currentline[position + 1]):
                    total = total + int(currentline[position + 1])
                    position = position + 1
                else:
                    total = int(currentline[position])
            else: #only expected use is for first line.
                total = int(currentline[position])
    print total


triangle(r'C:\Users\Joe\Desktop\triangle.txt') #need the 'r' before the path because I did this on Windows(sigh)
