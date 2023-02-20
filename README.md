# Cisco Catalyst 9800 NETCONF shut radios
 A python script using NETCONF shutdown radios of C9800 managed APs:
 
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219956385-baa50880-bb4f-490e-89c6-2a4e0782813a.png">

## Targeted changes

To do so, the script updates RF Profiles of 2.4GHz, 5GHz and 6GHz bands for given RF Tags.

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
-24ghz-rf-policy 15dbm_24ghz
+24ghz-rf-policy No_24ghz
-5ghz-rf-policy 15dbm_5ghz
+5ghz-rf-policy No_5ghz
6ghz-rf-policy No_6ghz
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

<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219962987-7938febe-2207-4e95-8df7-4a37bd23994b.png">
 
 </td>
<td>
 
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219963013-576873af-39b7-4845-95da-ed1e9f0171c3.png">
 
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
    ├── netconf/
    │    ├── config/
    │    │     ├── rfTag.xml
    │    │     └── rfTagsContainer.xml
    │    └── filter/
    │          └── getRfTags.xml
    └── conf/
         └── <wlc_ip>_rf-tags.xml  
```
4. In the config.yml file, add the following variables:
```yaml
#config.yml
---

controllers:
  - name: "<wlc name>"
    username: "<wlc NETCONF username>"
    password: "<wlc NETCONF password>"
    port: "<wlc NETCONF port>"
    host: "<wlc NETCONF @IP>"
rfTags:
  - name: FR42_STE07ALD
    rfProfiles:
      radiosDown:
        24ghz: "No_24ghz"
        5ghz: "No_5ghz"
        6ghz: "No_6ghz"
      radiosUp:
        24ghz: "15dbm_24ghz"
        5ghz: "15dbm_5ghz"
        6ghz: "No_6ghz"
      
...

```
5. Now you can run the code by using the following command:

Disable the radio of access points:
```console
python3 src/main.py 0
```

Enable the radio of access points:
```console
python3 src/main.py 1
```

## Output
<table>
<tr>
<th width="800px">

 ```console
python3 src/main.py 1
```
 
</th> <th width="800px">
 
 ```console
python3 src/main.py 0
```
 
 </th>
</tr>
<tr>
<td>

<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219943599-50998333-fa66-4aab-96b4-30f38b3e7bcf.png">

</td>
<td>
<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/219943608-f1ed543c-9799-46b7-bcc5-d8b9a6bb1f5c.png">

</td>
</tr>
</table>
