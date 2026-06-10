import logging
from pathlib import Path
from models.filter import FirewallRequest

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("firewall")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/firewall.log")
handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
))
logger.addHandler(handler)

def log_request(request: FirewallRequest, result: dict):
    action = result["action"].upper()
    logger.info(f"{action} | ip={request.ip} port={request.port} path={request.path} | reason={result.get('reason')}")