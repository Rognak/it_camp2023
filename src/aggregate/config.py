from enum import Enum
import os


class Settings(Enum):
    VLP_HOST = f"http://{os.environ.get('VLP_HOST', 'localhost')}:8000"
    IPR_HOST = f"http://{os.environ.get('IPR_HOST', 'localhost')}:8002"
    NODAL_HOST = f"http://{os.environ.get('NODAL_HOST', 'localhost')}:8003"
