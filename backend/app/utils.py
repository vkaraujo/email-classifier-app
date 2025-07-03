import os

def delete_file(path):
    try:
        os.remove(path)
    except OSError:
        pass
