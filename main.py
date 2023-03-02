# download list of files from IPFS
import requests
import os
with open('jin_files.txt') as jin_hashes:
    for line in jin_hashes:
        print(line, end=' ')  # The comma to suppress the extra new line char
        url = "https://shuttle-9.estuary.tech/gw/ipfs/" + line
        print(url)
        r = requests.get(url, allow_redirects=True)
        open('./download/'+line, 'wb').write(r.content)

        # DOWNLOAD!!

        url = "https://gateway.estuary.tech/upload"
        payload = {}
        files = [
            ('file', ('file', open('./download/'+line, 'rb'), 'application/octet-stream'))
        ]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)

        # UPLOAD !!

        # Delete the file
        os.remove('./download/'+line)