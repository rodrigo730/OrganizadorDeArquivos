from pathlib import Path
import sys


FOLDER_PATH = Path(__file__).parent.parent
FILE_ICON_PATH = FOLDER_PATH / 'files' / 'python-logo-only.png'
PATH_ABSOLUTE = Path(__file__).resolve()
PATH_FOLDER_ABSOLUTE = PATH_ABSOLUTE.parents[2]
sys.path.append(str(PATH_FOLDER_ABSOLUTE))
print(PATH_FOLDER_ABSOLUTE)
print(sys.path)
