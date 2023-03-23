#!/usr/bin/env python3

import shodan

api_key = '6KvXzZK8Zt9K6hksjl75uB8QOcLUI1L2' #Kevin's API Key. Use yours here

def search_org(org, port):
    api = shodan.Shodan(api_key)
    try:
        query = 'org:"{}" port:{}'.format(org, port)
        results = api.search(query)
        return results['matches']
    except shodan.APIError as e:
        print('Error: {}'.format(e))
        return []