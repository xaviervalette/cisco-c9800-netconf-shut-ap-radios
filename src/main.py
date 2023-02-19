# Import necessary libraries
from ncclient import manager    # ncclient library used to manage NETCONF operations
import yaml    # yaml library used to read YAML configuration files
from xml.dom import minidom    # xml.dom library used to parse XML files

# Open the configuration YAML file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Set up device info
for controller in config["controllers"]:
    username = controller["username"]
    password = controller["password"]
    port = controller["port"]
    host = controller["host"]
    device_params = {"name": "iosxe"}

    # Read in the NETCONF XML configuration file and convert to string
    netconf_config_xml = minidom.parse('netconf/config/noShutRadios.xml').toxml()

    # Connect to the device and edit its configuration
    with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as netconf_manager:
        edit_config_response = netconf_manager.edit_config(netconf_config_xml, target='running')

    # Read in the NETCONF XML filter file and convert to string
    netconf_filter_xml = minidom.parse('netconf/filter/getRfTags.xml').toxml()

    # Connect to the device and retrieve its configuration, then parse and format the output
    with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as netconf_manager:
        get_config_response = netconf_manager.get_config('running', netconf_filter_xml).data_xml
        parsed_xml = minidom.parseString(get_config_response)
        pretty_xml = parsed_xml.toprettyxml()
        print(pretty_xml)

        # Write the output to a file
        with open("conf/%s_rf-tags.xml" % host, 'w') as file:
            file.write(pretty_xml)
