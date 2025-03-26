from glootil import Toolbox

tb = Toolbox("my-gd-ext", "My Extension", "My Utility Tools")


@tb.tool
def compound_interest_calculator(
    principal: float = 1.0,
    interest_rate: float = 3.0,
    years: int = 5,
):
    amount = principal
    rows = []

    for i in range(0, years + 1):
        interest = amount * (interest_rate / 100)
        rows.append((i, amount))
        amount += interest

    return "\n".join(f"- {i}: ${round(amount, 2)}" for i, amount in rows)


tb.serve(host="127.0.0.1", port=8087)
