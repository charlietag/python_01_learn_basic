import test_import_flock as f

# --- default in FileLock init ---
# from pathlib import Path
# lock_file = Path(__file__).with_suffix('.lock')
# script = f.FileLock(name=lock_file)
# --- default in FileLock init ---

script = f.FileLock()

script.lock()

# -------------------------------------------------------
# main
# -------------------------------------------------------
print("sleep 600")
import time
time.sleep(600)


# -------------------------------------------------------
script.unlock()
