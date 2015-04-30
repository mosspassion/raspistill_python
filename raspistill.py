import subprocess
import tempfile

raspistill_date = '''\
DATE=$(date +"%Y-%m-%d_%H:%M")

raspistill -vf -hf -o $DATE.jpg
'''

def run_script(script):
    with tempfile.NamedTemporaryFile() as scriptfile:
        scriptfile.write(script)
        scriptfile.flush()
        subprocess.call(['/bin/bash', scriptfile.name])

run_script(raspistill_date)
