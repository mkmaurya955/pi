import requests

url="http://zohobooks.co.in/upload/save_image.php"

files={'image':open('img.jpg','rb')}
try:
	response=requests.post(url,files=files,timeout=60)
	print(response)

except requests.exceptions.RequestException as  e:
	print("Error:{}".format(e))
	print("time out error")
