from web3 import Web3
import os
import sys
import ast

print("-------------")

bsc = "https://"
web3 = Web3(Web3.HTTPProvider(bsc))

private_key = "" # account_1 private key

def signTx():
        tx = open(os.path.join(sys.path[0], "UnsignedTransaction.txt"), "r")
        signed_tx = web3.eth.account.signTransaction(ast.literal_eval(tx.read()),private_key)

        with open(os.path.join(sys.path[0], "SignedTransaction.txt"), "w+") as f:
            f.write(str(signed_tx.rawTransaction))
            f.close()

        print("Transaction:")
        print(signed_tx.rawTransaction)
        print("Signed transaction was saved to the SignedTransaction.txt file")
        print("Never turn on the Internet on this device!")
if __name__ == '__main__':
    try:
        signTx()
    except Exception as e:
        print(e)
        pass