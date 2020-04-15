# importing important modules
import io
import pandas as pandas
import matplotlib.pyplot as plotter

gdpData = pandas.read_csv('gdp.csv')
# retreving data for United States
unitedStatesData = gdpData[gdpData.Country_Name == "United States"]
# retreving data for India
indiaData = gdpData[gdpData.Country_Name == "India"]
# retreving data for China
chinaData = gdpData[gdpData.Country_Name == "China"]
# retreving data for United Kingdom
unitedKingdomData = gdpData[gdpData.Country_Name == "United Kingdom"]

# plotting data from the CSV file to compare different GDP Rates
plotter.plot(unitedStatesData.Year, unitedStatesData.Value / 10**10)
plotter.plot(indiaData.Year, indiaData.Value / 10**10)
plotter.plot(chinaData.Year, chinaData.Value / 10**10)
plotter.plot(unitedKingdomData.Year, unitedKingdomData.Value / 10**10)
plotter.title("GDP Index")
plotter.xlabel("Year")
plotter.ylabel("GDP in Billion Dollars($)")
plotter.legend(["United States of America (USA)", "India (IND)", "China (CHN)", "United Kingdom (UK)"])
plotter.show()
