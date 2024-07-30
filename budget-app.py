class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spent = 0
    def __str__(self):
        chars = 30
        output = ''
        chars -= len(self.name)
        output += '*' * (chars//2) + self.name + '*' * (chars//2) + '\n'

        for item in self.ledger:
            chars = 30
            desc = item['description'][:23]
            amount = '{:.2f}'.format(float(item['amount']))[:7]
            chars -= (len(desc) + len(amount))
            output += desc + ' ' * chars + amount + '\n'
        
        output += 'Total: ' + str(self.total)
        return output
    
    def deposit(self, amount, desc = ''):
        self.total += amount
        self.ledger.append({
            'amount': amount,
            'description': desc
        })

    def withdraw(self, amount, desc = ''):
        if not self.check_funds(amount):
            print('Not Enough Funds!')
            return False
        self.total -= amount
        self.spent += amount
        self.ledger.append({
            'amount': -amount,
            'description': desc
        })
        return True

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.total -= amount
        category.deposit(amount, f'Transfer from {self.name}')
        self.ledger.append({
            'amount': -amount,
            'description': f"Transfer to {category.name}"
        })
        return True
    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True
    


def create_spend_chart(categories):
    objs = [{'max_len': 0}]
    total_spent = 0
    for i in categories:
        if len(i.name) > objs[0]['max_len']:
            objs[0]['max_len'] = len(i.name)
        total_spent += i.spent

    for i in categories:
        percent = (i.spent/total_spent) * 100
        objs.append({
            'name': i.name,
            'percent': (percent // 10) * 10
        })

    output = 'Percentage spent by category\n'

    count = 100
    while count >= 0:
        output += f'{count:>{3}}| '
        count -= 10
        for index, i in enumerate(objs):
            # print(i.name)
            if index == 0:
                continue
            output += "o  " if not i['percent'] <= count else '   ' 
        output += '\n'
        if count < 0:
            output += '    ' + '---' * len(categories) + '-\n'
    j = 0
    while j < objs[0]['max_len']:
        output += '     '
        for i in categories:
            try:
                output += i.name[j] + '  '
            except:
                output += '   '
        if j != objs[0]['max_len'] - 1: # to pass the test
            output += '\n'
        j += 1
    return output


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food) 
print(entertainment)
print(business)
print(create_spend_chart([business, food, entertainment]))
