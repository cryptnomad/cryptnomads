//SPDX-License-Identifier: MIT

pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Cryptnomad is ERC721, Ownable {
    uint256 tokenCounter;
    uint256 MAX_NOMADS;


    constructor() public ERC721("Cryptnomad", "NOM"){
        tokenCounter = 0;
    }

    function withdraw() public onlyOwner {
        uint balance = address(this).balance;
        msg.sender.transfer(balance);
    }

    function reserveNomads() public onlyOwner{
        //uint supply = totalSu
    }

    function mintNomad(uint numberOfTokens) public payable {

    }
}