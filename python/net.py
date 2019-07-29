import requests

def download_img():
    """
    下载图片
    """
    r = requests.get("https://pics1.baidu.com/feed/34fae6cd7b899e5127c964166f7dfc36c9950d4f.jpeg?token=23b4016ab8ebaa9981f9fbcbd647fe5a&s=B3E0E5A61AE187511AE4F1070300F0C1")
    with open("./test.png", 'wb') as f:
        f.write(r.content)   

download_img()