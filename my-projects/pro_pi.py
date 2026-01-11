import random
MAX_LINES = 3
MAX_AMOUNT = 1000
MIN_AMOUNT = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}   

symbol_win = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}




def check_winnings(columns, lines, bet, values):
    print("\n\n----- CHECKING WINNINGS -----")
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines




def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns





def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()






def depsoit():
    print("\n\n----- DEPOSIT -----")
    while(1):
        amount = input("Enter amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero. Please try again.")
        else:
            print("Invalid input. Please enter a positive integer amount.")
    return amount
    




def lines():
    print("\n\n----- BETTING LINES -----")
    while(1):
        num_lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if num_lines.isdigit():
            num_lines = int(num_lines)
            if 1 <= num_lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and " + str(MAX_LINES) + ". Please try again.")
        else:
            print("Invalid input. It must be a digit, please try again.")
    return num_lines    





def bet():    
    print("\n\n----- BET AMOUNT -----")
    while 1:
        amount = input("Enter bet amount per line: $")
        if amount.isdigit():
            amount = int(amount)
            if amount :
                break
            else:
                print(F"Bet amount must be between ${MIN_AMOUNT} and ${MAX_AMOUNT}. Please try again.")
        else:
            print("Invalid input. Please enter a positive integer amount.")
    return amount





def game(balance):
    num_lines = lines()

    while 1:
        bet_amount = bet()
        total_bet = bet_amount * num_lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount (${total_bet}), your current balance is: ${balance}.")
        else:
            break
    import time
    for i in range (3,0,-1):
        print(i)
        time.sleep(2)
    print("\n\n----- SUMMARY -----")
    print(f"Deposited: ${balance}, Betting on {num_lines} lines.")
    print(f"\nYou are betting ${bet_amount} on {num_lines} lines. Total bet is: ${total_bet}")

    slots = spin(ROWS, COLS, symbol_count)
    print("\n\n----- SLOT MACHINE -----")
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, num_lines, bet_amount, symbol_win)
    print(f"\n\nYou won: ${winnings}")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet





def main():
    print("\n----- WELCOME TO FRANKIE'S SLOT MACHINE! -----\n\n")   
    balance = depsoit() 
    while 1:
        print(f"\nCurrent balance is: ${balance}")
        play = input("Press enter to play (q to quit).")
        if play == "q":
            break
        balance += game(balance)
    print(f"\nYou left with ${balance}. Thanks for playing!")



    


    
main()
