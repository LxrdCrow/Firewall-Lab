from unittest.mock import patch

from core.engine import evaluate_request
from models.filter import FirewallRule, FirewallRequest


def make_request(
        ip="192.168.1.10",
        port=80,
        protocol="TCP",
        path="/",
        method="GET",
):
    """ Helper function to make a request """
    return FirewallRequest(
        ip=ip,
        port=port,
        protocol=protocol,
        path=path,
        method=method,)

def make_rule(
        id_=1,
        type_="block_ip",
        value="192.168.1.10",
        reason="test",
        active=True,
        priority=10,
):
    """ Helper for creating a firewall rule without repeat always in all fields """
    return FirewallRule(id=id_, type=type_, value=value, reason=reason, active=active, priority=priority)


# --- TEST IP ---

@patch("core.engine.load_rules")
def test_block_ip(mock_load_rules):
    """ blocked IP -> deny """
    mock_load_rules.return_value = [ make_rule(type_="block_ip", value="192.168.1.10") ]

    result = evaluate_request(make_request(ip="192.168.1.10"))

    assert result["action"] == "deny"
    assert result["rule_id"] == 1

@patch("core.engine.load_rules")
def test_allow_ip(mock_load_rules):
    """ IP in whitelist -> allow """
    mock_load_rules.return_value = [make_rule(type_="allow_ip", value="192.168.1.1")]

    result = evaluate_request(make_request(ip="192.168.1.1"))
    assert result["action"] == "allow"


# --- TEST PORT ---

@patch("core.engine.load_rules")
def test_block_port(mock_load_rules):
    """ Block port -> deny """
    mock_load_rules.return_value = [ make_rule(type_="block_port", value="22") ]

    result = evaluate_request(make_request(port=22))

    assert result["action"] == "deny"


# --- TEST PATH ---

@patch("core.engine.load_rules")
def test_block_path(mock_load_rules):
    """ Block path -> deny """
    mock_load_rules.return_value = [ make_rule(type_="block_path", value="/admin") ]

    result = evaluate_request(make_request(path="/admin"))
    assert result["action"] == "deny"


# --- TEST INACTIVE RULE ---

@patch("core.engine.load_rules")
def test_inactive_rule_ignored(mock_load_rules):
    """ Inactive rule -> ignore -> default policy """
    mock_load_rules.return_value = [ make_rule(type_="block_ip", value="192.168.1.10", active=False) ]

    result = evaluate_request(make_request(ip="192.168.1.10"))

    assert result["action"] == "deny"
    assert result["reason"] == "default policy"


# --- TEST DEFAULT POLICY ---

@patch("core.engine.load_rules")
def test_default_policy(mock_load_rules):
    """ No rules match -> default policy """
    mock_load_rules.return_value = [make_rule(type_="block_ip", value="10.0.0.1")]

    result = evaluate_request(make_request(ip="192.168.1.99"))

    assert result["action"] == "deny"
    assert result["reason"] == "default policy"


# --- TEST PRIORITY ---

@patch("core.engine.load_rules")
def test_priority(mock_load_rules):
    """ The rule with the lower priority resolves the conflict """
    mock_load_rules.return_value = [
        make_rule(id_=1, type_="allow_ip", value="192.168.1.10", priority=5),
        make_rule(id_=2, type_="block_ip", value="192.168.1.10", priority=10),
    ]

    result = evaluate_request(make_request(ip="192.168.1.10"))

    assert result["action"] == "allow"
    assert result["rule_id"] == 1
