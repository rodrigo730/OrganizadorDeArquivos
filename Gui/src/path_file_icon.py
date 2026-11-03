from pathlib import Path

FOLDER_PATH = Path(__file__).parent.parent
FILE_PATH = FOLDER_PATH / 'files' / 'python-logo-only.png'
print(FILE_PATH)