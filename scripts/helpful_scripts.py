from brownie import (
    accounts, 
    config, 
    network
)


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local', 'mainnet-fork', 'local-ganache']
FORKED_LOCAL_ENVIRONMENTS = ['mainnet-fork', 'mainnet-fork']
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

coin_mapping = {0:"BTC", 1: "ETH", 2: "USDC"}


DECIMALS = 8
STARTING_PRICE = 400000000000

def get_account(index=0, id=None):
    if index:
        return accounts[index]
    if id:
        accounts.load(id)

    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
   

    return accounts.add(config["wallets"]["from_key"])
