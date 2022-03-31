from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import network, Cryptnomad
import pytest
from scripts.deploy_and_mint import deploy, mint

def test_can_deploy_and_mint_nomads():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    nomad_contract = deploy()
    last_creation_tx = mint(20)

    # Assert
    assert nomad_contract.tokenIds() == 20