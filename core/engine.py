import json
from pathlib import Path

RULES_FILE = Path("config/rules.json")
DEFAULT_POLICY = "deny"  # "allow" o "deny"

def load_rules() -> list:
    with RULES_FILE.open("r") as f:
        rules = json.load(f)
    # Ordina per priorità (più basso = più urgente)
    return sorted(rules, key=lambda r: r.get("priority", 99))

def normalize_request(request: dict) -> dict:
    """Normalizza i tipi per evitare type mismatch."""
    normalized = request.copy()
    if "port" in normalized:
        normalized["port"] = int(normalized["port"])
    return normalized

def evaluate_request(request: dict) -> dict:
    rules = load_rules()
    request = normalize_request(request)

    for rule in rules:
        if not rule.get("active", True):
            continue

        rule_type = rule.get("type", "")
        value = rule.get("value")
        reason = rule.get("reason", "no reason specified")

        # Normalizza il valore della regola se è una porta
        if "port" in rule_type:
            value = int(value)

        field_map = {
            "block_ip":   ("ip",   "deny"),
            "allow_ip":   ("ip",   "allow"),
            "block_port": ("port", "deny"),
            "allow_port": ("port", "allow"),
            "block_path": ("path", "deny"),
            "allow_path": ("path", "allow"),
        }

        if rule_type in field_map:
            field, action = field_map[rule_type]
            if request.get(field) == value:
                return {"action": action, "reason": reason, "rule_id": rule.get("id")}

    # Nessuna regola corrisponde → applica policy di default
    return {"action": DEFAULT_POLICY, "reason": "default policy"}
