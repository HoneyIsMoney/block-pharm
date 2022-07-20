#!/usr/bin/python3

from brownie import Token, LoggerNFT, InsurancePool, InsurancePool, PremiumOracle, JobManager, InsurancePoolFactory, accounts

from . import deploy_test

admin = accounts[0]
logger_1 = accounts[1]
logger_2 = accounts[2]


def main():
    usdc, loggers, uae_uk_insurance, oracle = deploy_test.main()
    print("\n============================================================================")
    print("inside simulate")
    print("USDC:                 ", usdc.address)
    print("============================================================================")
