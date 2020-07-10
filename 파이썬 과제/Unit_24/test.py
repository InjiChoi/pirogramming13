price = map(int, input().split(';'))
prices = list(price)
prices.sort(reverse=True)
for i in range(len(prices)):
    print('{0:>9,}'.format(prices[i]))
