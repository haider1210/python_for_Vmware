#pip install pyvmomi

from pyVim.connect import SmartConnect, Disconnect
import ssl

# Ignore SSL warnings
context = ssl._create_unverified_context()

# Connect to vSphere
si = SmartConnect(
    host="your_vcenter_server",
    user="your_username",
    pwd="your_password",
    sslContext=context
)

# Retrieve content
content = si.RetrieveContent()

# Print VM names
for datacenter in content.rootFolder.childEntity:
    for vm in datacenter.vmFolder.childEntity:
        print(vm.name)

# Disconnect from vSphere
Disconnect(si)
