#!/usr/bin/python3
import time
from brownie import *
from web3 import Web3
from . import deploy_test
from pprint import pprint
import pandas as pd

admin = accounts[0]
logger_1 = accounts[1]
logger_2 = accounts[2]

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


def main():
    usdc, loggers, uae_uk_insurance, oracle = deploy_test.main()
    generate_logging_data(loggers, 1, logger_1)
    generate_logging_data(loggers, 2, logger_2)
    get_logger_data(loggers, logger_1)


def generate_logging_data(loggers, id, signer):
    loggers.logData(id, 32, "02435:13463", time.time(), {'from': signer})
    loggers.logData(id, 33, "12535:53263", time.time(), {'from': signer})
    loggers.logData(id, 34, "18435:13463", time.time(), {'from': signer})
    loggers.logData(id, 36, "12535:12463", time.time(), {'from': signer})
    loggers.logData(id, 37, "12435:03483", time.time(), {'from': signer})
    loggers.logData(id, 39, "12435:03463", time.time(), {'from': signer})


# returns a dataframe with the logging data
def get_logger_data(loggers, signer):
    contract = w3.eth.contract(address=loggers.address, abi=loggers.abi)
    filter = contract.events.LogData.createFilter(
        fromBlock=0, argument_filters={'loggerId': 1})
    events = filter.get_all_entries()

    mappedList = map(lambda d: d.args.data, events)

    df = pd.DataFrame(list(mappedList))
    print(df)

    # pprint(list(mappedList)[0][0])
