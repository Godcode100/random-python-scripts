import subprocess
import shlex
url ='http://127.0.0.1:8000/'
cmd = f'open {url}'
cmd_parts = shlex.split(cmd)
subprocess.run(cmd_parts)
