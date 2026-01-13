from urllib.request import urlopen

url = "https://mathesis.netlify.app/"

page = urlopen(url)

print(page.read().decode("utf-8"))