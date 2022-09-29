# surfs_up
## Overview

For this challenge project, we analyzed weather data on the Hawaiian island of Oahu. The goal was to evaluate the viability of opening a combination surf shop/ice cream parlor according to the weather patterns on different parts of the island. To accomplish this task, we were provided an sqlite database with several years' worth of weather data recorded at a number of weather stations around the island.

Throughout the module, we learned to use SQLAlchemy and Pandas tools to examine the weather over the course of the most recent year's worth of available data, ending in August 2017. For this challenge we shifted focus to analyzing the data in only the months June and December, but from all available years. The logic behind this direction is to ensure that a combination surf shop/ice cream parlor would be a viable buisness venture year-round. So, by examining several years' woth of data during the time around both the summer and winter solstices, we can get a better idea of how weather patterns on the island vary over the course of a whole year.

### Resources

- Data: hawaii.sqlite
- Software: Python 3.7.13, Anaconda command line client 1.9.0, Conda 4.13.0, Jupyter Notebook 6.4.8, Pandas 1.3.5, NumPy 1.21.5, SQLAlchemy 1.4.32

## Results

Two queries were constructed in order to filter the database's temperature data, restricting the results to June and December datapoints, respectively. The relevant data were extracted from the database and converted into a DataFrame to derive descriptive statistics for the temperatures recorded in the months of interest.

![June Temperatures](https://github.com/tfish110/surfs_up/blob/main/resources/june_temps_stats.png)
![December Temperatures](https://github.com/tfish110/surfs_up/blob/main/resources/december_temps_stats.png)

These tables contain the descriptive statistics for the two relevant months' observed temperature records. Based on these temperature means and standard deviations, there seems to be  minimal differences between the temperatures in June vs. December.

- With means of approximately 75 and 71 degrees for June and December, respectively, there doesn't appear to be a significant difference in these two months at polar opposite ends of the year.
- The standard deviation for June datapoints is approximately 3.25, and for December datapoints is approximately 3.75. These similar standard deviations suggest consistency in the range that temperature varies for each month across all availble years' worth of data, regardless of whether it is winter or summer.
- The biggest difference that we see here is in the minimum temperature; the minimum December temperature is about 8 degrees lower than the minimum June temperature. This is in contrast the the quartile and maximum temperatures, which only vary by 2 to 4 degrees between June and December.

## Summary

Overall, these are very promising results for the proposed buisness to operate as a year-round business. With such small variations in temperature between summer and winter, seasonal temperature shifts should have little to no impact on attracting customers. Even the largest difference between the June and December datapoints, minimum temperature, could very likely be an outlier in the dataset. Because all the other descriptive statistics are so similar between these opposite times of year, it's very reasonable to assume that an occasional chilly day in December is rare enough not to make a significant impact on business.

It is important to consider that temperature is not the only weather consideration for this type of business. In the tropical latitudes where Oahu lies, it is quite common for summer and winter to be differentiated by precipitation rather than temperature. In that sense, this business's seasonal differences might better be described as a wet vs. dry season rather than summer vs. winter. So, it would be prudent to query the database focusing on the difference in precipitation in June and December to get a sense if that might be the case.

In addition to the differences in a wet vs. dry season, wind measurements might also be taken into consideration. If the aforementioned query does indicate that there is a wet season, does that rain come down in a consistent daily pattern? Or is there perhaps a series of severe storms that drives precipitation during a wet season? This would certainly be relevant information for a combination shop like this. While severe weather might stop people from sunbathing and wanting a cool off with some ice cream, it can also bring bigger waves which might actually attract an increase in the surf shop side of the business. So additional queries to get a sense of weather conditions and wind speed could be helpful to correlate with precipitation and determine potential fluctuations in the surf aspect of the business vs. the ice cream aspect.