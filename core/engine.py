from pathlib import Path
from models.filter import FirewallRule, FirewallRequest
from services.logger import log_request
import json

RULES_FILE = Path("config/rules.json")
DEFAULT_POLICY = "deny"

def load_rules() -> list[FirewallRule]:
    with RULES_FILE.open("r") as f:
        rules = json.load(f)
    return sorted(
        [FirewallRule.from_dict(r) for r in rules],
        key=lambda r: r.priority
    )

def evaluate_request(request: FirewallRequest) -> dict:
    rules = load_rules()

    for rule in rules:
        if not rule.active:
            continue

        rule_type = rule.type
        value = rule.value
        reason = rule.reason

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
            if getattr(request, field) == value:
                result = {"action": action, "reason": reason, "rule_id": rule.id}
                log_request(request, result)
                return result

    result = {"action": DEFAULT_POLICY, "reason": "default policy"}
    log_request(request, result)
    return result

def save_rule(rule: FirewallRule):
    rules = load_rules()
    rules.append(rule.to_dict())
    with RULES_FILE.open("w") as f:
        json.dump(rules, f, indent=2)
