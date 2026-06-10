
import random

stocks =[
["BSC",100],
["R&R",60],
["HUIS",120],
["CP",670],
["AO",240],
["BJ",210],
["JIT",290]
    ]
#global balance=int(1000)
balance=1000
portfolio=[]
#portfolio.append(stocks)

def generatestockprice():
    
    for stock in stocks:
        price=random.randint(1,1000)
        stock[1]=price

def display_stocks():
    print("\n--- MARKET ---")
    for stock in stocks:
        print(f"  {stock[0]:<6} ${stock[1]}")

    print("\n--- PORTFOLIO ---")
    if not portfolio:
        print("  (empty)")
    else:
        for stock in portfolio:
            status = " [HELD]" if len(stock)>2 and stock[2] else ""
            print(f"  {stock[0]:<6} bought @ ${stock[1]}{status}")
        
       
   
def buy(balance):
    # `uinput` is a variable that stores the user input for the stock symbol that the user wants to
    # buy, sell, or hold. It is used to identify the stock selected by the user and perform the
    # corresponding action based on the input provided by the user.
    uinput=input('enter stock you want to buy:').upper()
    if uinput in stocks:
        print('stock found')
    else:
        print('stock not found press enter')
    for stock in stocks:
        if stock[0]== uinput:
            if balance>= stock[1]:
                balance-=stock[1]
                portfolio.append(stock.copy())
                print (f"you bought {uinput} at ${stock[1]}")
               
                print(f"balance: ${balance}")
            return balance
            
            print("Not enough money")
            
    



def sell(balance):
    uinput3=input('enter stock you want to sell:').upper()
    if uinput3 in portfolio:
        print('stock found')
    else:
        print('stock not found')
    for stock in stocks:
        print(stock[0])
        print(uinput3)
        if stock[0]==uinput3:
            balance+=stock[1]
            portfolio.remove(stock)
            print(f"you sold {uinput3} at ${stock[1]}")
            print(f"balance: ${balance}")
            return
        return balance
        
    print("stock not found")
       # elif portfolio.append(stock):

def hold():
    """Toggle hold on a stock so it can't be accidentally sold."""
    uinput = input("Enter stock to toggle hold: ").upper()
    for stock in portfolio:
        if stock[0] == uinput:
            stock[2] = not stock[2]
            status = "HELD" if stock[2] else "RELEASED"
            print(f"{uinput} is now {status}.")
            return
    print("Stock not found in portfolio.")
           


if __name__ == '__main__':
    while True:
        generatestockprice()
        display_stocks()
        
        print(f"\nBalance: ${balance}")
        print("\nOptions: buy / sell / hold / quit")
        action = input("Action: ").lower()

        if action == "buy":
            balance = buy(balance)
        elif action == "sell":
            balance = sell(balance)
        elif action == "hold":
            hold()
        elif action == "quit":
            print(f"Final balance: ${balance}")
            break
        else:
            print("Invalid option.")
        
