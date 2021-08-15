#!/usr/bin/env python
# coding: utf-8

# # Introduction

# Google Trends gives us an estimate of search volume. Let's explore if search popularity relates to other kinds of data. Perhaps there are patterns in Google's search volume and the price of Bitcoin or a hot stock like Tesla. Perhaps search volume for the term "Unemployment Benefits" can tell us something about the actual unemployment rate? 
# 
# Data Sources: <br>
# <ul>
# <li> <a href="https://fred.stlouisfed.org/series/UNRATE/">Unemployment Rate from FRED</a></li>
# <li> <a href="https://trends.google.com/trends/explore">Google Trends</a> </li>  
# <li> <a href="https://finance.yahoo.com/quote/TSLA/history?p=TSLA">Yahoo Finance for Tesla Stock Price</a> </li>    
# <li> <a href="https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD">Yahoo Finance for Bitcoin Stock Price</a> </li>
# </ul>

# # Import Statements

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates


# # Read the Data
# 
# Download and add the .csv files to the same folder as your notebook.

# In[2]:


df_tesla = pd.read_csv('day74-data/TESLA Search Trend vs Price.csv')

df_btc_search = pd.read_csv('day74-data/Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('day74-data/Daily Bitcoin Price.csv')

df_unemployment = pd.read_csv('day74-data/UE Benefits Search vs UE Rate 2004-19.csv')


# # Data Exploration

# ### Tesla

# **Challenge**: <br>
# <ul>
# <li>What are the shapes of the dataframes? </li>
# <li>How many rows and columns? </li>
# <li>What are the column names? </li>
# <li>Complete the f-string to show the largest/smallest number in the search data column</li> 
# <li>Try the <code>.describe()</code> function to see some useful descriptive statistics</li>
# <li>What is the periodicity of the time series data (daily, weekly, monthly)? </li>
# <li>What does a value of 100 in the Google Trend search popularity actually mean?</li>
# </ul>

# In[19]:


df_tesla.head()


# In[17]:


print(f'Largest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].max()}')
print(f'Smallest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].min()}')


# In[27]:


df_tesla.describe()


# ### Unemployment Data

# In[32]:


df_unemployment.head()


# In[25]:


print('Largest value for "Unemployemnt Benefits" '
      f'in Web Search: {df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()}')


# ### Bitcoin

# In[22]:


df_btc_search.head()


# In[23]:


df_btc_price.head()


# In[26]:


print(f'largest BTC News Search: {df_btc_search["BTC_NEWS_SEARCH"].max()}')


# # Data Cleaning

# ### Check for Missing Values

# **Challenge**: Are there any missing values in any of the dataframes? If so, which row/rows have missing values? How many missing values are there?

# In[30]:


print(f'Missing values for Tesla?: {df_tesla.isnull().values.any()}')
print(f'Missing values for U/E?: {df_unemployment.isnull().values.any()}')
print(f'Missing values for BTC Search?: {df_btc_search.isnull().values.any()}')


# In[31]:


print(f'Missing values for BTC price?: {df_btc_price.isnull().values.any()}')


# In[4]:


df_btc_price[df_btc_price['CLOSE'].isnull()]


# In[42]:


print(f'Number of missing values: {df_btc_price.isnull().values.any().sum()}')


# **Challenge**: Remove any missing values that you found. 

# In[3]:


df_btc_price = df_btc_price.dropna()


# ### Convert Strings to DateTime Objects

# **Challenge**: Check the data type of the entries in the DataFrame MONTH or DATE columns. Convert any strings in to Datetime objects. Do this for all 4 DataFrames. Double check if your type conversion was successful.

# In[44]:


df_tesla.info()


# In[4]:


df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])


# In[46]:


df_tesla.info()


# In[47]:


df_unemployment.info()


# In[5]:


df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])


# In[33]:


df_unemployment.info()


# In[50]:


df_btc_search.info()


# In[6]:


df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])


# In[53]:


df_btc_search.info()


# In[54]:


df_btc_price.info()


# In[7]:


df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])


# In[57]:


df_btc_price.info()


# ### Converting from Daily to Monthly Data
# 
# [Pandas .resample() documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html) <br>

# In[8]:


df_btc_monthly = df_btc_price.resample(rule='M', on='DATE').last()


# In[31]:


df_btc_monthly.head()


# In[20]:


df_btc_monthly.columns


# # Data Visualisation

# ### Notebook Formatting & Style Helpers

# In[22]:


# Create locators for ticks on the time axis


# In[21]:


