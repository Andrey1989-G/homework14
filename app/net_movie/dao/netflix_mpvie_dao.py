from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.joinpath('app')

DATA_PATH = DATA_DIR.joinpath("netflix.db")

