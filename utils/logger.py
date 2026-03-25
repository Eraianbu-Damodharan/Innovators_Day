import os
from datetime import datetime
from utils.config import LOG_FILE

os.makedirs("logs", exist_ok=True)

def log_action(user_input: str, tool: str, args: str, result: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"INPUT={user_input} | TOOL={tool} | ARGS={args} | RESULT={result}\n"
        )