# Register date converters to avoid warning messages


# ### Tesla Stock Price v.s. Search Volume

# **Challenge:** Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes. Label one axis 'TSLA Stock Price' and the other 'Search Trend'. 

# In[33]:


plt.figure(figsize=(16,14))
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Volume', color='royalblue', fontsize=16)
ax2.set_ylabel('Close Price', color='#e50000', fontsize=16)

ax1.plot(df_btc_monthly['DATE'], df_btc_monthly['VOLUME'], color='royalblue')
ax2.plot(df_btc_monthly['DATE'], df_btc_monthly['CLOSE'], color='#e50000', animated=True)


# **Challenge**: Add colours to style the chart. This will help differentiate the two lines and the axis labels. Try using one of the blue [colour names](https://matplotlib.org/3.1.1/gallery/color/named_colors.html) for the search volume and a HEX code for a red colour for the stock price. 
# <br>
# <br>
# Hint: you can colour both the [axis labels](https://matplotlib.org/3.3.2/api/text_api.html#matplotlib.text.Text) and the [lines](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D) on the chart using keyword arguments (kwargs).  

# In[ ]:


plt.figure(figsize=(16,14))
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Volume', color='royalblue', fontsize=16)
ax2.set_ylabel('Close Price', color='#e50000', fontsize=16)

ax1.plot(df_btc_monthly['DATE'], df_btc_monthly['VOLUME'], color='royalblue')
ax2.plot(df_btc_monthly['DATE'], df_btc_monthly['CLOSE'], color='#e50000', animated=True)


# **Challenge**: Make the chart larger and easier to read. 
# 1. Increase the figure size (e.g., to 14 by 8). 
# 2. Increase the font sizes for the labels and the ticks on the x-axis to 14. 
# 3. Rotate the text on the x-axis by 45 degrees. 
# 4. Make the lines on the chart thicker. 
# 5. Add a title that reads 'Tesla Web Search vs Price'
# 6. Keep the chart looking sharp by changing the dots-per-inch or [DPI value](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.figure.html). 
# 7. Set minimum and maximum values for the y and x axis. Hint: check out methods like [set_xlim()](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.set_xlim.html). 
# 8. Finally use [plt.show()](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.show.html) to display the chart below the cell instead of relying on the automatic notebook output.

# In[60]:


plt.figure(figsize=(14,8), dpi=500)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Volume', color='royalblue', fontsize=14)
ax2.set_ylabel('Close Price', color='#e50000', fontsize=14)
ax1.set_xlim(dt.date(year=2014, month=9, day=30), dt.date(year=2020, month=10, day=31))
ax1.set_ylim(0, 70000000000)
ax2.set_ylim(0, 14500)

ax1.plot(df_btc_monthly['DATE'], df_btc_monthly['VOLUME'], color='royalblue', linewidth=5)
ax2.plot(df_btc_monthly['DATE'], df_btc_monthly['CLOSE'], color='#e50000', linewidth=5)

plt.title('BTC Close Price and Volume vs Date', fontsize=14)
plt.show()


# How to add tick formatting for dates on the x-axis. 

# In[66]:


years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

plt.figure(figsize=(14,8), dpi=500)
plt.yticks(fontsize=14)
plt.xticks(fontsize=14, rotation=45)
ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Volume', color='royalblue', fontsize=14)
ax2.set_ylabel('Close Price', color='#e50000', fontsize=14)
ax1.set_xlim(dt.date(year=2014, month=9, day=30), dt.date(year=2020, month=10, day=31))
ax1.set_ylim(0, 70000000000)
ax2.set_ylim(0, 14500)
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_minor_locator(months)
ax1.xaxis.set_major_formatter(years_fmt)

ax1.plot(df_btc_monthly['DATE'], df_btc_monthly['VOLUME'], color='royalblue', linewidth=5)
ax2.plot(df_btc_monthly['DATE'], df_btc_monthly['CLOSE'], color='#e50000', linewidth=5)

plt.title('BTC Close Price and Volume vs Date', fontsize=14)
plt.show()


# ### Bitcoin (BTC) Price v.s. Search Volume

# **Challenge**: Create the same chart for the Bitcoin Prices vs. Search volumes. <br>
# 1. Modify the chart title to read 'Bitcoin News Search vs Resampled Price' <br>
# 2. Change the y-axis label to 'BTC Price' <br>
# 3. Change the y- and x-axis limits to improve the appearance <br>
# 4. Investigate the [linestyles](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html ) to make the BTC price a dashed line <br>
# 5. Investigate the [marker types](https://matplotlib.org/3.2.1/api/markers_api.html) to make the search datapoints little circles <br>
# 6. Were big increases in searches for Bitcoin accompanied by big increases in the price?

