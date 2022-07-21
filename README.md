# Block Pharm Contracts

## Installation

1. `pipx install eth-brownie`                                       // Install the brownie package
2. `npm i -g ganache-cli `                                          // Install local blockchain
3. `python3 -m venv venv`                                           // Create a virtual environment
4. `source venv/bin/activate`                                       // Activate the virtual environment
5. `pip3 install -r requirements.txt`                               // Install project dependencies
6. `brownie pm install OpenZeppelin/openzeppelin-contracts@4.7.1 `  // Install the OpenZeppelin contracts library

# workflow
1. create a script in the `/scripts` directory
2. run the script with `brownie run scripts/<script> --silent`