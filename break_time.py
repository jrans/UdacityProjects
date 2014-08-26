import time
import webbrowser


count = 0

print ("this program started on" + time.ctime())
while (count < 3):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=nPImqZo0D74&list=FLN3h_oc4PZSLH6-IdgnVooQ&index=12")
    count = count + 1
