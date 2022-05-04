s = requests.Session()
s.hooks['response'].append(print_url)
