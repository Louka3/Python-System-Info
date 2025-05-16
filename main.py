import platform as Platform
import psutil as PSUtil
import os as OS
from rich import print as rprint
from rich.columns import Columns
from rich.panel import Panel
import shutil


# OS, CPU, RAM, disk space, etc.

def bytes_to_gib(bytes):
  return bytes / (1024 ** 3)

def bytes_to_gb(bytes):
  return bytes / 1e9

my_os = "OS: " + Platform.system()
if my_os == "OS: Darwin":
  my_os += "(Apple)"
# my_uname = Platform.uname()
my_cpu = "CPU: " + Platform.machine()

mem = PSUtil.virtual_memory()
total_mem = bytes_to_gib(mem.total)
my_total_mem = "RAM: " + str(total_mem) + " GB"

ds = shutil.disk_usage('/')

final_string = 'System Info\n-------------'
final_string += "\n" + my_os
final_string += "\n" + my_cpu
final_string += "\n" + my_total_mem
final_string += "\nDisk Space:\n" + "\tTotal: " + format(bytes_to_gb(ds.total), '.3f') + " GB\n\tUsed: " + format(bytes_to_gb(ds.used), '.3f') + " GB\n\tFree: "+ format(bytes_to_gb(ds.free), '.3f') + " GB"

print(total_mem)
rprint(Panel(final_string, width=50))
