import sys
import requests

#################################################################################
# you will need an api key from https://user.whoisxmlapi.com/products           #
# if you don't have free credits, you will need to purchase credits in DRS      #
# https://drs.whoisxmlapi.com/pricing                                           #
# 3 command line args - searchterm, nameserver1, nameserver2                    #
#################################################################################

url = "https://reverse-whois.whoisxmlapi.com/api/v2"
token = "PUT YOUR TOKEN HERE"

def posty():
    initial = requests.post(url=url, data=post_data)
    req = initial.json()

    if initial.status_code != 200:
        print(initial.text)
        quit()

    domains = req['domainsList']
    for i in domains:
        if domain_search in i:
            print(i)


if len(sys.argv) > 1:
    domain_search = sys.argv[1]
    ns_1 = sys.argv[2]
    ns_2 = sys.argv[3]
    post_data = (
                '{"apiKey":"%s","searchType":"current","mode":"purchase","advancedSearchTerms":[{"field":"NameServers","term":"%s"},{"field":"NameServers","term":"%s."}]}' % (
        token, ns_1, ns_2))

    posty()
else:
    print("Usage: $ python3 WhoISXml-CloudFlare.py <search domain> <nameserver1> <nameserver2>")
    print("Usage: $ python3 WhoISXml-CloudFlare.py discord gabe.ns.cloudflare.com sima.ns.cloudflare.com")