//SPDX-License-Identifier: MIT

pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract Cryptnomad is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter public tokenIds;
    uint256 MAX_NOMADS;


    constructor() ERC721("Cryptnomad", "NOM"){}

    function withdraw() public onlyOwner {
        uint balance = address(this).balance;
        payable(msg.sender).transfer(balance);
    }



    function reserveNomads() public onlyOwner{
        //uint supply = totalSu
    }

    function mintNomad(string memory tokenURI) public payable {
        tokenIds.increment();
        uint256 nomadId = tokenIds.current();
        _mint(msg.sender, nomadId);
    }
}