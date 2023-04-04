# Import the necessary libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import os 
import time
# Authenticate and create the PyDrive client
gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Define the ID of the file you want to download
# file_id = '1BUr_2LBz1BWj3vNyU0GNTojCArdu9_ew'
files_id = '''1-1YjGz7oYos2zrJdHZpZaAJeCzesGOIg
1BUr_2LBz1BWj3vNyU0GNTojCArdu9_ew
1tHjPG6gZI-WLkHeQsYGcwQySUrkB47Lc
12xsRojkwDAf9a9QHvH3q0ugd_1U4qDBk
1VmcrhoctvyWsOUrvdYYQr1yf0o7_12OH
1JyVbGiWAxMhPyvRmu-IyZZyR0Nql3wLr
1OvuUg21qAtA77o3Qw4EwxV56xX-DMJUQ
1-2rbkfcyvZcDMoxKrmcBYW-Y7pD6W2Li
1UJmG_vUHgfboRqaqtWQ2JPiAzYY_PH8M
1mh9USFLXYfZt_mhrHWI0dtAyIOI2CNUc
1J0rvW1hdpVSckzQWlG_OslxMFDVGdndQ
1a8HcZhqogrgTxvir_aaWmtSVNac1tQzX
1xq6DcAcovqUh3zImmKEKbQ6B28IKH3um
100_t3-75wKaFkFB7YCwoo_iXQQBHgOzE
1Bg12yu7K0u7ZWhUGUS_TjAfpyeCep1KK
1PP7TJrIIwmfxJsJK-6GF69AlmReqjned
1w2B9cseYlnHLZq9-pi_5b9WCX88ZsJwU
1E-w2jJadlzdR7FIZSXiq9RXjijjUid5_
1YL5I3cxLDBmfVf9xU-hz2QVgUCa5S79R
1pWx8RklUfLDteV_sX6rO5rksfkI7i_sk
1grxbzNHirT0YTM8GZBZWTVAcYRKjjb5R
1YQvlTobKClIg4m0xsc7CDjJX4FFWCQgh
17QmcxaadoA6HwZUVMv0bzFS-hVC9ei5C
1cA724u27eEv0fFcNAqYcD45ZJ5sV1SXs'''.split('\n')

for file_id in files_id:
    # Get the file from Google Drive
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(file['title'])

    # Check if the file is a PDF
    if file['mimeType'] == 'application/pdf':
        # Download the file
        file.GetContentFile(file['title'])
        print(f'Downloaded "{file["title"]}" to the current directory.')
    else:
        print('The file is not a PDF.')

os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)
os.system('paplay /usr/share/sounds/Oxygen-Im-Cant-Connect.ogg')
time.sleep(1)