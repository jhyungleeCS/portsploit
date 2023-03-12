#!/usr/bin/env python3

import shodan

api_key = '864UqpknfcTN9HWpkX8Kz5bzzaTiWNWc' #jl3993 API Key. Use yours here

def search_org(org, port):
    api = shodan.Shodan(api_key)
    try:
        query = 'org:"{}" port:{}'.format(org, port)
        results = api.search(query)
        return results['matches']
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return []