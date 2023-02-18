# Cisco Catalyst 9800 NETCONF disable radios
 A python script using NETCONF shutdown radios of C9800 managed APs:
 
<img width="725" alt="image" src="https://user-images.githubusercontent.com/28600326/219903794-64f2f4c3-d92e-47fa-bc7f-7d57a7270449.png">

## Targeted changes
### CLI configuration changes

<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

```diff
wireless tag rf FR42_STE07ALD
 24ghz-rf-policy 15dbm_24ghz
 5ghz-rf-policy 15dbm_5ghz
 6ghz-rf-policy 15dbm_6ghz
```

</td>
<td>
    
```diff
wireless tag rf FR42_STE07ALD
+24ghz-rf-policy No_24ghz
+5ghz-rf-policy No_5ghz
+6ghz-rf-policy No_6ghz
-24ghz-rf-policy 15dbm_24ghz
-5ghz-rf-policy 15dbm_5ghz
-6ghz-rf-policy 15dbm_6ghz
```
</td>
</tr>
</table>

### GUI configuration changes

Go to ```Configuration > Tags & Profiles > Tags > RF``` section:
<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219903092-88f22b85-4e31-4ef2-a6cd-e7fd7f3af408.png">
</td>
<td>
    
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219903100-5c4427ec-285c-406b-95f0-9d6ab0e67482.png">
</td>
</tr>
</table>


```xml
<nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:21e08907-aa6d-4ce0-a255-b5f2d640b967">
  <nc:get-config>
    <nc:source>
      <nc:running/>
    </nc:source>
    <nc:filter>
      <rf-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rf-cfg">
        <rf-tags>
          <rf-tag>
            <tag-name>FR42_STE07ALD</tag-name>
            <description/>
            <dot11a-rf-profile-name/>
            <dot11b-rf-profile-name/>
            <dot11-6ghz-rf-prof-name/>
          </rf-tag>
        </rf-tags>
      </rf-cfg-data>
    </nc:filter>
  </nc:get-config>
</nc:rpc>
````

```xml
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:21e08907-aa6d-4ce0-a255-b5f2d640b967">
  <data>
    <rf-cfg-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rf-cfg">
      <rf-tags>
        <rf-tag>
          <tag-name>FR42_STE07ALD</tag-name>
          <dot11a-rf-profile-name>test</dot11a-rf-profile-name>
          <dot11b-rf-profile-name>15dbm_24ghz</dot11b-rf-profile-name>
          <dot11-6ghz-rf-prof-name>No_6ghz</dot11-6ghz-rf-prof-name>
        </rf-tag>
      </rf-tags>
    </rf-cfg-data>
  </data>
</rpc-reply>
```
