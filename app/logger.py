import logging
from datetime import datetime

def setup_logger():
    logging.basicConfig(
        filename=f'logs/bank_{datetime.now().strftime("%Y%m%d")}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

def log_action(username, action):
    with open('audit.log', 'a') as f:
        f.write(f"{datetime.now()} | {username} | {action}\n")
