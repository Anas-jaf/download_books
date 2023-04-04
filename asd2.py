import requests

# Replace the URL with the URL of the PDF file on Google Drive
url = 'https://drive.google.com/uc?id=1-1YjGz7oYos2zrJdHZpZaAJeCzesGOIg&export=download'

# Replace YOUR_FILE_ID with the ID of the PDF file on Google Drive
# url = url.replace('YOUR_FILE_ID', 'YOUR_ACTUAL_FILE_ID')

# Make an HTTP request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the PDF file to 
    with open('filename.pdf', 'wb') as f:
        f.write(response.content)
    print('PDF file downloaded successfully.')
else:
    print('Error downloading PDF file.')