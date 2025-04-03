import json
from pathlib import Path

class UserManager:
    def __init__(self):
        self.data_path = Path("data/users.json")
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not self.data_path.exists():
            self.data_path.parent.mkdir(exist_ok=True)
            with open(self.data_path, "w") as f:
                json.dump({"allowed": [], "admins": []}, f)

    def is_admin(self, user_id: int) -> bool:
        with open(self.data_path, "r") as f:
            data = json.load(f)
        return user_id in data["admins"]

    def is_allowed(self, user_id: int) -> bool:
        with open(self.data_path, "r") as f:
            data = json.load(f)
        return user_id in data["allowed"] or self.is_admin(user_id)