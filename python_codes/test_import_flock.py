from pathlib import Path
import test_import_flock as f

lock_file = Path(__file__).with_suffix('.lock')
script = f.FileLock(name=lock_file)
script.lock()
