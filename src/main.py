# Import necessary libraries
from ncclient import manager    # ncclient library used to manage NETCONF operations
import yaml    # yaml library used to read YAML configuration files
from xml.dom import minidom    # xml.dom library used to parse XML files
import xmltodict
import sys

if len(sys.argv) != 2:
    print("Usage: python main.py 0 (shut radios) or python main.py 1 (no shut radios)")
    sys.exit(1)

# Parse the argument
arg = sys.argv[1]

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
    # Open the XML file and read its contents
    with open('netconf/config/rfTagsContainer.xml', 'r') as file:
        rfTagsContainerDict = xmltodict.parse(file.read())

    with open('netconf/config/rfTag.xml', 'r') as file:
        rfTagDict = xmltodict.parse(file.read())

    for rfTag in config["rfTags"]:
        rfTagDict["rf-tag"]["tag-name"] = rfTag["name"]
        if arg == 0:
            rfTagDict["rf-tag"]["dot11a-rf-profile-name"] = rfTag["rfProfiles"]["no5ghz"]
            rfTagDict["rf-tag"]["dot11b-rf-profile-name"] = rfTag["rfProfiles"]["no24ghz"]
            rfTagDict["rf-tag"]["dot11-6ghz-rf-prof-name"] = rfTag["rfProfiles"]["no6ghz"]
        else:
            rfTagDict["rf-tag"]["dot11a-rf-profile-name"] = rfTag["rfProfiles"]["5ghz"]
            rfTagDict["rf-tag"]["dot11b-rf-profile-name"] = rfTag["rfProfiles"]["24ghz"]
            rfTagDict["rf-tag"]["dot11-6ghz-rf-prof-name"] = rfTag["rfProfiles"]["6ghz"]
        rfTagsContainerDict["config"]["rf-cfg-data"]["rf-tags"] = []
        rfTagsContainerDict["config"]["rf-cfg-data"]["rf-tags"].append(rfTagDict)
    
    rfTagsContainerXml = xmltodict.unparse(rfTagsContainerDict, pretty=True)

    # Connect to the device and edit its configuration
    with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as netconf_manager:
        edit_config_response = netconf_manager.edit_config(rfTagsContainerXml, target='running')

    # Read in the NETCONF XML filter file and convert to string
    getRfTagsXml = minidom.parse('netconf/filter/getRfTags.xml').toxml()

    # Connect to the device and retrieve its configuration, then parse and format the output
    with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as netconf_manager:
        get_config_response = netconf_manager.get_config('running', getRfTagsXml).data_xml
        parsed_xml = minidom.parseString(get_config_response)
        pretty_xml = parsed_xml.toprettyxml()
        print(pretty_xml)

        # Write the output to a file
        with open("conf/%s_rf-tags.xml" % host, 'w') as file:
            file.write(pretty_xml)
