#!/usr/bin/python3
from brownie import *
from . import deploy_contracts, helpers
from pprint import pprint as pp


# Contracts
usdc, loggers, insurance, oracle = deploy_contracts.main()

# Signing keys
admin = accounts[0]
device_1 = accounts[1]
device_2 = accounts[2]
harun = accounts[6]
usama = accounts[7]
raj = accounts[8]
customer = accounts[9]


def main():
    # Generate some mock logging data on the contract
    helpers.generate_logging_data(loggers, 1, device_1)
    helpers.generate_logging_data(loggers, 2, device_2)

    # Get the data from the contract as a pandas dataframe
    device_1_data = helpers.get_logger_data(loggers, 1)
    device_2_data = helpers.get_logger_data(loggers, 2)

    # Print the data
    print('\nDevice 1 data:')
    pp(device_1_data)

    print(f'\nAdmin USDC balance:    ${helpers.token_balance(usdc, admin)}')
    print(f'harun USDC balance:    ${helpers.token_balance(usdc, harun)}')
    print(f'usama USDC balance:    ${helpers.token_balance(usdc, usama)}')
    print(f'raj USDC balance:      ${helpers.token_balance(usdc, raj)}')
    print(f'harun Pool-LP balance: ${helpers.token_balance(insurance, harun)}')
    print(f'Pool USDC balance:     ${helpers.token_balance(usdc, insurance)}')

    print("\n--------------------------------------------")
    print(f'Harun Depositing USDC into Insurance Pool...')
    print("--------------------------------------------")

    helpers.add_liquidity_insurance(insurance, usdc, 1e6 * 250000, harun)
    print(f'Harun USDC balance:    ${helpers.token_balance(usdc, harun)}')
    print(f'Harun Pool-LP balance: ${helpers.token_balance(insurance, harun)}')
    print(f'Pool USDC balance:     ${helpers.token_balance(usdc, insurance)}')

    print("\n--------------------------------------------")
    print(f'Usama Depositing USDC into Insurance Pool...')
    print("--------------------------------------------")

    helpers.add_liquidity_insurance(insurance, usdc, 1e6 * 250000, usama)
    print(f'Usama USDC balance:    ${helpers.token_balance(usdc, usama)}')
    print(f'Usama Pool-LP balance: ${helpers.token_balance(insurance, usama)}')
    print(f'Pool USDC balance:     ${helpers.token_balance(usdc, insurance)}')

    print("\n--------------------------------------------")
    print(f'Raj Depositing USDC into Insurance Pool...')
    print("--------------------------------------------")

    helpers.add_liquidity_insurance(insurance, usdc, 1e6 * 500000, raj)
    print(f'Raj USDC balance:      ${helpers.token_balance(usdc, raj)}')
    print(f'Raj Pool-LP balance:   ${helpers.token_balance(insurance, raj)}')
    print(f'Pool USDC balance:     ${helpers.token_balance(usdc, insurance)}')
    print("--------------------------------------------\n")

    print("\n\n\n--------------------------------------------")
    print("get insurance quote")
