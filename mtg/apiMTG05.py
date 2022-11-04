#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    """Run time code"""
    resp = requests.get(f"{API}sets")
    cardsets = resp.json().get("sets")

    for cardset in cardsets:
         print(cardset)

if __name__ == "__main__":
    main()

    
