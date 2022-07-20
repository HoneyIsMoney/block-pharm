// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/token/ERC20/ERC20.sol";
import "./JobManager.sol";
import "./InsurancePool.sol";
import "./PremiumOracle.sol";

contract InsurancePoolFactory  {
    JobManager public jobManager;
    PremiumOracle public premiumOracle;
    ERC20 public usdc;
    uint public totalPools;
    mapping(uint => InsurancePool) pools;

    event PoolCreated(uint poolId);

    constructor(JobManager manager, PremiumOracle oracle, ERC20 stableCoin) public {
            jobManager = manager;
            premiumOracle = oracle;
            usdc = stableCoin;
    }

    function createPool(string memory name, string memory symbol) public returns (InsurancePool pool) {
        totalPools ++;
        uint poolId = totalPools;
        pool = new InsurancePool(name, symbol, usdc, premiumOracle, jobManager);
        pools[poolId] = pool;

        emit PoolCreated(poolId);
        return pool;
    }

    function getPool(uint poolId) public view returns (InsurancePool pool) {
        pool = pools[poolId];
        return pool;
    }

}