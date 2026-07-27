"""
Efficient Frontier Generator.
"""

from calculators.portfolio_return import (
    calculate_portfolio_return,
)

from calculators.portfolio_volatility import (
    portfolio_volatility,
)


def generate_frontier(
    portfolios,
):
    """
    Generate efficient frontier points.

    Parameters
    ----------
    portfolios : list

    Returns
    -------
    list
    """

    frontier = []

    for portfolio in portfolios:

        frontier.append(

            {

                "return":
                calculate_portfolio_return(
                    portfolio["returns"],
                ),

                "volatility":
                portfolio_volatility(
                    portfolio["weights"],
                    portfolio["volatility"],
                ),

                "weights":
                portfolio["weights"],

            }

        )

    frontier.sort(

        key=lambda x: (
            x["volatility"],
            -x["return"],
        )

    )

    return frontier
