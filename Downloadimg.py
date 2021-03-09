import urllib.request
import re

url = "https://www.indiaglitz.com/hindi-actor-aamir-khan-photos-7950"
request_response = urllib.request.urlopen(url)
wc = request_response.read()
imageurls = re.findall(r'src=[\'"]?([^\'" >]+amir.*?jpg)[^ ]', str(wc))
for i,imageurl in enumerate(imageurls):
    urllib.request.urlretrieve(imageurl, str(i)+'.jpg')