#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:44:40 2024

@author: jmr
"""

import matplotlib.pyplot as plt

# Line Chart
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temperature = [20, 22, 21, 23, 19]
plt.plot(days, temperature)
plt.xlabel('Day')
plt.ylabel('Temperature (C)')
plt.title('Temperature Over a Week')
plt.show()
# Bar Chart
cities = ['City A', 'City B', 'City C', 'City D']
population = [300000, 450000, 200000, 500000]
plt.bar(cities, population, color='lightcoral')
plt.xlabel('City')
plt.ylabel('Population')
plt.title('City Population')
plt.show()
# Pie Chart
market_share = [35, 25, 20, 15, 5]
labels = ['Company A', 'Company B', 'Company C', 'CompanyD', 'Others']
plt.pie(market_share, labels=labels, autopct='%1.1f%%',startangle=180)
plt.title('Market Share of Companies')
plt.show()


