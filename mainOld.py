"""
There are problems with this- ie that google trends gives data as relative to total searches for that amount rather than
total web searches so this is not a fair comparison. It was intended as a project to learn matplotlib and pandas.
"""


# import the libraries
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

pytrendU = TrendReq(hl='en-US', tz=360)

plt.style.use('ggplot')

# search terms for base unis
value_list = ['uoft', 'university of waterloo', 'university of british columbia', 'university of ottawa', 'mcmaster']
_cat = 74
_geo = ''
_gprop = ''
_timeframe = 'today 1-m'

# run model for keywords (can also be competitors)
pytrendU.build_payload(value_list, cat=_cat, timeframe=_timeframe, geo=_geo, gprop=_gprop)
"""
Make second request list and merge returns
"""

# Interest by Region
regiondf = pytrendU.interest_by_region()

# looking at rows where all values are not equal to 0
regiondf = regiondf[(regiondf != 0).all(1)]

# drop all rows that have null values in all columns
regiondf.dropna(how='all', axis=0, inplace=True)


# define array
chart_vals = []

# make an array of scalars for the amounts of searches
for i in range(len(value_list)):
    chart_vals.append(regiondf.iat[0, i]+50)

acceptance_rate_vals = [67, 51, 37, 19, 49]


print("This visualizes Google Trends Data for Canadian University Searches.")

val_pos = [i for i, _ in enumerate(value_list)]

plt.bar(val_pos, chart_vals, color='green')
plt.xlabel("University Name")
plt.ylabel("Search Amount")
plt.title("What Canadian University has the most searches?")

plt.xticks(val_pos, value_list)

plt.show()
