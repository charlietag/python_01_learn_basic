class FileLock:
    def __init__(self, name="this.lock"):
        print("init test")
        print(name)

    def lock(self):
        print("lock test")
