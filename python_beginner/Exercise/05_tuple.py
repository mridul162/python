import statistics
tpl = {"info" : [600, 630, 620], "ril": [1430, 1490, 1567]
       , "mtl": [234, 180, 160]}

op = input("Enter your option (print or add): ")

if op == "print":
    for k, v in tpl.items():
        avg = statistics.mean(v)
        print(f"{k} ==> {v} ==> avg: {round(avg,2)}")

elif op == "add":
    stock = input("Enter stock name: ")
    price = int(input("Enter stock price: "))
    if stock in tpl:
        tpl[stock].append(price)
    else:
        tpl[stock] = [price]
    print(tpl)
