import subprocess
proc = subprocess.Popen("python newfile.py > /dev/null &",shell=True);
print(proc.pid);
