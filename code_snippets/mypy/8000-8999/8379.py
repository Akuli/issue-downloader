class TryWalrus:
    CKEY = { 
        'KY': (p:='a_'),
         'ANOTHER': p+'content',
        }

print(TryWalrus.CKEY['ANOTHER']) # => a_content
