from flask import Blueprint, jsonify, request

from core.engine import evaluate_request, load_rules, save_rule
from models.filter import FirewallRequest, FirewallRule

bp = Blueprint("api", __name__)


@bp.route("/simulate", methods=["POST"])
def simulate():
    data = request.get_json()
    fw = FirewallRequest(
        data["ip"],
        data["port"],
        data["protocol"],
        data["path"],
        data["method"],
    )
    result = evaluate_request(fw)
    return jsonify(result)


@bp.route("/rules", methods=["GET"])
def get_rules():
    rules_list = load_rules()
    rules_dict = [rule.to_dict() for rule in rules_list]
    return jsonify(rules_dict)


@bp.route("/rules", methods=["POST"])
def add_rule():
    data = request.get_json()
    fw = FirewallRule.from_dict(data)
    save_rule(fw)
    return jsonify(fw.to_dict()), 201
