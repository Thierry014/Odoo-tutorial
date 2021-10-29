def print_silly_name(name):
    # index should be defined (you can also put index in main() as an user input, if you want make it dynamic)
    index = 0
    silly_string =""
    while (index < 60):
        # print 59 times silly
        index += 1
        silly_string += 'silly '
    print(f"{silly_string}name")

def main():
    name = input("What is your name?\n")
    if (name == "Ted") or (name == "Fred"):
        print(f"{name} is an awesome name!")
    else:
        print(f"{name} is a ")
        print_silly_name(name)
       
main()