@dataclass
class Order:  # the Context
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], float]] = None  # the Strategy

class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], float]] = None  # the Strategy
