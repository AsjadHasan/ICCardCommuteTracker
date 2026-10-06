def ride(balance, fare):
    if balance >= fare:
        balance -= fare
        return balance, True
    else:
        return balance, False
def top_up(balance, amount):
    valid_amounts = [1000, 2000, 3000, 5000, 10000]
    if amount in valid_amounts:
        balance += amount
        return balance, True
    else:
        return balance, False
balance = int(input("Enter starting balance: "))
total_fares = 0
rides = 0
top_ups = 0
while True:
    print("\n===== IC CARD MENU =====")
    print("1. Ride")
    print("2. Top up")
    print("3. Check balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        fare = int(input("Enter train fare: "))
        balance, success = ride(balance, fare)
        if success:
            total_fares += fare
            rides += 1
            print(f"Paid ¥{fare}. Balance: ¥{balance}")
        else:
            print("Insufficient balance")
    elif choice == "2":
        amount = int(input("Enter top-up amount: "))
        balance, success = top_up(balance, amount)
        if success:
            top_ups += 1
            print(f"Balance: ¥{balance}")
        else:
            print("Invalid amount. Please enter 1000, 2000, 3000, 5000 or 10000.")
    elif choice == "3":
        print(f"Balance: ¥{balance}")
    elif choice == "4":
        print(f"\nFinal balance: ¥{balance}")
        print(f"Total fares: ¥{total_fares}")
        print(f"Rides: {rides}")
        print(f"Top-ups: {top_ups}")
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")