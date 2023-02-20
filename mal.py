import os
import platform
import subprocess
import sys

# Get the OS name and version
os_name = platform.system()
os_version = platform.release()

# Get the current username
username = os.environ.get('USERNAME')

# Check if the user is an administrator
is_admin = False
groups = subprocess.check_output(['net', 'localgroup']).decode('utf-8')
if 'Administrators' in groups:
    members = subprocess.check_output(['net', 'localgroup', 'Administrators']).decode('utf-8')
    if username in members:
        is_admin = True

# Get the IP configuration
config = subprocess.check_output(['ipconfig']).decode('utf-8')

# Get the current working directory, process ID, process name, and executable path
current_dir = os.getcwd()
pid = os.getpid()
process_name = os.path.basename(__file__)
executable_path = sys.executable

# Check if Windows Defender is installed
defender_path = os.path.join(os.environ['ProgramFiles'], 'Windows Defender')
windows_defender_installed = os.path.exists(os.path.join(defender_path, 'MsMpEng.exe'))

# Check if the current file is executable
current_file_is_executable = os.access(__file__, os.X_OK)

# Print the results
print('Operating system:', os_name)
print('Operating system version:', os_version)
print('Current username:', username)
print('Current user has admin privileges:', is_admin)
print('IP configuration:', config)
print('Current working directory:', current_dir)
print('Process ID:', pid)
print('Process name:', process_name)
print('Executable path:', executable_path)

if windows_defender_installed:
    print('Windows Defender is installed')
else:
    print('Windows Defender is not installed')

if current_file_is_executable:
    print('This file is executable')
else:
    print('This file is not executable')
