class WaterMain:
    def __init__(self, ml, one_Liter, five_Liter):
        self.prices = {
            1: ("500 mL Bottle", ml), 
            2: ("1 Liter Bottle", one_Liter),
            3: ("5 Liter Container", five_Liter)
        }

    
    def main_transaction(self, choice, payment):
        
        
        if choice not in self.prices:
            print("Invalid selection.")
            return

        name, price = self.prices[choice]
        
        print(f"Container: {name}")
        print(f"Price: ₱{price}")

        if payment < price:
            print("Insufficient payment.")
            return
        
        change = payment - price
        print(f"Change: ₱{change}")

        
        remaining = change
        
        twenties = remaining // 20
        remaining %= 20
        
        tens = remaining // 10
        remaining %= 10
        
        fives = remaining // 5
        remaining %= 5
        
        ones = remaining


        print(f"\u20b120: {twenties}")
        
        print(f"\u20b110: {tens}")
        
        print(f"\u20b15: {fives}")
        
        print(f"\u20b11: {ones}")
        


vendo = WaterMain(ml=10, one_Liter=15, five_Liter=40)

choice = int(input())
payment = int(input())

vendo.main_transaction(choice, payment)