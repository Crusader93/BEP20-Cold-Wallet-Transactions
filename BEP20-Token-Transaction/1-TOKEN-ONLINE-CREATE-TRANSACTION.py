from web3 import Web3
import json
import sys
import os
import sys

print("-------------")
print("Connecting...")

bsc = "https://bsc-dataseed1.binance.org:443"
web3 = Web3(Web3.HTTPProvider(bsc))

if (web3.isConnected()) == True:
    print("CONNECTED")
else:
    print("NOT CONNECTED!")    

# abi1 = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
# contract_address = "0xeD24FC36d5Ee211Ea25A80239Fb8C4Cfd80f12Ee"

abi1 = json.loads('') # contract abi
contract_address = "" # contract address

account_1 = "" # from
account_2 = "" # to

contract = web3.eth.contract(address=contract_address, abi=abi1)

k = 1000000000
eth = 1000000000000000000

amount = 0.25 # account_1 token amount for transaction
amount = int(amount * eth) # converting

def myfunc():
    balance = web3.eth.get_balance(account_1)
    balanceOf = contract.functions.balanceOf(account_1).call() # token balance
    balanceOf = balanceOf/eth # converting
    print("Token balance: " + str(balanceOf))

    if balanceOf <= amount/eth:
        print("Error: token balance <= amount tokens")
        sys.exit()

    humanReadable = balance/eth # converting
    print("Balance: " + str(humanReadable))

    if humanReadable > 0.000105: # min BNB tax 5 GWEI
        
        gas = 50000 # gasLimit, set 60000-100000 if the transaction does not work, but then the minimum balance should be 0.0005 BNB. k = 1000000000, eth = 1000000000000000000, balance = 0.0005 * eth, gwei = 5 gas = 100000, wei = gwei * 1000000000, value = balance - (wei*gas), value must be > 0
        gwei = 5 # gasPrice in gwei
        wei = gwei * k # calculated gasPrice in wei
        summ = balance - (wei*gas)

        if gwei < 5:
            print("gasPrice cant be less than 5 GWEI")
            sys.exit()

        if summ <= 0:
            allowedGas = balance/wei
            print("Too much gasLimit, you need gasLimit less than: " + str(allowedGas))
            sys.exit()

        nonce = web3.eth.getTransactionCount(account_1)
        
        transaction = contract.functions.transfer(account_2, amount).buildTransaction({
        'chainId': 56,
        'from': account_1,
        'nonce': nonce,
        'gas': gas,
        'gasPrice': int(wei)
        })

        with open(os.path.join(sys.path[0], "UnsignedTokenTransaction.txt"), "w+") as tx:
            tx.write(str(transaction))
            tx.close()

        print("Transaction:")
        print(transaction)
        print("Unsigned transaction was saved to the UnsignedTokenTransaction.txt file")
    else:
        print("The balance is less than the minimum network tax 0.000105 BNB")

if __name__ == '__main__':
    try:
        myfunc()
    except Exception as e:
        print(e)








