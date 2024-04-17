import os
from pathlib import Path

bundled_folder_path = Path(__file__).parent.parent.absolute()

CHROMEDRIVER_PATH = os.path.join(bundled_folder_path, 'chromedriver_win32', 'chromedriver.exe')
CHROME_BINARY_PATH = os.path.join(bundled_folder_path, 'chrome-win', 'chrome.exe')
USER_DATA_DIR_PATH = os.path.join(bundled_folder_path, 'selenium')
