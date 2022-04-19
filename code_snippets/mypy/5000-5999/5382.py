from concurrent.futures import ThreadPoolExecutor
import sys

opts = {'max_workers': None}
if sys.version_info >= (3, 6):
    opts['thread_name_prefix'] = 'SyncWorker'
executor = ThreadPoolExecutor(**opts)
