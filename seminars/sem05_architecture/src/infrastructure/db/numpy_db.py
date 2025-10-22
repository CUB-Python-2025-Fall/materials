import os
import json
import numpy as np
from typing import Optional, Dict


class NumpyDB:
    def __init__(self, dbpath: str) -> None:
        self._dbpath: str = dbpath
        os.makedirs(self._dbpath, exist_ok=True)
        self._data_path: str = os.path.join(self._dbpath, "data.npy")
        self._index_path: str = os.path.join(self._dbpath, "index.json")

    def _load_index(self) -> dict[str, int]:
        if not os.path.exists(self._index_path):
            return {}
        with open(self._index_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_index(self, index: Dict[str, int]) -> None:
        with open(self._index_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

    def _load_data(self) -> np.ndarray:
        if not os.path.exists(self._data_path):
            return np.empty((0, 0), dtype=float)
        return np.load(self._data_path)

    def _save_data(self, data: np.ndarray) -> None:
        np.save(self._data_path, data)

    def get_by_id(self, id: str) -> Optional[np.ndarray]:
        index = self._load_index()
        if id not in index:
            return None
        data = self._load_data()
        return data[index[id]]

    def set_by_id(self, id: str, vector: np.ndarray) -> None:
        if vector.ndim != 1:
            raise ValueError(f"Expected 1D numpy array, got shape {vector.shape}")

        vector_2d: np.ndarray = vector.reshape(1, -1)

        index: Dict[str, int] = self._load_index()
        data: np.ndarray = self._load_data()

        if data.size == 0:
            data = vector_2d
            index[id] = 0
        else:
            if id in index:
                row = index[id]
                data[row] = vector
            else:
                if data.shape[1] != vector_2d.shape[1]:
                    raise ValueError(
                        f"Vector dim {vector_2d.shape[1]} != existing dim {data.shape[1]}"
                    )
                index[id] = len(data)
                data = np.vstack([data, vector_2d])

        self._save_data(data)
        self._save_index(index)
