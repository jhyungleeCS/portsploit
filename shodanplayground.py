#!/usr/bin/env python3

import shodan

api_key = '864UqpknfcTN9HWpkX8Kz5bzzaTiWNWc' # Use your API key here

def search_org(org):
    api = shodan.Shodan(api_key)
    try:
        results = api.search('org:"{}"'.format(org))
        return results['matches']
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return []

if __name__ == "__main__":
    print("Test") 
