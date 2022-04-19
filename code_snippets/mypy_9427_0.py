from decimal import Decimal
from collections import OrderedDict

GRID = OrderedDict(sorted({
    (93, 659): Decimal('0.3000'), (93, 714): Decimal('0.2950'), (93, 749): Decimal('0.2820'), (93, 799): Decimal('0.2690'), (93, 850): Decimal('0.1990'),  # noqa: E501
    (94, 659): Decimal('0.3000'), (94, 714): Decimal('0.2900'), (94, 749): Decimal('0.2745'), (94, 799): Decimal('0.2590'), (94, 850): Decimal('0.1820'),  # noqa: E501
    (95, 659): Decimal('0.3000'), (95, 714): Decimal('0.2850'), (95, 749): Decimal('0.2620'), (95, 799): Decimal('0.2390'), (95, 850): Decimal('0.1620'),  # noqa: E501
    (96, 659): Decimal('0.3000'), (96, 714): Decimal('0.2800'), (96, 749): Decimal('0.2495'), (96, 799): Decimal('0.2190'), (96, 850): Decimal('0.1570'),  # noqa: E501
    (97, 659): Decimal('0.2800'), (97, 714): Decimal('0.2750'), (97, 749): Decimal('0.2370'), (97, 799): Decimal('0.1990'), (97, 850): Decimal('0.1520'),  # noqa: E501
    (98, 659): Decimal('0.2710'), (98, 714): Decimal('0.2650'), (98, 749): Decimal('0.2220'), (98, 799): Decimal('0.1790'), (98, 850): Decimal('0.1470'),  # noqa: E501
    (99, 659): Decimal('0.2500'), (99, 714): Decimal('0.1990'), (99, 749): Decimal('0.1975'), (99, 799): Decimal('0.1670'), (99, 850): Decimal('0.1170'),  # noqa: E501
    (100, 659): Decimal('0.2500'), (100, 714): Decimal('0.1890'), (100, 749): Decimal('0.1500'), (100, 799): Decimal('0.1084'), (100, 850): Decimal('0.1000'),  # noqa: E501
}.items()))

