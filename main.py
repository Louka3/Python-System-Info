import platform as Platform
import psutil as PSUtil
import os as OS
from rich import print as rprint
from rich.columns import Columns
from rich.panel import Panel


# OS, CPU, RAM, disk space, etc.

BYTES_IN_GB = 1e9





my_os = Platform.system()

my_uname = Platform.uname()
# print(my_uname)
my_machine = Platform.machine()

my_cpu = Platform.processor()
# print(my_cpu)

mem = PSUtil.virtual_memory()
total_mem = mem.total / BYTES_IN_GB

ds = PSUtil.disk_usage('/')


print("OS: " + my_os)
print("CPU: " + my_cpu)
print("RAM: " + format(total_mem, '.3f') + " GB")
print("Disk Space:")
print("\tTotal: " + format(ds.total / BYTES_IN_GB, '.3f') + " GB\n\tUsed: " + format(ds.used / BYTES_IN_GB, '.3f') + " GB\n\tFree: "+ format(ds.free / BYTES_IN_GB, '.3f') + " GB") 

rprint(Columns([my_os, my_cpu, my_machine], padding=(3,3)))

# i need to build the string first, then pass it to the Panel
rprint(Panel(my_os + "\n" + my_cpu + "\n" + my_machine, expand=False))