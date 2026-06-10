
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
        change = random.randint(-5, 5)
        stock[1] += change
        if stock[1] < 1:
            stock[1] = 1

def display_stocks():
    print("\n--- MARKET ---")
    for stock in stocks:
        print(f"  {stock[0]:<6} ${stock[1]}")

    print("\n--- PORTFOLIO ---")
    if not portfolio:
        print("  (empty)")
    else:
        for pstock in portfolio:
            symbol = pstock[0]
            buy_price = pstock[1]
            status = " [HELD]" if len(pstock)>2 and pstock[2] else ""
            
            for market_stock in stocks:
                if market_stock[0] == symbol:
                    current_price = market_stock[1]
                    profit = current_price - buy_price
                    profit_str = f"+${profit}" if profit >= 0 else f"-${abs(profit)}"
                    print(f"  {symbol:<6} bought @ ${buy_price} | current ${current_price} | {profit_str}{status}")
                    break
        
       
   
def buy(balance):
    uinput=input('enter stock you want to buy:').upper()
    if any(stock[0] == uinput for stock in stocks):
        print('stock found')
    else:
        print('stock not found press enter')
    for stock in stocks:
        if stock[0]== uinput:
            if balance>= stock[1]:
                balance-=stock[1]
                portfolio.append(stock.copy())
                if len(portfolio[-1]) == 2:
                    portfolio[-1].append(False)
                print (f"you bought {uinput} at ${stock[1]}")
                print(f"balance: ${balance}")
            else:
                print("Not enough money")
            return balance
    



def sell(balance):
    uinput3=input('enter stock you want to sell:').upper()
    for pstock in portfolio:
        if pstock[0]==uinput3:
            if len(pstock) > 2 and pstock[2]:
                print(f"This stock is HELD and cannot be sold.")
                return balance
            
            for stock in stocks:
                if stock[0]==uinput3:
                    balance+=stock[1]
                    portfolio.remove(pstock)
                    print(f"you sold {uinput3} at ${stock[1]}")
                    print(f"balance: ${balance}")
                    return balance
    print("stock not found")

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

def networth():
    """Calculate total net worth: balance + all portfolio holdings at current price."""
    total = balance
    for pstock in portfolio:
        symbol = pstock[0]
        for market_stock in stocks:
            if market_stock[0] == symbol:
                total += market_stock[1]
                break
    return total

           


if __name__ == '__main__':
    while True:
        generatestockprice()
        display_stocks()
        
        print(f"\nBalance: ${balance}")
        print(f"Net Worth: ${networth()}")
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
            print(f"Final net worth: ${networth()}")
            break
        else:
            print("Invalid option.")
        
