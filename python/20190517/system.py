import os, subprocess

# print(os.popen('ls').read())
# shell 指定默认shell解释器解释第一个命令，stdout 当命令执行成功以后把结果放进去（管道）stderr 当命令执行错误时把结果放进去（管道）
sp = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(sp.stdout.read().decode())
print(sp.stderr.read())

