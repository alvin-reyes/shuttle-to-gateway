# download list of files from IPFS
import requests
import os
import threading


def download_and_upload(url):
    r = requests.get(url, allow_redirects=True)
    open('./download/' + line, 'wb').write(r.content)

    # DOWNLOAD!!

    url = "https://dedicated-gw.estuary.tech/upload"
    payload = {}
    files = [
        ('file', ('file', open('./download/' + line, 'rb'), 'application/octet-stream'))
    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.status_code)

    # remove file
    os.remove('./download/' + line)


with open('jin_files.txt') as jin_hashes:
    for line in jin_hashes:
        print(line, end=' ')  # The comma to suppress the extra new line char
        url = "https://ipfs.io/ipfs/" + line
        print(url)

        download_and_upload(url)
        # threading.Thread(target=download_and_upload, args=(url,)).start()
