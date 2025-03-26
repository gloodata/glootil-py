from datetime import datetime

from glootil import Toolbox

tb = Toolbox("my-gd-ext", "My Extension", "My Utility Tools")


@tb.tool
def compound_interest_calculator(
    principal: float = 1.0,
    interest_rate: float = 3.0,
    years: int = 5,
):
    year = datetime.now().year
    amount = principal
    rows = []

    for i in range(0, years + 1):
        interest = amount * (interest_rate / 100)
        rows.append((year + i, amount))
        amount += interest

    return {
        "type": "Table",
        "columns": [("year", "Year"), ("amount", "Amount")],
        "rows": rows,
    }


tb.serve(host="127.0.0.1", port=8087)
