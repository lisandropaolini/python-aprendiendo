checkingAccount = 500
savingsAccount = 1000

# add 100 to our savings (Yeah!)
savingsAccount = savingsAccount + 100

# remove 50 from our checkingaccount (Sniff)
checkingAccount = checkingAccount - 50

# calculate the number of days to save to reach 5000
numberDaysSave = (5000 - checkingAccount) / 500

# update our checkingaccount (again) after the daily gains/losses
checkingAccount = checkingAccount + (30 - 10) * 7

print(savingsAccount % 500) # -> 100
# 1100 = 500 * 2 + 100, so 1100 % 500 = remainder = 100

print(9 ** 3) # -> 729, 9*9*9 = 729

print(savingsAccount // 500) # -> 2
# 1100 = 500 * 2 + 100, so 1100 // 500 = integer division result = 2*
