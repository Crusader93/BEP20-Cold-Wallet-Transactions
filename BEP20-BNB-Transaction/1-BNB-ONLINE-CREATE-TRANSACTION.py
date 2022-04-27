from web3 import Web3
import sys
import os

print("-------------")
print("Connecting...")

bsc = "https://bsc-dataseed1.binance.org:443"
web3 = Web3(Web3.HTTPProvider(bsc))

if (web3.isConnected()) == False:
    print("Not connected!")
else:
    print("Connected")

k = 1000000000
eth = 1000000000000000000

account_1 = "" # from adress
account_2 = "" # to adress

amount = 0.000054 # BNB amount for transaction

checkAmount = amount
amount = int(amount * eth)

def createTransaction():
    global amount

    balance = web3.eth.get_balance(account_1)
    humanReadable = balance/eth # converting
    print("Balance: " + str(humanReadable))
    if humanReadable > 0.000105: # min BNB tax - 5 GWEI

        gas = 21000 # gasLimit
        gwei = 5 # gasPrice in gwei
        wei = gwei * k # calculated gasPrice in wei
        
        if gwei < 5:
            print("gasPrice cant be less than 5 GWEI")
            sys.exit()

        calcAmount = balance - (wei*gas) # calculated amount with network tax
        tax = (balance-calcAmount)/eth # tax

        if checkAmount == humanReadable: # Transfer the entire balance of the wallet if the user sets the amount equal to the balance of the wallet
            gwei = 5
            wei = gwei * k
            amount = balance - (wei*gas)

        elif amount > calcAmount:
            print("Not enough funds. Too much gas price: " + str(tax))
            print("Maximum allowed amount is " + str(calcAmount/eth))
            sys.exit()

        nonce = web3.eth.getTransactionCount(account_1)

        transaction = {
        'nonce': nonce,
        'to': account_2,
        'value': int(amount),
        'gas': gas,
        'gasPrice': int(wei)
        }

        with open(os.path.join(sys.path[0], "UnsignedTransaction.txt"), "w+") as tx:
            tx.write(str(transaction))
            tx.close()

        print("Transaction:")
        print(transaction)
        print("Unsigned transaction was saved to the UnsignedTransaction.txt file")
    else:
        print("The balance is less than the minimum network tax 0.000105 BNB")

if __name__ == '__main__':
    try:
        createTransaction()
    except Exception as e:
        print(e)




