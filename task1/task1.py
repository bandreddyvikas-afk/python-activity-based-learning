balance = 5000.0
withdrawal_limit = 2000.0

deposit_count = 0
withdrawal_count = 0
rejected_count = 0

# Each nested list stores transaction details
transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    print("\nTransaction", i + 1)
    transaction_type = input("Enter D for deposit or W for withdrawal: ").upper()
    amount = float(input("Enter amount: "))

    if amount <= 0:
        status = "Rejected - Invalid amount"
        rejected_count += 1

    elif transaction_type == "D":
        balance += amount
        deposit_count += 1
        status = "Deposit successful"

    elif transaction_type == "W":
        if amount > withdrawal_limit:
            status = "Rejected - Limit exceeded"
            rejected_count += 1
        elif amount > balance:
            status = "Rejected - Insufficient balance"
            rejected_count += 1
        else:
            balance -= amount
            withdrawal_count += 1
            status = "Withdrawal successful"

    else:
        status = "Rejected - Invalid transaction type"
        rejected_count += 1

    transactions.append(
        [transaction_type, amount, status, balance]
    )

print("\n========== TRANSACTION SUMMARY ==========")
print("Initial balance: Rs. 5000.00")
print("Successful deposits:", deposit_count)
print("Successful withdrawals:", withdrawal_count)
print("Rejected transactions:", rejected_count)

print("\nTransaction details:")
for transaction in transactions:
    transaction_type, amount, status, current_balance = transaction
    print(transaction_type, amount, status,
          "Balance:", round(current_balance, 2))

print("\nFinal balance: Rs.", round(balance, 2))
print("=========================================")
