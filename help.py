portfolio = [('AAPL',5, 140),('FB',3, 330)]

for i in portfolio:
    sum_value = 0
    stocks  = list (i)
    item_value = stocks[1] * stocks[2]
    print(sum([sum_value,item_value]))