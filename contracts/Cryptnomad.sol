//SPDX-License-Identifier: MIT

pragma solidity 0.8.10;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract Cryptnomad is ERC721 {
    uint256 tokenCounter;

    constructor() public ERC721("Cryptnomad", "CRN"){
        tokenCounter = 0;
    }
}