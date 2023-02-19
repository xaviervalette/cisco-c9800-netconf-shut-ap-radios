# Import necessary libraries
from ncclient import manager    # ncclient library used to manage NETCONF operations
import yaml    # yaml library used to read YAML configuration files
from xml.dom import minidom    # xml.dom library used to parse XML files
import xmltodict
import sys

# Check if the correct number of arguments have been provided
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

    # Loop over all the rfTags defined in the configuration file
    for rfTag in config["rfTags"]:
        # Set the tag name
        rfTagDict["rf-tag"]["tag-name"] = rfTag["name"]
        if arg == 0:
            # Set the rf profiles to the "radiosDown" profiles
            rfTagDict["rf-tag"]["dot11a-rf-profile-name"] = rfTag["rfProfiles"]["radiosDown"]["5ghz"]
            rfTagDict["rf-tag"]["dot11b-rf-profile-name"] = rfTag["rfProfiles"]["radiosDown"]["24ghz"]
            rfTagDict["rf-tag"]["dot11-6ghz-rf-prof-name"] = rfTag["rfProfiles"]["radiosDown"]["6ghz"]
        else:
            # Set the rf profiles to the "radiosUp" profiles
            rfTagDict["rf-tag"]["dot11a-rf-profile-name"] = rfTag["rfProfiles"]["radiosUp"]["5ghz"]
            rfTagDict["rf-tag"]["dot11b-rf-profile-name"] = rfTag["rfProfiles"]["radiosUp"]["24ghz"]
            rfTagDict["rf-tag"]["dot11-6ghz-rf-prof-name"] = rfTag["rfProfiles"]["radiosUp"]["6ghz"]
        # Add the current rfTag to the list of rf-tags in the rfTagsContainer
        rfTagsContainerDict["config"]["rf-cfg-data"]["rf-tags"] = []
        rfTagsContainerDict["config"]["rf-cfg-data"]["rf-tags"].append(rfTagDict)
    
    # Convert the rfTagsContainer dict to XML and format it
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
