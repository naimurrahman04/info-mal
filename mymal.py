import platform
import os
import getpass
import wmi
os_name = platform.system()
print("Operating system: ", os_name)
# Get the OS version
os_version = platform.release()
print("Operating system version: ", os_version)
username = getpass.getuser()
print("Current username: ", username)
is_admin = os.environ.get('ADMIN')
if is_admin:
    print("Current user has admin privileges.")
else:
    print("Current user does not have admin privileges.")
c = wmi.WMI()

# retrieve the network adapters
adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

# loop through the adapters and print their configuration details
for adapter in adapters:
    print("Adapter: %s" % adapter.Description)
    print("\tIP Address: %s" % adapter.IPAddress[0])
    print("\tSubnet Mask: %s" % adapter.IPSubnet[0])
    print("\tDefault Gateway: %s" % adapter.DefaultIPGateway[0])
    print("\tDNS Servers: %s" % adapter.DNSServerSearchOrder)
