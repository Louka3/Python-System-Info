import platform as Platform
import psutil as PSUtil
import os as OS

# OS, CPU, RAM, disk space, etc.

BYTES_IN_GB = 1e9


my_os = Platform.system()
print(my_os) # OS
my_uname = Platform.uname()
print(my_uname)
my_machine = Platform.machine()
print(my_machine)
my_cpu = Platform.processor()
print(my_cpu)

mem = PSUtil.virtual_memory()
total_mem = mem.total / BYTES_IN_GB

print(str(total_mem) + ' GB')



