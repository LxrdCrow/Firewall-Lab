# Firewall-Lab

A modular, application-level firewall simulation built in Python and Flask.  
Firewall-Lab demonstrates core concepts of request filtering, rule management,
and logging for educational and portfolio purposes.

---

## Overview

This project simulates a firewall environment where HTTP requests are analyzed
and either allowed or blocked based on configurable rules. The system is designed
to be modular and easy to extend with additional security features.

---

## Repository Structure

```
Firewall-lab/
├── api/
│   └── routes.py        ← Flask Blueprint (endpoints)
├── config/
│   └── rules.json       ← rule configuration
├── core/
│   └── engine.py        ← rule evaluation logic
├── models/
│   └── filter.py        ← dataclasses (FirewallRule, FirewallRequest)
├── services/
│   └── logger.py        ← request logging
├── storage/             ← reserved for future persistence (SQLite)
├── docs/                ← reserved for future documentation
├── tests/
│   └── test_engine.py   ← pytest test suite
├── app.py               ← Flask app factory
├── main.py              ← entrypoint
└── requirements.txt
```

---

## Features

- Core rule engine for request filtering (allow/deny)
- Priority-based rule evaluation
- JSON-based rule configuration
- Flask REST API to manage rules and simulate requests
- Request logging via Python logging module
- Modular design for future SQLite integration and dashboard

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/simulate` | Simulate a firewall request |
| GET | `/rules` | List all active rules |
| POST | `/rules` | Add a new rule |

---

## Tech Stack

- Python 3.11+
- Flask
- JSON (rule storage)
- SQLite (planned)
- Pytest
- Python-dotenv

---

## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

---

## Educational Purpose

This project is built for learning and portfolio purposes.  
It demonstrates application-level firewall concepts and Python backend
development practices including modular design, REST APIs, and logging.
```

