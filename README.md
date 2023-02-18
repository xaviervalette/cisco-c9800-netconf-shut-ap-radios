# cisco-c9800-netconf-disable-radios
 A python script using NETCONF shutdown radios of C9800 managed APs

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
-24ghz-rf-policy 15dbm_24ghz
-5ghz-rf-policy 15dbm_5ghz
-6ghz-rf-policy 15dbm_6ghz
```

</td>
<td>
    
```diff
wireless tag rf FR42_STE07ALD
+24ghz-rf-policy No_24ghz
+5ghz-rf-policy No_5ghz
+6ghz-rf-policy No_6ghz
```
</td>
</tr>
</table>

### GUI configuration changes

<table>
<tr>
<td> Before </td> <td> After </td>
</tr>
<tr>
<td>

<img width="1658" alt="image" src="https://user-images.githubusercontent.com/28600326/219868447-af490010-f71f-43c4-a9c4-5f1cfc69afd6.png">


</td>
<td>
    
<img width="1658" alt="image" src="https://user-images.githubusercontent.com/28600326/219868431-a67a6cf4-34f1-4cb8-8963-0c81ded91f2a.png">


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
