import sys

def cat():
    print("meow")

def dog():
    print("bow bow")

def default():
    print("hello")

def main():
    if sys.arg[1]=="cat":
        cat()
    else:
        defualt()

if __name__ == '__main__':
    main()
