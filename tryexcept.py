try:
    file= open("example.py", "r")
    data = file.read()

    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry, this file does not exist")
finally:
    print("Thank you for using this program")