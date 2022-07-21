#!/usr/bin/python3
from brownie import Token, LoggerNFT, InsurancePool, InsurancePool, PremiumOracle, JobManager, InsurancePoolFactory, accounts
from . import helpers
from pprint import pprint as pp
import time

# Accounts
admin = accounts[0]

# Contracts
loggersNFT = LoggerNFT.deploy({'from': admin})
usdc = Token.deploy("Test Token", "TST", 6, 1e6 * 1000000, {'from': admin})
job_manager = JobManager.deploy({'from': admin})
oracle = PremiumOracle.deploy({'from': admin})
pool_factory = InsurancePoolFactory.deploy(
    oracle, job_manager, usdc, {'from': admin})
pool_factory.createPool("UAE_UK Insurance Pool", "UAE_UK", {'from': admin})
poolId = pool_factory.totalPools()
uae_uk_insurance = InsurancePool.at(pool_factory.getPool(poolId))


def main():
    setup_loggersNFT(loggersNFT)
    mint_token(usdc)
    print("===================================================================")
    pp(f"USDC:                  {usdc.address}")
    pp(f"loggersNFT:            {loggersNFT.address}")
    pp(f"UAE_UK Insurance Pool: {uae_uk_insurance.address}")
    pp(f"Oracle:                {oracle.address}")
    print("===================================================================")

    return [usdc, loggersNFT, uae_uk_insurance, oracle]


def setup_loggersNFT(loggersNFT):
    admin = accounts[0]
    loggersNFT.addLogger(accounts[1], admin, {'from': admin})
    loggersNFT.addLogger(accounts[2], admin, {'from': admin})
    loggersNFT.addLogger(accounts[3], admin, {'from': admin})
    loggersNFT.addLogger(accounts[4], admin, {'from': admin})
    loggersNFT.addLogger(accounts[5], admin, {'from': admin})


def mint_token(token):
    token.mint(accounts[6], 1e6 * 1000000, {'from': admin})
    token.mint(accounts[7], 1e6 * 1000000, {'from': admin})
    token.mint(accounts[8], 1e6 * 1000000, {'from': admin})
    token.mint(accounts[9], 1e6 * 1000000, {'from': admin})
