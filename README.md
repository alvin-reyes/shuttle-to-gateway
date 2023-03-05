# shuttle-to-gateway
Simple shuttle to gateway manual data transfer. It'll basically download the CID from reliable IPFS nodes and push it to Estuary gateway


## Install
```
git clone https://github.com/alvin-reyes/shuttle-to-gateway
```

## Configure
```
def download_and_upload(url):
    r = requests.get(url, allow_redirects=True)
    open('./download/' + line, 'wb').write(r.content)
    
    # CHANGE URL if you want to push to another gateway
    url = "https://gateway.estuary.tech/upload" 
    payload = {}
    files = [
        ('file', ('file', open('./download/' + line, 'rb'), 'application/octet-stream'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)

    # remove file
    os.remove('./download/' + line)
    
# change the text file here if you want to use your own list of CIDs    
with open('jin_files.txt') as jin_hashes: 
```
## Running
```
cd shuttle-to-gateway
python main.py
```
