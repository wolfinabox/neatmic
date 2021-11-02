import sys,os
import subprocess
import time
if len(sys.argv)<3:
    print('Pass scripy pyside-uic path, ui folder path, and output folder path')
    sys.exit()

_,pyside_exe,ui_folder,out_folder=sys.argv
print(f'Using {pyside_exe}')
#get all ui files
ui_files=[f for f in os.listdir(ui_folder) if os.path.isfile(os.path.join(ui_folder, f)) and f.endswith(".ui")]
print(f'Processing: {",".join(ui_files)}')

for file in ui_files:
    in_path=os.path.join(ui_folder,file)
    out_name=os.path.splitext(file)[0]+'_ui.py'
    out_path=os.path.join(out_folder,out_name)
    #run pyside6-uic
    proc=subprocess.Popen([pyside_exe,in_path],stdout=subprocess.PIPE,stdin=None,stderr=None)
    print(f'{file} > {out_name}')
    #eugh
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired as e:
        print(f'Timed out after {e.timeout}s!')
    lines=proc.stdout.read().decode('utf-8')
    print(f'{len(lines)} lines')
    with open(out_path,'w') as out_file:
        out_file.write(lines)
    print('Done')