# In[30]:


plt.figure(figsize=(14,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Bitcoin News Search vs Resampled Price', fontsize=14)

ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('BTC Price', fontsize=14, color='g')
ax2.set_ylabel('Search Volume', fontsize= 14, color='b')
ax1.set_xlim(df_btc_monthly['DATE'].min(), df_btc_monthly['DATE'].max())
ax1.set_ylim(0, 14500)
ax2.set_ylim(0, df_btc_monthly['VOLUME'].max())

ax1.plot(df_btc_monthly['DATE'], df_btc_monthly['CLOSE'], color='g', linestyle='--')
ax2.plot(df_btc_monthly['DATE'], df_btc_monthly['VOLUME'], color='b', marker='o')


# In[ ]:





# ### Unemployement Benefits Search vs. Actual Unemployment in the U.S.

# **Challenge** Plot the search for "unemployment benefits" against the unemployment rate. 
# 1. Change the title to: Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate <br>
# 2. Change the y-axis label to: FRED U/E Rate <br>
# 3. Change the axis limits <br>
# 4. Add a grey [grid](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.grid.html) to the chart to better see the years and the U/E rate values. Use dashes for the line style<br> 
# 5. Can you discern any seasonality in the searches? Is there a pattern? 

# In[41]:


plt.figure(figsize=(14,10))
plt.grid(b=True, linestyle='--')
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14, rotation=45)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=14)

ax1 = plt.gca()
ax2 = plt.twinx()
ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('Search Volume', fontsize=14, color='g')
ax2.set_ylabel('Unemployment Rate', fontsize=14, color='b')
ax1.set_xlim(df_unemployment['MONTH'].min(), df_unemployment['MONTH'].max())
ax1.set_ylim(0, 110)
ax2.set_ylim(0, 15)

ax1.plot(df_unemployment['MONTH'], df_unemployment['UE_BENEFITS_WEB_SEARCH'], color='g', marker='o')
ax2.plot(df_unemployment['MONTH'], df_unemployment['UNRATE'], color='b', linestyle='--')


# **Challenge**: Calculate the 3-month or 6-month rolling average for the web searches. Plot the 6-month rolling average search data against the actual unemployment. What do you see in the chart? Which line moves first?
# 

# In[45]:


plt.figure(figsize=(14,10))
plt.grid(b=True, linestyle='--')
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14, rotation=45)
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=14)

ax1 = plt.gca()
ax2 = plt.twinx()
ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('Search Volume', fontsize=14, color='g')
ax2.set_ylabel('Unemployment Rate', fontsize=14, color='b')
ax1.set_xlim(df_unemployment['MONTH'].min(), df_unemployment['MONTH'].max())
ax2.set_ylim(3, 10.5)

ax1.plot(df_unemployment['MONTH'], df_unemployment['UE_BENEFITS_WEB_SEARCH'].rolling(6).mean(), color='g', marker='o')
ax2.plot(df_unemployment['MONTH'], df_unemployment['UNRATE'].rolling(6).mean(), color='b', linestyle='--')


# ### Including 2020 in Unemployment Charts

# **Challenge**: Read the data in the 'UE Benefits Search vs UE Rate 2004-20.csv' into a DataFrame. Convert the MONTH column to Pandas Datetime objects and then plot the chart. What do you see?

# In[56]:


df_unemployment2020 = pd.read_csv('day74-data/UE Benefits Search vs UE Rate 2004-20.csv', parse_dates=['MONTH'])
df_unemployment2020.head()


# In[64]:


plt.figure(figsize=(14, 10))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14, rotation=45)

ax1 = plt.gca()
ax2 = plt.twinx()

ax1.set_xlabel('Date', fontsize=14)
ax1.set_ylabel('Search Volume', fontsize=14, color='g')
ax2.set_ylabel('Unemployment Rate', fontsize=14, color='b')
ax1.set_xlim(df_unemployment2020['MONTH'].min(), df_unemployment2020['MONTH'].max())

ax1.plot(df_unemployment2020['MONTH'], df_unemployment2020['UE_BENEFITS_WEB_SEARCH'].rolling(6).mean(), color='g', linestyle='--')
ax2.plot(df_unemployment2020['MONTH'], df_unemployment2020['UNRATE'].rolling(6).mean(), color='b')


# In[29]:




