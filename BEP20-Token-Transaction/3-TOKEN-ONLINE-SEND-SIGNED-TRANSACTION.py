from web3 import Web3
import os
import sys
import ast

print("-------------")
print("Connecting...")

bsc = "https://bsc-dataseed1.binance.org:443"
web3 = Web3(Web3.HTTPProvider(bsc))

if (web3.isConnected()) == False:
    print("Not connected!")
else:
    print("Connected")

def sendSignedTransaction():
    tx = open(os.path.join(sys.path[0], "SignedTokenTransaction.txt"), "r")
    tx_hash = web3.eth.sendRawTransaction(ast.literal_eval(tx.read()))
    trans = web3.toHex(tx_hash)
    transaction = web3.eth.get_transaction(trans)
    print("Transaction:")
    print(transaction)
    print("DONE! Signed transaction has been sent to the blockchain.")

if __name__ == '__main__':
    try:
        sendSignedTransaction()
    except Exception as e:
        print(e)




