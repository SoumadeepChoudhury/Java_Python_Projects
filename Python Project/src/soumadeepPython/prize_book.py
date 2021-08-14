# Accept prize of book. There is 10% discount and 5% sales tax, display net prize.

prize = float(input("Enter prize of book: "))
net_prize = prize-(10.0/100*prize)
net_prize = net_prize+(5.0/100*net_prize)
print("Net Prize", net_prize)
