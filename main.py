seats = 50
bookings = {}

while True:
    print("\n1.Check Availability")
    print("2.Book Ticket")
    print("3.View Ticket")
    print("4.Cancel Ticket")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available seats:", seats)

    elif choice == "2":
        name = input("Enter name: ")
        age = input("Enter age: ")
        booking_id = len(bookings) + 1
        bookings[booking_id] = {"name": name, "age": age}
        seats -= 1
        print("Ticket booked. ID:", booking_id)

    elif choice == "3":
        bid = int(input("Enter booking ID: "))
        print(bookings.get(bid, "Not found"))

    elif choice == "4":
        bid = int(input("Enter booking ID: "))
        if bid in bookings:
            del bookings[bid]
            seats += 1
            print("Ticket cancelled")

    elif choice == "5":
        break
