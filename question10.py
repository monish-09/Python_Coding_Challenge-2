day = input("Enter day: ")

if day.lower() == "sunday":
    price = 200
elif day.lower() == "saturday":
    price = 180
else:
    price = 150

print("Ticket Price:", price)