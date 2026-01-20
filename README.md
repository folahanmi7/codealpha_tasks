# Python Cybersecurity Projects  
## Network Sniffer & Secure Coding Review

This repository contains **two beginner-to-intermediate cybersecurity projects** implemented in Python.  
The projects focus on **network traffic analysis** and **secure coding practices**, demonstrating both offensive awareness and defensive programming techniques.

# 🔹 Project 1: Basic Network Sniffer in Python

## Overview
A beginner-friendly project that demonstrates how to build a **simple network packet sniffer** using Python and **Scapy**.  
It helps in understanding how network traffic flows and how packets can be inspected in real time.

## Objectives
- Understand what a **network sniffer** is
- Capture live network packets
- Extract **source and destination IP addresses**
- Identify **transport layer protocols** (TCP / UDP / Others)
- Practice Python using **Scapy**

## Features
- Captures live packets from the network interface
- Displays:
  - Source IP address
  - Destination IP address
  - Protocol type (TCP / UDP)
- Beginner-friendly and well-structured logic

## Tools & Technologies
| Item | Description |
|-----|------------|
| Language | Python 3 |
| Library | Scapy |
| OS | Windows|


## Requirements
Install Scapy before running the sniffer:

## Learning Outcome
- Practical exposure to packet-level networking
- Understanding of IP and transport-layer protocols
- Introduction to network traffic analysis

# 🔹 Project 2: Secure Coding Review Using Bandit

## Overview
This project focuses on **static code analysis** of a Python application using **Bandit**, a security linting tool.  
The aim is to identify insecure coding practices, document vulnerabilities, and apply secure remediation techniques.

The project follows a **before-and-after** security review approach.

## Objectives
- Perform static security analysis on Python code
- Identify common vulnerabilities
- Understand security risks in application code
- Apply secure coding best practices
- Validate fixes using Bandit

## Tools & Technologies
| Item | Description |
|-----|------------|
| Language | Python |
| Security Tool | Bandit |
| IDE | Visual Studio Code |
| OS | Windows |

## Vulnerability Identified
- **Type:** SQL Injection  
- **Bandit Rule:** B608 – Hardcoded SQL Expressions  
- **Severity:** Medium  
- **CWE:** CWE-89

### Vulnerable Code Example
```python
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)
```

## Remediation Applied
- Replaced string-based SQL queries with **parameterized queries**
- Prevented direct user input injection

### Secure Code Example
```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

## Bandit Scan Results

| File | Result |
|-----|-------|
| app.py | 1 Medium severity issue found |
| fixedapp.py | No issues detected |

This confirms successful remediation of the vulnerability.

## Secure Coding Best Practices Followed
- Use parameterized SQL queries
- Avoid hardcoded SQL expressions
- Validate and sanitize user input
- Run static analysis during development
- Follow the principle of least privilege

## Conclusion
These projects collectively demonstrate core cybersecurity skills:
- **Network-level visibility** through packet sniffing
- **Application-level security** through static code analysis
