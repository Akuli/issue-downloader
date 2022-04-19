from os.path import abspath

def test1( x : List[str]) -> List[str] :
    # this is not working
    result = list(map(abspath, x)) # Line 5
    return result                  # Line 6

def test2( x : List[str]) -> List[str] :
    # this is working
    return list(map(abspath, x))
