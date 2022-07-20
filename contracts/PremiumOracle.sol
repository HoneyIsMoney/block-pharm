// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract PremiumOracle {
    uint premium;
    uint ONE_TOKEN = 1e6;
    bool validClaim;

    constructor() {
        premium = 5000 * ONE_TOKEN;
        validClaim = false;
    }

    function quotePremium(uint amount, uint startDate, uint endDate) public view returns (uint) {
        return premium;
    }

    function setCanClaim(bool _canClaim) public {
        validClaim = _canClaim;
    }

    function canClaim(uint id) public view returns (bool) {
        return validClaim;
    }
}