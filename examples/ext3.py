from datetime import datetime

from glootil import Toolbox

tb = Toolbox("my-gd-ext", "My Extension", "My Utility Tools")


@tb.tool(
    name="Compound Interest Rate Calculator",
    examples=[
        "calculate compound interest for initial 1500 dollars, 2.5% interests for 8 years",
        "compound interst for $2000 at 3.5% interests for 10 years",
    ],
)
def compound_interest_calculator(
    principal: float = 1.0,
    interest_rate: float = 3.0,
    years: int = 5,
):
    year = datetime.now().year
    amount = principal
    cols = [("year", "Year"), ("amount", "Amount")]
    rows = []

    for i in range(0, years + 1):
        interest = amount * (interest_rate / 100)
        rows.append((year + i, amount))
        amount += interest

    return {
        "type": "Series",
        "title": "Compound Interest by Year",
        "xColTitle": "Year",
        "yColTitle": "$",
        "xCol": "year",
        "valCols": ["amount"],
        "cols": cols,
        "rows": rows,
    }


tb.serve(host="127.0.0.1", port=8087)
