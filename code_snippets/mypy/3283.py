from datetime import datetime, timedelta

data_dic = {idx: []
            for idx in range(len(lcl.msgs['DATA_COL_NAMES']) - 1)}  # type: Dict[int, List[Union[datetime, float]]]

