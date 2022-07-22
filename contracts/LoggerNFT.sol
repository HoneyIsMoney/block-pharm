// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/token/ERC721/ERC721.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/access/Ownable.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/utils/Counters.sol";

contract LoggerNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;
    mapping(address => uint) public loggers;
    mapping(uint => uint) private lastTimestamp;

    struct Data {
        uint256 temprature;
        string gps;
        uint timestamp;
    }

    event LogData(uint loggerId, Data data);
    event LoggerAdded(address logger, uint loggerId);

    constructor() ERC721("BlockPharm Logger", "LOGGER") {}

    // -------------------- functions -------------------
    function addLogger(address logger, address owner) external onlyOwner {
        _tokenIdCounter.increment();
        uint256 loggerId = _tokenIdCounter.current();
        loggers[logger] = loggerId;
        _safeMint(owner, loggerId);

        emit LoggerAdded(logger, loggerId);
    }

    function logData(
        uint loggerId,
        uint temp,
        string calldata gps,
        uint timestamp
    ) external {
        require(loggers[msg.sender] == loggerId, "You are not the logger");
        lastTimestamp[loggerId] = timestamp;
        emit LogData(loggerId, Data(temp, gps, timestamp));
    }

    function numOfLoggers() external view returns (uint) {
        return _tokenIdCounter.current();
    }

    function timestamp(uint loggerId) external view returns (uint) {
        return lastTimestamp[loggerId];
    }
}
