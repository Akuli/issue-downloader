np = load_numpy()  # def load_numpy() -> ??:

x = np.array(123)  # << I want to have auto-complete & type checking here

if typing.TYPE_CHECKING:
  import numpy as np


def load_numpy() -> Literal[np]:
  import numpy as np
  return np
