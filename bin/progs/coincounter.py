"""
Coin counter program.
For use in NLOS, to test the program standard.
"""

# generated by ChatGPT, all praise our robot overlords
def nlosrun():
    try:
        coin_counter = {
            'Penny': 0,
            'Nickel': 0,
            'Dime': 0,
            'Quarter': 0
        }

        coin_value = {
            'Penny': 0.01,
            'Nickel': 0.05,
            'Dime': 0.1,
            'Quarter': 0.25
        }

        total_amount = 0.0

        while True:
            coin = input("Enter coin (Penny, Nickel, Dime, Quarter, Done): ")

            if coin == "Done":
                break
            elif coin in coin_counter:
                coin_counter[coin] += 1
                total_amount += coin_value[coin]
            else:
                print("Invalid coin. Please enter a valid coin.")

        for coin, count in coin_counter.items():
            print(f"{coin}: {count}")

        print(f"Total amount: ${total_amount:.2f}")
        return 0
    except:
        return 1

if __name__ == "__main__":
    print("This file is not meant to be run by Python.\nPlease install or open in NLOS to run this application.")