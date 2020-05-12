from dataclasses import dataclass
import numpy as np


@dataclass
class Status:
    is_alive: bool = True
    frame: np.array = None
