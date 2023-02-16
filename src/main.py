from ncclient import manager
import yaml

# Open the config.yml file and load its contents into the 'config' variable
with open('../config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Set up device info
for c9800 in config["controllers"]:
    username=c9800["username"]
    password=c9800["password"]
    port = c9800["port"]
    host = c9800["host"]
    device_params={"name":"iosxe"}

netconf_filter = """ <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"></interfaces> </filter> """

with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as m:
    c = m.get_config('running', netconf_filter).data_xml
    with open("%s_int.xml" % host, 'w') as f:
        f.write(c)