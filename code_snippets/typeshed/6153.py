import subprocess
process = subprocess.Popen("echo hello", shell=True, stdout=subprocess.PIPE)
assert process.stdout is not None
print(process.stdout.read1())
