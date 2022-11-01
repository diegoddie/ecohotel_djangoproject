from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/bd1b4d3eed144ebb8f4ea4756f0ba58e"))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(address)
print(privateKey)
