import requests
import re
def main():
     print(f"Welcome to the simple HTTP response parser. Where should we search (ex: https://alta3.com)?")
     url = input()
     print(f"Great! So we'll try to open this url {url} to search for the phrase:")
     searchFor = input()
     searchMe = requests.get(url).text
     if re.search(searchFor, searchMe):
         print("Found a match!")
     else:
         print("No match!")
if __name__ == "__main__":
    main()
