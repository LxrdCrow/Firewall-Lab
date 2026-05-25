import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logger = logging.getLogger("firewall")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/firewall.log")
handler.setFormatter(logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
))
logger.addHandler(handler)

def log_request(request: dict, result: dict):
    action = result["action"].upper()
    logger.info(f"{action} | ip={request.get('ip')} port={request.get('port')} path={request.get('path')} | reason={result.get('reason')}")