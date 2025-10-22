import json
import os

class JsonDB:
    def __init__(self, dbpath):
        self._dbpath = dbpath

    def _load(self):
        if not os.path.exists(self._dbpath):
            return {}
        
        with open(self._dbpath, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    def _save(self, data):
        with open(self._dbpath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_collection(self, entity_type):
        data = self._load()
        return data.get(entity_type, [])

    def set_collection(self, entity_type, collection):
        data = self._load()
        data[entity_type] = collection
        self._save(data)
