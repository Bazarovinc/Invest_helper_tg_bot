from .convert import convert
from decimal import Decimal


def currency(cur: str) -> str:
    if '-' not in cur and cur.isalpha():
        result = convert(Decimal("1.0"), cur, 'RUR')
    elif '-' in cur and '/' in cur:
        cur, date = cur.split('-')
        result = convert(Decimal("1.0"), cur, 'RUR', date)
    else:
        return "Error in message!"
    return f"{cur}/RUR: {result}"
