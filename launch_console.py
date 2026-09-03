print("Welcome to the Launch Console!")
name = input("What is your name? ")
print("Hi, " + name +"!") 

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    choice = input("Pick your choice from 1-3: ")
    if choice == "1":
        print("I'm a freshman at Round Rock High School who is passionate about robotics and software development.")
    elif choice == "2":
        print("My goal is to create a complex project this term and hopefully land an internship with Code2College in the soon future!")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3!")