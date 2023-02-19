# Cisco Catalyst 9800 NETCONF disable radios
 A python script using NETCONF shutdown radios of C9800 managed APs:
 
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219938190-5cc80d65-f912-40ac-a23e-888f0335a54b.png">

## Targeted changes
### CLI configuration changes

<table>
<tr>
<th width="800px"> Before </th> <th width="800px"> After </th>
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
<th width="800px"> Before </th> <th width="800px"> After </th>
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

## Get started
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/cisco-c9800-netconf-disable-ap-radios
```
2. Install required packages
```console
pip3 install -r requirements.txt
```
3. Add a file called config.yml as follow:
```diff
└── cisco-c9800-netconf-disable-ap-radios/
+   ├── config.yml
    ├── src/
    │    └── main.py    
    └── conf/
         └── <wlc_ip>_rf-tags.xml  
```
4. In the config.yml file, add the following variables:
```yaml
#config.yml
---

tagName: <RF tag name>
controllers:
  - name: "<wlc name>"
    username: "<wlc NETCONF username>"
    password: "<wlc NETCONF password>"
    port: "<wlc NETCONF port>"
    host: "<wlc NETCONF @IP>"
    
...

```
5. Now you can run the code by using the following command:
```console
python3 src/main.py
```

## Output
<table>
<tr>
<th width="800px"> Before </th> <th width="800px"> After </th>
</tr>
<tr>
<td>

<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219943599-50998333-fa66-4aab-96b4-30f38b3e7bcf.png"></td>
<td>
    
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219943608-f1ed543c-9799-46b7-bcc5-d8b9a6bb1f5c.png"></td>
</tr>
</table>
