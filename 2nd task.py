

cabin_class = str(input("What is your cabin class: "))

LUX = cabin_class
A = cabin_class
B = cabin_class
C = cabin_class

if cabin_class == LUX :
    print("upper-deck cabin with a balcony.")

elif cabin_class == A:
    print("above the car deck, equipped with a window.")

elif cabin_class == B:
    print("windowless cabin above the car deck.")

elif cabin_class == C:
    print("windowless cabin below the car deck.")

else:
    print("invalid cabin class")