#!/usr/bin/python3

import subprocess
import os

root_dir = '2019-1-PA0'
files_in_root_dir = os.listdir(root_dir)

for filename in files_in_root_dir:
    file_path_v = root_dir, filename
    file_path = str(os.path.join(*file_path_v))

    # TODO: Deal with report

    command = ['make', '-C', file_path]

    result = subprocess.run(command)

    if result.returncode != 0:
        print('Compile error')

