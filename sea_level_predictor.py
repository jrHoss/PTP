import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
  fig, ax = plt.subplots()
  ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    # Create first line of best fit
  lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  xA = np.arange(df['Year'].min(),2050)
  yA = xA * lineA.slope + lineA.intercept
  plt.plot(xA,yA)

    # Create second line of best fit
  df_2000 = df[df['Year'] >= 2000]
  ax.scatter(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
  lineB = linregress(df_2000["Year"],df_2000["CSIRO Adjusted Sea Level"])
  xB = np.arange(df_2000["Year"].min(),2050,1)
  yB = xB * lineB.slope + lineB.intercept
  ax.plot(xB,yB)

  # Add labels and title
  ax.set_title("Rise in Sea Level")
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()