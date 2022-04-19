class SubModel(BaseModel):
    entries: list


class MyModel(BaseModel):
    myessentialfield: str
    myoptionalfield: Optional[SubModel] = Field(alias="whatever",default=None)


@app.get("/")
def hello() -> MyModel:
    responseA = MyModel(myessentialfield="foo")
    responseA.myoptionalfield = SubModel(entries=[]) # optionalField added in second command
    responseA.myoptionalfield.entries = [1,2,3] # works

    responseB = MyModel(myessentialfield="foo", myoptionalfield = SubModel(entries=[])) # optionalfield directly created
    responseB.myoptionalfield.entries = [1, 2, 3] # raises Error:  Item "None" of "Optional[SubModel]" has no attribute "entries"

    return responseA
