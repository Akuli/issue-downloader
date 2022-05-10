SeriesOfBool = NewType("SeriesOfBool", Annotated[pandas.Series, "bool"])

def is_series_of_bool(series: pandas.Series) -> TypeGuard[SeriesOfBool]:
    return series.dtype == "bool"
