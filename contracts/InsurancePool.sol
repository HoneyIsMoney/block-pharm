// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/token/ERC20/extensions/ERC4626.sol";
import "OpenZeppelin/openzeppelin-contracts@4.7.1/contracts/token/ERC20/ERC20.sol";
import "./JobManager.sol";
import "./PremiumOracle.sol";

contract InsurancePool is ERC4626 {

    PremiumOracle public premiumOracle;
    JobManager public jobManager;
    ERC20 public usdc;
    uint public totalJobs;
    mapping(uint => JobData) public jobs;
    mapping(uint => address) public insuranceCertificates;

    enum JobStatus {
        IN_PROGRESS,
        COMPLETED,
        CLAIMED
    }

    struct JobData {
        address owner;
        uint price;
        uint cover;
        uint startDate;
        uint endDate;
        uint loggerId;
        JobStatus status ;
    }

    event InsurancePurchaced(uint jobId);
    event InsuranceClaimed(uint jobId);

    constructor(
        string memory name, 
        string memory symbol, 
        ERC20 stableCoin, 
        PremiumOracle oracle, 
        JobManager manager
        ) ERC4626(IERC20Metadata(stableCoin)) ERC20(name, symbol) {
            premiumOracle = oracle;
            jobManager = manager;
        }

    function quote(uint amount, uint startDate, uint endDate) public view returns (uint) {
        return premiumOracle.quotePremium(amount, startDate, endDate);
    }

    function buyPremium(uint cover, uint startDate, uint endDate) public returns (uint jobId) {
        uint price = premiumOracle.quotePremium(cover, startDate, endDate);
        require(usdc.balanceOf(msg.sender) >= price, "Not enough USDC");
        require(usdc.allowance(msg.sender, address(this)) >= price, "Not enough allowance");
        usdc.transferFrom(msg.sender, address(this), price);
        
        uint loggerId = jobManager.selectLogger();
        jobId = totalJobs ++;

        jobs[jobId] = JobData(msg.sender, price, cover, startDate, endDate, loggerId, JobStatus.IN_PROGRESS);
        insuranceCertificates[jobId] = msg.sender;
        emit InsurancePurchaced(jobId);
    }

    function claim(uint jobId) public {
        require(insuranceCertificates[jobId] == msg.sender, "You are not the owner of this Certificate");
        require(premiumOracle.canClaim(jobId) == true, "Job is not claimable");
        jobs[jobId].status = JobStatus.CLAIMED;
        usdc.transfer(msg.sender, jobs[jobId].cover);
        emit InsuranceClaimed(jobId);
    }
}
