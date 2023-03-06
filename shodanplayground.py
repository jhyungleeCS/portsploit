import shodan
import sys

API_KEY = '6KvXzZK8Zt9K6hksjl75uB8QOcLUI1L2'

try:
    api = shodan.Shodan(API_KEY)

    query = "org:'Drexel University' port:80"
    results = api.search(query)

    for result in results['matches']:
        print("Port: %s" % result['port'])
        print(result['data'])

except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
