import pymongo # this can be any third-party module without stubs

Collection = pymongo.collection.Collection

def func(a: Collection) -> bool:
   return True

import pymongo

def func(a: pymongo.collection.Collection) -> bool:
  return True
