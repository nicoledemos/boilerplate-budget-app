class Category:

    def __init__(self, type):
        self.name = type
        self.balance = 0.0
        self.ledger = list()

    def __str__(self):
        ledger_total = self.get_balance()

        start_stars = (30 - len(self.name)) // 2

        lines = ("*" * start_stars + f"{self.name}").ljust(30,"*")

        for item in self.ledger:
            lines = lines + "\n" + (item['description'][0:23]).ljust(23," ")
            lines = lines +(f"%0.2f" % item['amount']).rjust(7," ")

        lines = lines + "\n" + "Total: " + f"%0.2f" % ledger_total
        return lines

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        print(self.name)
        if not self.check_funds(amount): return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        balance = sum(item['amount'] for item in self.ledger)
        return balance

    def transfer(self, amount, other_category):
        balance_ok = self.withdraw(amount, "Transfer to " + other_category.name)
        if not balance_ok: return False
        other_category.deposit(amount, "Transfer from " + self.name)
        return True

    def check_funds(self, amount):
        balance =self.get_balance()
        if balance < amount: return False
        return True

    def perc_spend(self):
        deposits = 0.0
        withdrawals = 0.0
        for item in self.ledger:
            if float(item['amount']) > 0:
                deposits = deposits + float(item['amount'])
            else:
                withdrawals = withdrawals + -1 * float(item['amount'])
        if withdrawals == 0:
            return 0
        else:
            return int((withdrawals / deposits ) * 100)

def generate_histogram(self,cat_perc_spend):
    lines = str()

    lines = "Percentage spent by category"
    for step in range(100,-10,-10):
        lines = lines + "\n"
        lines = lines + str(step).rjust(3," ") + "| "
        for category in self:
            if cat_perc_spend[category.name] >= step: 
                lines = lines + "o  "
            else:
                lines = lines + "   "
    lines = lines + "\n    " + "---" * len(self) + "-"
    return lines

def generate_labels(self,lines):
 
    max_label_size = max(len(category.name) for category in self)
    for l in range(0, max_label_size):
        lines = lines + "\n    "

        for o in range (len(self)):
            if len(self[o].name) > l:
                lines = lines + " " + self[o].name[l] + " "
            else:
                lines = lines + "   "
        lines = lines + " "
    return lines

def create_spend_chart(self):
    cat_perc_spend = dict()
    
    for category in self:
        cat_perc_spend[category.name] = category.perc_spend()
    
    above_axis = generate_histogram(self,cat_perc_spend)
    chart = generate_labels(self,above_axis)
    return chart