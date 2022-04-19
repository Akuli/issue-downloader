...
fut = loop.run_in_executor(None, g)
x = await fut
return x
