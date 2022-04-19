from urllib.parse import urlencode, quote

args_dict = {'a': 'b'}
urlencode(args_dict, quote_via=quote)
