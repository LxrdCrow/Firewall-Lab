import json
from pathlib import Path

RULES_FILE = Path("config/rules.json")
RULES = json.loads(RULES_FILE.read_text())

