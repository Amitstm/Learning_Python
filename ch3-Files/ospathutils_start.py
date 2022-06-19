import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # print the name of the os
    print(os.name)
    # check for item existence and type
    print("Item exists:", str(path.exists("textfile.txt")))
    print("Item is a file:", path.isfile("textfile.txt"))
    print("Item is a dirrectoru:", path.isdir("textfile.txt"))
    
    # Work with file paths

    print("item's path:", path.realpath("textfile.txt"))
    print("item's path and name:", path.split(path.realpath("textfile.txt")))
    # Get the modification time
    t = time.ctime(path.getatime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getatime("textfile.txt")))
    
    #  Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))
    print ("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")
if __name__ == '__main__':
    main()
        