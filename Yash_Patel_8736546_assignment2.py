print("------------------WELCOME TO OUR SHOP--------------------")

age = input('''What is your age? ''')
print("Hi, welcome to my shop. Here are items available")

shirt_price = 19.99
short_price = 8.95

print("Price of Shirt is 19.99")
print("Price of Short is 8.95")

shirt_color = input("\nEnter the color of shirt: ")
option = int(input("\nDo you want Polo-Shirt or T-shirt(For Polo-Shirt enter 1 and for T-Shirt enter 2: "))

short_color = input("\nEnter the color of short: ")
option = int(input("\nDo you want Jeans or Cotton (For Jeans enter 3 and for Cotton enter 4: "))

if option == 1:

    shirt_type = "Polo-Shirt"
    print("\nThe type of shirt you selected is", shirt_type)

elif option == 2:

    shirt_type = "T-Shirt"
    print("\nThe type of shirt you selected is ", shirt_type)

elif option == 3:

    short_type = "Jeans"
    print("\nThe type of short you selected is ", short_type)

elif option == 4:

    short_type = "Cotton"
    print("\nThe type of short you selected is ", short_type)
else:

    print("Incorrect number")

num_shirt = int(input("\nNumber of shirts: "))

num_short = int(input("\nNumber of shorts: "))

total = (shirt_price * num_shirt) + (short_price * num_short)

tax = 0.13 * total

final_total = tax + total

print("\nThe color of your shirts are: ", shirt_color)
print("\nThe color of your shorts are: ", short_color)

print("\nThe total number of shirt your want are: ", num_shirt)
print("\nThe total number of short your want are: ", num_short)

print("\nYour price before adding HST is", total)

print("\nYour total price after adding HST is", final_total)
