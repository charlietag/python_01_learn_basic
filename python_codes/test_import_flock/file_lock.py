# ------------------------------------------
# --- Lock ---
# fcntl.flock - only support linux

# Ref. https://psutil.readthedocs.io/en/latest/
# psutil - Cross platform
#        - psutil.Process

# --- check if variable is defined ---
# Ref. https://www.geeksforgeeks.org/how-to-check-if-a-python-variable-exists/

# locals()  - in function
# globals() - outsidde function

# ------------------------------------------

from pathlib import Path
import psutil

class FileLock:
    # ----------------------------------------
    # init
    # ----------------------------------------
    def __init__(self, name = None):
        if name is None:
            import __main__
            self._name = __main__.__file__
        else:
            self._name = name

        self._f = Path(self._name)
        self._lock_file = self._f.with_suffix('.lock')

        # -------------------------------------
        # true - test_import_flock.py exists
        # print(self._f.is_file())

        # false - test_import_flock.lock does not exists
        # print(self._lock_file.is_file())
        # -------------------------------------

        print("init test")
        # print(type(self._lock_file))
        print(self._lock_file)

    # ----------------------------------------
    # lock
    # ----------------------------------------
    def lock(self):
        self.check_process()
        print("--- lock start ---")
        current_pid = psutil.Process().pid

        with open(self._lock_file, "w", encoding="utf-8") as f:
            f.write(str(current_pid))

        print("Current PID:", current_pid)
        print(f"Current PID {current_pid} is written to {self._lock_file}")


    # ----------------------------------------
    # unlock
    # ----------------------------------------
    def unlock(self):
        # no extra actions needed
        print("--- unlock ---")
        print("no extra actions needed")



    # ----------------------------------------
    # other method
    # ----------------------------------------
    def is_pid_running(self, pid = None):
        try:
            # Check if the process with the given PID is running
            process = psutil.Process(pid)
            return process.is_running()
        except psutil.NoSuchProcess:
            return False

    def is_file_exists(self):
        f_status = False

        if self._lock_file.is_file():
            f_status = True

        return f_status


    def check_process(self):
        # print("check...")
        # if self._lock_file.is_file():
        if self.is_file_exists():
            with open(self._lock_file, "r") as f:
                pid = int(f.read().strip())

            if self.is_pid_running(pid):
                print(f"Process with PID {pid} is running.")
                exit()
        #     else:
        #         print(f"Process with PID {pid} is not running.")
        # else:
        #     print("Lock file not found. The script may not be running.")
