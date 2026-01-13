from urllib.request import urlopen
url = "https://www.bmlonline.it/"
page = urlopen(url)
print(page.read().decode("utf-8"))

