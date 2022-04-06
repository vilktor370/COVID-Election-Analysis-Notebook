import pandas as pd
import os

from sympy import EX
"""_summary_
    TODO
"""

ELECTION16 = 'Election2016'
ELECTION20 = 'Election2020'
COVID = 'COVID'

def load_csv():
    """
    TODO: docstring
    """

    president_state = pd.read_csv(os.path.join(ELECTION20,'president_state.csv'))
    president_county_candidate = pd.read_csv(os.path.join(ELECTION20,'president_county_candidate.csv'))
    us_covid19_daily = pd.read_csv(os.path.join(COVID,'us_covid19_daily.csv'))
    us_counties_covid19_daily = pd.read_csv(os.path.join(COVID,'us_counties_covid19_daily.csv'))
    return president_state, president_county_candidate, us_covid19_daily, us_counties_covid19_daily
load_csv()