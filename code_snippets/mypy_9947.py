@icontract.ensure(lambda result: (result[0] is None) ^ (result[1] is None))
def some_func() -> Tuple[Optional[str], Optional[str]]:
    ...
    return something, errors

...

result, errors = some_func()
if errors is not None:
   ...

# We know here according to the contract that ``result`` can not be None.
