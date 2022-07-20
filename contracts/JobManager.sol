// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract JobManager {
    uint nextId;

    constructor() {
        nextId = 0;
    }

    function selectLogger() public returns (uint) {
        nextId ++;
        return nextId;
    }
}