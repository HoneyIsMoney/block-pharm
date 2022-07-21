#!/usr/bin/python3

from brownie import Token, LoggerNFT, InsurancePool, InsurancePool, PremiumOracle, JobManager, InsurancePoolFactory, accounts

MILLION = 1e6 * 1000000

admin = accounts[0]
logger_1 = accounts[1]
logger_2 = accounts[2]


def main():
    usdc, loggers, uae_uk_insurance, oracle = deploy_contracts()
    setup_loggers(loggers)
    print("============================================================================")
    print("USDC:                 ", usdc.address)
    print("Loggers:              ", loggers.address)
    print("UAE_UK Insurance Pool:", uae_uk_insurance.address)
    print("Oracle:               ", oracle.address)
    print("============================================================================")

    return [usdc, loggers, uae_uk_insurance, oracle]


def deploy_contracts():
    loggers = LoggerNFT.deploy({'from': admin})
    usdc = Token.deploy("Test Token", "TST", 6, MILLION, {'from': admin})
    job_manager = JobManager.deploy({'from': admin})
    oracle = PremiumOracle.deploy({'from': admin})
    pool_factory = InsurancePoolFactory.deploy(
        oracle, job_manager, usdc, {'from': admin})

    pool_factory.createPool("UAE_UK Insurance Pool", "UAE_UK", {'from': admin})
    poolId = pool_factory.totalPools()
    uae_uk_insurance = InsurancePool.at(pool_factory.getPool(poolId))
    return [usdc, loggers, uae_uk_insurance, oracle]


def setup_loggers(loggers):
    loggers.addLogger(logger_1, admin, {'from': admin})
    loggers.addLogger(logger_2, admin, {'from': admin})
