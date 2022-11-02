from web3 import Web3
import os

ADDRESS = "0xEcE60DE075DeAe8335a12caAE638935FBB2Eb3fb"
P_KEY = os.environ.get("P_KEY")

def sendTransactionAndGetTxId(message):
    w3 = Web3(Web3.HTTPProvider("https://goerli.infura.io/v3/bd1b4d3eed144ebb8f4ea4756f0ba58e"))
    address = ADDRESS
    privateKey = P_KEY
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, "Ether")
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to="0x0000000000000000000000000000000000000000",
        value=value,
        data=message.encode("utf-8")
    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    receipt = w3.eth.waitForTransactionReceipt(txId)
    print(receipt['status'])
    return txId


    