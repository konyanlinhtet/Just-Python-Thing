import os
from datetime import *
stats = os.stat("./15_walk.py")
print("File size in bytes ",stats.st_size)
print("last modified ",datetime.fromtimestamp(stats.st_mtime))
print("last access",datetime.fromtimestamp(stats.st_mtime))