from ncclient import manager
import yaml
import xml.dom.minidom

# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Set up device info
for c9800 in config["controllers"]:
    username=c9800["username"]
    password=c9800["password"]
    port = c9800["port"]
    host = c9800["host"]
    device_params={"name":"iosxe"}

netconf_filter = """ <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> 
      <rf-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rf-cfg">
        <rf-tags>
          <rf-tag>
            <tag-name>FR42_STE07ALD</tag-name>
            <description/>
            <dot11a-rf-profile-name></dot11a-rf-profile-name>
            <dot11b-rf-profile-name></dot11b-rf-profile-name>
            <dot11-6ghz-rf-prof-name></dot11-6ghz-rf-prof-name>
          </rf-tag>
        </rf-tags>
      </rf-cfg-data>
</filter> """


with manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params=device_params) as m:
    c = m.get_config('running', netconf_filter).data_xml
    temp = xml.dom.minidom.parseString(c)
    new_xml = temp.toprettyxml()
    print(new_xml)
    with open("%s_rf-tags.xml" % host, 'w') as f:
        f.write(new_xml)

