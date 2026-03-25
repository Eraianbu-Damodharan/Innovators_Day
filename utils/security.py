from pathlib import Path
from utils.config import SAFE_DIRECTORIES

def normalize_path(path: str) -> Path:
    return Path(path).expanduser().resolve()

def is_path_allowed(path: str) -> bool:
    try:
        target = normalize_path(path)
        for safe_dir in SAFE_DIRECTORIES.values():
            safe_path = safe_dir.resolve()
            if safe_path == target or safe_path in target.parents:
                return True
        return False
    except Exception:
        return False

def resolve_alias_path(raw_path: str) -> str:
    raw_path = raw_path.strip()
    lowered = raw_path.lower()

    for alias, base in SAFE_DIRECTORIES.items():
        if lowered == alias:
            return str(base.resolve())

        if lowered.startswith(alias + "\\") or lowered.startswith(alias + "/"):
            rest = raw_path[len(alias):].strip().lstrip("\\/")
            return str((base / rest).resolve())

    return str(Path(raw_path).expanduser().resolve())