from scripts.helpful_scripts import (
    get_account, 
    OPENSEA_URL)
from brownie import (
    Cryptnomad, 
    config, 
    network
    )

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def deploy():
    account = get_account()
    nomad_contract = Cryptnomad.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False))
    print("New token has been created")
    return nomad_contract

def mint(number = 1):
    account = get_account()
    contract = Cryptnomad[-1]
    for i in range(number):
        tx = contract.mintNomad(sample_token_uri)
        tx.wait(1)
    return tx



def main():
    deploy()
    mint()