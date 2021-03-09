import urllib.request
def dl_jpg(url,file_path,file_name):
    full_path=file_path+file_name+'.jpg'
    urllib.request.urlretrieve(url,full_path)

url = input("enter the img URL to download:")
file_name = input("enter the file name:")

dl_jpg(url,'images/',file_name)