import os

def _registerTaskByPid(pid, packageName) -> bool:
    os.system(f"./db/task.exe {pid} {packageName}")
    return True
