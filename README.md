# Firewall Simulation
<br>

---

## Project Presentation
<br>

A modular, application-level firewall simulation built in Python and Flask.  
Firewall-Lab demonstrates core concepts of request filtering, rule management, logging, and basic threat detection for educational and portfolio purposes.

<br>

## Overview


This project simulates a firewall environment where requests are analyzed and either allowed or blocked based on user-defined rules.  
The system is designed to be modular, scalable, and easy to extend with additional security features.


---

### Repository
<br>

[ Structure ]

---

## Features

- Core rule engine for request filtering (allow/deny)
- JSON-based rule configuration for quick testing
- Flask API to manage rules and simulate requests
- Logging of blocked and allowed requests
- Modular design for future integration with SQLite and dashboards

---


## Tech Stack

- Python 3.11+
- Flask
- JSON for rule storage
- SQLite (planned for persistence in later versions)
- Pytest for testing
- Python-dotenv for environment configuration