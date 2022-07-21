from brownie import accounts
import pandas as pd
import time
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


def setup_pool(pool_factory, pool_name, pool_symbol, admin):
    pool_factory.createPool(pool_name, pool_symbol, {'from': admin})
    poolId = pool_factory.totalPools()
    pool = pool_factory.getPool(poolId)
    return pool


def generate_logging_data(loggersNFT, id, signer):
    loggersNFT.logData(id, 32, "02435:13463", time.time(), {'from': signer})
    loggersNFT.logData(id, 33, "12535:53263", time.time(), {'from': signer})
    loggersNFT.logData(id, 34, "18435:13463", time.time(), {'from': signer})
    loggersNFT.logData(id, 36, "12535:12463", time.time(), {'from': signer})
    loggersNFT.logData(id, 37, "12435:03483", time.time(), {'from': signer})
    loggersNFT.logData(id, 39, "12435:03463", time.time(), {'from': signer})


def get_logger_data(loggersNFT, id):
    # brownie is using an old version of the web3 library so we create
    # a new instance of the web3 library and contract
    contract = w3.eth.contract(address=loggersNFT.address, abi=loggersNFT.abi)

    # get the events from the contract
    filter = contract.events.LogData.createFilter(
        fromBlock=0, argument_filters={'loggerId': id})
    events = filter.get_all_entries()

    # create a dataframe from the events
    mappedList = map(lambda d: d.args.data, events)
    df = pd.DataFrame(list(mappedList), columns=['temp', 'gps', 'timestamp'])
    return df


def token_balance(token, account):
    unscaled_balance = token.balanceOf(account)
    decimals = token.decimals()
    return unscaled_balance / 10 ** decimals


def add_liquidity_insurance(pool, stablecoin, amount, account):
    stablecoin.approve(pool, amount, {'from': account})
    pool.deposit(amount, account, {'from': account})
    return pool.balanceOf(account)
