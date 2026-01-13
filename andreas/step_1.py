from urllib.request import urlopen

url = "https://www.geschkult.fu-berlin.de/e/semiarab/arabistik/seminar/index.html"

page = urlopen(url)

print(page.read().decode("utf-8"))

