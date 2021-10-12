import datetime

import matplotlib.dates
import matplotlib.pyplot


class Plot:
    def draw(self, hours, temperatures):
        dates = matplotlib.dates.date2num(hours)
        matplotlib.pyplot.plot_date(dates, temperatures, linestyle="-")
        matplotlib.pyplot.show(block=True)
