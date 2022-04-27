[![Python WEB3 Binance Smart Chain BEP20 - True Cold Wallet](https://github.com/Crusader93/BEP20-Cold-Wallet-Transactions/blob/master/1.jpg)](https://www.youtube.com/watch?v=P1CTAX8fb2E)<br/>
<br/>
Cold Wallet for Binance Smart Chain BEP20<br/>
Do not forget that the minimum gas fee on the BSC is 5 GWEI or 0.000105 BNB and 10 GWEI or 0.00021 BNB on the BSC - Testnet<br/>
<br/>
Use https://bscscan.com for BSC<br/>
Use https://testnet.bscscan.com for BSC-Testnet<br/>
<br/>
bsc url: https://bsc-dataseed1.binance.org:443<br/>
bsc testnet url: https://data-seed-prebsc-1-s1.binance.org:8545/<br/>
<br/>
How it works:<br/>
We will create a unsigned transaction on a device with Internet access, then we will sign this transaction with a private key on a device without Internet access, then we will export this signed transaction to the our online device and send transaction to the blockchain.<br/>
Thus, no one will ever know our private key or seed phrase.<br/>
<br/>
This is an ideal way to store stablecoins USDT, BUSD or other on a blockchain where transfer fees are low (0.000105 BNB now - 5 GWEI). The method is suitable for you if you do not like bitcoin and its unstable price.<br/>
<br/>
Requirements:<br/>
1. Smartphone or PC that will never connect to the Internet again.<br/>
2. 2nd PC or smartphone with internet access.<br/>
3. Pre-installed Metamask or Mnemonic Code Converter BIP39 on the device without internet access.<br/>
<br/>
Instructions:<br/>
<br/>
1. Install Python on your two devices.<br/>
2. Install the 'web3' packages for Python https://pypi.org/project/web3/<br/>
3. Create a Metamask wallet on an offline device without Internet or use html from Mnemonic Code Converter BIP39 (https://github.com/iancoleman/bip39)<br/>
4. Export the private key for account_1 (private_key) to the script on offline device '2-BNB-OFFLINE-SIGN-TRANSACTION.py'<br/>
5. Set wallet addresses in '1-BNB-ONLINE-CREATE-TRANSACTION.py' script - account_1 and account_2<br/>
6. Enter BNB amount - amount<br/>
7. If you want to send a tokens, use the scripts from the 'BEP20-Token-Transaction' folder. The sequencing is the same, but don't forget to enter contract_adress and contract abi (abi1) in the '1-TOKEN-ONLINE-CREATE-TRANSACTION.py' script<br/>
8. Create a transaction on a device with Internet access, run the script '1-BNB-ONLINE-CREATE-TRANSACTION.py'<br/>
9. Copy the unsigned transaction 'UnsignedTransaction.txt'<br/>
10. Paste 'UnsignedTransaction.txt' to the offline device<br/>
11. Run the script '2-BNB-OFFLINE-SIGN-TRANSACTION.py' on an offline device<br/>
12. Copy the signed transaction 'SignedTransaction.txt'<br/>
13. Paste 'SignedTransaction.txt' to the online device<br/>
14. Run the script '3-BNB-ONLINE-SEND-TRANSACTION.py' on an online device<br/>
15. DONE! Your signed transaction has been sent to the blockchain.<br/>
<br/>
You can support me (Binance Smart Chain Network): 0x4d213Eaf37a179Bc4473532e84C8b553137C0F8f

