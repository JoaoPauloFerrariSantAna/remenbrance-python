from typing import Union
from operation_statuses import OpErrors, OpSuccess

type OpStatus = Union[OpErrors, OpSuccess]
