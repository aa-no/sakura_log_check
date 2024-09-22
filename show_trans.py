#!/usr/bin/env python
import subprocess
import time
import sys

def run_command():
    return subprocess.run('./latest_assistant.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout

# def clear_previous_output(num_lines):
#     for _ in range(num_lines):
#         sys.stdout.write("\033[F")  # 将光标上移一行
#         sys.stdout.write("\033[K")  # 清除当前行

r = run_command()

print(r, end='', flush=True)
previous_lines = r.splitlines()

while True:
    # 每秒钟获取新输出
    nr = run_command()
    time.sleep(1)
    
    if nr == r:
        continue
    else:
        current_lines = nr.splitlines()
        newline = [line for line in current_lines if line not in previous_lines]
        
        r = nr
        print("\n".join(newline))
        
        previous_lines = current_lines