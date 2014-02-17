#wfp, continuous prompt for a file name.

file_str = input("Enter a file to open: ")

while True:
    try:
        file_obj = open(file_str, 'r')
        print("Opened the file", file_str)
        break
    except IOError:
        print("Bad file name, try again")
        file_str = input("Enter a file to open: ")
    print("next iteration")

# do something with the file here
file_obj.close()
print("successfully closed the file")
print("moving on")

# Alternative
#keep_going_bool = True

#while keep_going_bool:
        #keep_going_bool = False
