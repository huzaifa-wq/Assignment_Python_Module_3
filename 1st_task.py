zander_length = int(input("enter the length of the zander in centimeters: "))
size_limit = 42
standerd_size = size_limit - zander_length
if zander_length <= size_limit :
    print(" release the fish back in the lack because your fish is",standerd_size,"cm small then size limit")
else:
    print("Nice fish size")