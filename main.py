#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse how many visitors come to Singapore within range of years for each Region
#Name: Daniel
#Group Name: OCK
#Class: PN2004J
#Date: 9/2/21
#Version: 1
########################################################
#######################################################
#import Pandas Library for Data Analysis
import pandas as pd
#######################################################

#######################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
############################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - "df"
    dataframe = pd.read_csv("MonthlyVisitors.csv")
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

def sortCountry(df):

  #Display sorted dataframe for Asia Pacific Region
  print("\n\n"+"Asia Pacific region was selected.")

  #Display sorted dataframe base on given year range of region (2007-2017)
  print("The countries in the region are shown below.")
  print(" Year range: 2007 - 2017" + "\n")
  asiapacific_region = df.iloc[348:, 9:14]
  year_month = df.iloc[348:,0:2]

  #Display Year,Month,Country and no. of visitors
  result = year_month.join(asiapacific_region)
  print("Total number of countries:", str(len(result.columns) - 2) + "\n")
  print(result)

  #Display the top 3 countries that visited Singapore over the span of 10 years 
  print("\n"+"The Top 3 countries of visitors to Singapore from the selected region over the span of 10 years: ")
  Top3Countries=df.iloc[348:,9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
  print(Top3Countries)
  return 
  



#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == "__main__":
  
  #Project Title
  print("######################################")
  print("# Data Analysis App - PYTHON Project #")
  print("######################################")
  
  

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

  #read excel data 
  df = pd.read_csv("MonthlyVisitors.csv")


  #Display all Region option
  print("\n")
  print("[1]South East Asia")
  print("[2]Asia Pacific")
  print("[3]South Asia Pacific")
  print("[4]Middle East")
  print("[5]Europe")
  print("[6]North America")
  print("[7]Australia")
  print("[8]Africa")
  print("\n")
  

  #All acceptable inputs
  Regions = ["South East Asia","Asia Pacific","South Asia Pacific", "Middle East", "Europe","North America","Australia","Africa","south east asia","asia pacific","south asia pacific", "middle east", "europe","north america","australia","africa","1","2","3","4","5","6","7","8"]
  

  #Error checking for all Regions
  while True:
    x = 0
    Region = input("Enter a Region: ")
    if not Region in Regions:
      print("Error, Please input the options given!")

    elif Region in Regions:
      if Region == "South East Asia" or Region== "south east asia" or Region== "1":
        sea_region = df.iloc[:, 2:9]
        x += 10
        print("\n","##############[South East Asia Region Selected]#############")
        break
      elif Region == "Asia Pacific" or Region== "asia pacific" or Region== "2":
        ap_region = df.iloc[:,9:14]
        x += 20
        print("\n","##############[Asia Pacific Region Selected]#############")
        break
      elif Region == "South Asia Pacific" or Region== "south asia pacific" or Region== "3":
        sap_region = df.iloc[:,14:17]
        x += 30
        print("\n","##############South Asia Pacific Region Selected]#############")
        break
      elif Region == "Middle East" or Region== "middle east" or Region== "4":
        me_region = df.iloc[:,17:20]
        x += 40
        print("\n","##############[Middle East Region Selected]#############")
        break
      elif Region == "Europe" or Region== "europe" or Region== "5":
        eu_region = df.iloc[:,20:31]
        x += 50
        print("\n","##############[Europe Region Selected]#############")
        break
      elif Region == "North America" or Region== "north america" or Region== "6":
        na_region = df.iloc[:,31:33]
        x += 60
        print("\n","##############[North America Region Selected]#############")
        break
      elif Region == "Australia" or Region== "australia"  or Region== "7":
        au_region = df.iloc[:,33:35]
        x += 70
        print("\n","##############[Australia Region Selected]#############")
        break
      elif Region == "Africa" or Region== "africa" or Region== "8":
        af_region = df.iloc[:,35:36]
        x += 80
        print("\n","##############[Africa Region Selected]#############")
        break



  #Years error checking for all region

    df = pd.read_csv("MonthlyVisitors.csv")

  #Display Range of Year option
  print("[1]1978-1984")
  print("[2]1985-1995")
  print("[3]1996-2006")
  print("[4]2007-2017")
  
  #South East Asia Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]

  if x == 10:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          SEA = df.iloc[0:84,2:9]
          result=year_range.join(SEA)
          print(result)
          Countries=df.iloc[0:84,2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          SEA = df.iloc[84:216,2:9]
          result=year_range.join(SEA)
          print(result)
          Countries=df.iloc[84:216,2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          SEA = df.iloc[216:348,2:9]
          result=year_range.join(SEA)
          print(result)
          Countries=df.iloc[216:348,2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          SEA = df.iloc[348:,2:9]
          result=year_range.join(SEA)
          print(result)
          Countries=df.iloc[348:,2:9].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break


  #Asia Pacific Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4",]
  if x == 20:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          AP = df.iloc[0:84,9:14]
          result=year_range.join(AP)
          print(result)
          Countries=df.iloc[0:84,9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1

          break
        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          AP = df.iloc[84:216,9:14]
          result=year_range.join(AP)
          print(result)
          Countries=df.iloc[84:216,9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          AP = df.iloc[216:348,9:14]
          result=year_range.join(AP)
          print(result)
          Countries=df.iloc[216:348,9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          AP = df.iloc[348:,9:14]
          result=year_range.join(AP)
          print(result)
          Countries=df.iloc[348:,9:14].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #South Asia Pacific Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 30:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          SAP = df.iloc[0:84,14:17]
          result=year_range.join(SAP)
          print(result)
          Countries=df.iloc[0:84,14:17].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          SAP = df.iloc[84:216,14:17]
          result=year_range.join(SAP)
          print(result)
          Countries=df.iloc[84:216,14:17].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          SAP = df.iloc[216:348,14:17]
          result=year_range.join(SAP)
          print(result)
          Countries=df.iloc[216:348,14:17].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          SAP = df.iloc[348:,14:17]
          result=year_range.join(SAP)
          print(result)
          Countries=df.iloc[348:,14:17].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #Middle-East Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 40:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          southasiapacific = df.iloc[0:84,17:20]
          result=year_range.join(southasiapacific)
          print(result)
          Countries=df.iloc[0:84,17:20].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          southasiapacific = df.iloc[84:216,17:20]
          result=year_range.join(southasiapacific)
          print(result)
          Countries=df.iloc[84:216,17:20].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          southasiapacific = df.iloc[216:348,17:20]
          result=year_range.join(southasiapacific)
          print(result)
          Countries=df.iloc[216:348,17:20].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          southasiapacific = df.iloc[348:,17:20]
          result=year_range.join(southasiapacific)
          print(result)
          Countries=df.iloc[348:,17:20].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #Europe Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 50:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          EU = df.iloc[0:84,20:31]
          result=year_range.join(EU)
          print(result)
          Countries=df.iloc[0:84,20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          EU = df.iloc[84:216,20:31]
          result=year_range.join(EU)
          print(result)
          Countries=df.iloc[84:216,20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          EU = df.iloc[216:348,20:31]
          result=year_range.join(EU)
          print(result)
          Countries=df.iloc[216:348,20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          EU = df.iloc[348:,20:31]
          result=year_range.join(EU)
          print(result)
          Countries=df.iloc[348:,20:31].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #North-America Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 60:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          NA = df.iloc[0:84,31:33]
          result=year_range.join(NA)
          print(result)
          Countries=df.iloc[0:84,31:33].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          NA = df.iloc[84:216,31:33]
          result=year_range.join(NA)
          print(result)
          Countries=df.iloc[84:216,31:33].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          NA = df.iloc[216:348,31:33]
          result=year_range.join(NA)
          print(result)
          Countries=df.iloc[216:348,31:33].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          NA = df.iloc[348:,31:33]
          result=year_range.join(NA)
          print(result)
          Countries=df.iloc[348:,31:33].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #Australia Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 70:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          AU = df.iloc[0:84,33:35]
          result=year_range.join(AU)
          print(result)
          Countries=df.iloc[0:84,33:35].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          AU = df.iloc[84:216,33:35]
          result=year_range.join(AU)
          print(result)
          Countries=df.iloc[84:216,33:35].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          AU = df.iloc[216:348,33:35]
          result=year_range.join(AU)
          print(result)
          Countries=df.iloc[216:348,33:35].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          AU = df.iloc[348:,33:35]
          result=year_range.join(AU)
          print(result)
          Countries=df.iloc[348:,33:35].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break

  #Africa Region error checkling
  Years = ["1978-1984","1985-1995","1996-2006","2007-2017","1","2","3", "4"]
  if x == 80:
    while True:
      Year = input("Select a range of years []: ")
      if not Year in Years:
        print("Error, Please try again!")

      elif Year in Years:
        if Year == "1" or Year == "1978-1984":
          year_range = df.iloc[0:84, 0:2]
          AF = df.iloc[0:84,35:36]
          result=year_range.join(AF)
          print(result)
          Countries=df.iloc[0:84,35:36].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 1
          break

        elif Year == "2" or Year == "1985-1995":
          year_range = df.iloc[84:216, 0:2]
          AF = df.iloc[84:216,35:36]
          result=year_range.join(AF)
          print(result)
          Countries=df.iloc[84:216,35:36].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 2
          break

        elif Year == "3" or Year == "1996-2006":
          year_range = df.iloc[216:348, 0:2]
          AF = df.iloc[216:348,35:36]
          result=year_range.join(AF)
          print(result)
          Countries=df.iloc[216:348,35:36].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 3
          break

        elif Year == "4" or Year == "2007-2017":
          year_range = df.iloc[348:,0:2]
          AF = df.iloc[348:,35:36]
          result=year_range.join(AF)
          print(result)
          Countries=df.iloc[348:,35:36].sum(axis=0).sort_values(ascending=False).nlargest(3)
          print(Countries)
          x += 4
          break
          

  #Pie Chart
  import matplotlib.pyplot as plt



 
    
  #South East Asia Region from 1978-1984
  if x == 11:
    print("###########Sorry! there were No Visitors during this period#############")

  #South East Asia Region from 1985-1995
  if x == 12:
    print("###########Sorry! there were No Visitors during this period#############")
    
  
  #South East Asia Region from 1996-2006
  if x == 13:
    SEA3 = ["Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", " Vietnam", "Myanmar"]
    slices = [601772, 15288142, 6292852, 2323026, 2961107, 667954, 267938]
    colours = ["#F8F22A", "r", "b", "y", "crimson", "#FFFB00", "#8EFC01"]
    
    plt.pie(slices,
        labels=SEA3,
        startangle=90,
        shadow=True,
        colors=colours,
        explode=(0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #South East Asia Region from 2007-2017
  if x == 14:
    SEA4 = ["Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", " Vietnam", "Myanmar"]
    slices = [715883, 27572424, 11337420, 6548622, 4945136, 3914607, 1042608]
    colours = ["#F8F22A", "r", "b", "y", "crimson", "#FFFB00", "#8EFC01"]
   
    plt.pie(slices,
        labels=SEA4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()


  #Asia Pacific Region from 1978-1984
  if x == 21:
    AP1 = [" Japan", "Hong Kong", "China", "Taiwan", "Republic of Korea"]
    slices = [2220435, 567258, 11093, 407104, 164393]
    colours = ["r", "y", "crimson", "b", "#004CFB"]
   
    plt.pie(slices,
        labels=AP1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Asia Pacific Region from 1985-1995
  if x == 22:
    AP2 = [" Japan", "Hong Kong", "China", "Taiwan", "Republic of Korea"]
    slices = [8979753, 2042240, 839684, 3106422, 1474780]
    colours = ["r", "y", "crimson", "b", "#004CFB"]
   
    plt.pie(slices,
        labels=AP2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Asia Pacific Region from 1996-2006
  if x == 23:
    AP3 = [" Japan", "Hong Kong", "China", "Taiwan", "Republic of Korea"]
    slices = [8595057, 3017823, 6073384, 3191138, 3550115]
    colours = ["r", "y", "crimson", "b", "#004CFB"]
   
    plt.pie(slices,
        labels=AP3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Asia Pacific Region from 2007-2017
  if x == 24:
    AP4 = [" Japan", "Hong Kong", "China", "Taiwan", "Republic of Korea"]
    slices = [7557929, 4946522, 19857410, 3086819,  5120273]
    colours = ["r", "y", "crimson", "b", "#004CFB"]
   
    plt.pie(slices,
        labels=AP4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #South Asia Pacific Region from 1978-1984
  if x == 31:
    SAP1 = ["India","Pakistan","Sri Lanka"]
    slices = [797049, 98771, 131082]
    colours = ["#FB7500","#207807","#FFC300"]
   
    plt.pie(slices,
        labels=SAP1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #South Asia Pacific Region from 1985-1995
  if x == 32:
    SAP2 = ["India","Pakistan","Sri Lanka"]
    slices = [2259950, 385747, 476109]
    colours = ["#FB7500","#207807","#FFC300"]
   
    plt.pie(slices,
        labels=SAP2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()
  #South Asia Pacific Region from 1996-2006
  if x == 33:
    SAP3 = ["India","Pakistan","Sri Lanka"]
    slices = [4047581, 311922, 646776]
    colours = ["#FB7500","#207807","#FFC300"]
   
    plt.pie(slices,
        labels=SAP3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()
  #South Asia Pacific Region from 2007-2017
  if x == 34:
    SAP4 = ["India","Pakistan","Sri Lanka"]
    slices = [9991342, 232279, 950030]
    colours = ["#FB7500","#207807","#FFC300"]
   
    plt.pie(slices,
        labels=SAP4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()


  #Middle-East Region from 1978-1984
  if x == 41:
    ME1 = ["Saudi Arabia","Kuwait","UAE"]
    slices = [124968, 19578, 51511]
    colours = ["#FFC300","#C70039","#07783A"]
   
    plt.pie(slices,
        labels=ME1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Middle-East Region from 1985-1995
  if x == 42:
    ME2 = ["Saudi Arabia","Kuwait","UAE"]
    slices = [216456, 31990, 145576]
    colours = ["#FFC300","#C70039","#07783A"]
   
    plt.pie(slices,
        labels=ME2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Middle-East Region from 1996-2006
  if x == 43:
    ME3 = ["Saudi Arabia","Kuwait","UAE"]
    slices = [159278, 67010, 236559]
    colours = ["#FFC300","#C70039","#07783A"]
   
    plt.pie(slices,
        labels=ME3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Middle-East Region from 2007-2017
  if x == 44:
    ME4 = ["Saudi Arabia","Kuwait","UAE"]
    slices = [165567, 92375, 705583]
    colours = ["#FFC300","#C70039","#07783A"]
   
    plt.pie(slices,
        labels=ME4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Europe Region from 1978-1984 
  if x == 51:
    EU1 = ["United Kingdom","Germany","France ","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe"]
    slices = [941045,479646,284384,165413,297763,0,36795,165123,0,230669,51942]
    colours = ["#FF5733","#FFC300","#1247D8","#50D812","#D81212","b","#FFDF00","r","#D70B0B","#031CD1","#121B63"]
   
    plt.pie(slices,
        labels=EU1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Europe Region from 1985-1995
  if x == 52:
    EU2 = ["United Kingdom","Germany","France ","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe"]
    slices = [2834621,1522806,709847,531890,715570,155202,177584,582608,180468,818596,397623]
    colours = ["#FF5733","#FFC300","#1247D8","#50D812","#D81212","b","#FFDF00","r","#D70B0B","#031CD1","#121B63"]
   
    plt.pie(slices,
        labels=EU2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Europe Region from 1996-2006
  if x == 53:
    EU3 = ["United Kingdom","Germany","France ","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe"]
    slices = [4569048,1760776,823145,396964,729330,130491,217463,526466,172926,934676,590486]
    colours = ["#FF5733","#FFC300","#1247D8","#50D812","#D81212","b","#FFDF00","r","#D70B0B","#031CD1","#121B63"]
   
    plt.pie(slices,
        labels=EU3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()

  #Europe Region from 2007-2017
  if x == 54:
    EU4 = ["United Kingdom","Germany","France ","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe"]
    slices = [5162602,2649558,1568727,651621,865591,95211,279493,917355,243714,1128958,1626192]
    colours = ["#FF5733","#FFC300","#1247D8","#50D812","#D81212","b","#FFDF00","r","#D70B0B","#031CD1","#121B63"]
   
    plt.pie(slices,
        labels=EU4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0,0,0,0,0,0,0,0,0,0),
        autopct="%1.2f%%")

    plt.show()


  #North-America Region from 1978-1984 
  if x == 61:
    NA1 = ["USA","Canada"]
    slices = [1019339,160723]
    colours = ["#084D83","#D10000"]
   
    plt.pie(slices,
        labels=NA1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #North-America Region from 1985-1995
  if x == 62:
    NA2 = ["USA","Canada"]
    slices = [2849900,573042]
    colours = ["#084D83","#D10000"]
   
    plt.pie(slices,
        labels=NA2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #North-America Region from 1996-2006
  if x == 63:
    NA3 = ["USA","Canada"]
    slices = [3856501,753964]
    colours = ["#084D83","#D10000"]
   
    plt.pie(slices,
        labels=NA3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #North-America Region from 2007-2017
  if x == 64:
    NA4 = ["USA","Canada"]
    slices = [5015088,957576]
    colours = ["#084D83","#D10000"]
   
    plt.pie(slices,
        labels=NA4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #Australia Region from 1978-1984 
  if x == 71:
    AU1 = ["Australia","New Zealand"]
    slices = [1765582,409224]
    colours = ["#1936C5","#061E8F"]
   
    plt.pie(slices,
        labels=AU1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()
  #Australia Region from 1985-1995
  if x == 72:
    AU2 = ["Australia","New Zealand"]
    slices = [4027425,756879]
    colours = ["#1936C5","#061E8F"]
   
    plt.pie(slices,
        labels=AU2,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #Australia Region from 1996-2006
  if x == 73:
    AU3 = ["Australia","New Zealand"]
    slices = [5491694,1011090]
    colours = ["#1936C5","#061E8F"]
   
    plt.pie(slices,
        labels=AU3,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #Australia Region from 2007-2017
  if x == 74:
    AU4 = ["Australia","New Zealand"]
    slices = [10566769,1272109]
    colours = ["#1936C5","#061E8F"]
   
    plt.pie(slices,
        labels=AU4,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0,0),
        autopct="%1.2f%%")

    plt.show()

  #Africa Region from 1978-1984 
  if x == 81:
    AF1 = ["Africa","Africa total"]
    slices = [77970,2411981]
    colours = ["#14B212","g"]
   
    plt.pie(slices,
        labels=AF1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0.1,0),
        autopct="%1.2f%%")

    plt.show()

  #Africa Region from 1985-1995 
  if x == 82:
    AF1 = ["Africa","Africa total"]
    slices = [628798,2411981]
    colours = ["#14B212","g"]
   
    plt.pie(slices,
        labels=AF1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0.1,0),
        autopct="%1.2f%%")

    plt.show()

  #Africa Region from 1996-2006 
  if x == 83:
    AF1 = ["Africa","Africa total"]
    slices = [884554,2411981]
    colours = ["#14B212","g"]
   
    plt.pie(slices,
        labels=AF1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0.1,0),
        autopct="%1.2f%%")

    plt.show()

  #Africa Region from 2007-2017
  if x == 84:
    AF1 = ["Africa","Africa total"]
    slices = [820659,2411981]
    colours = ["#14B212","g"]
   
    plt.pie(slices,
        labels=AF1,
        startangle=90,
        shadow=False,
        colors=colours,
        explode=(0.1,0),
        autopct="%1.2f%%")

    plt.show()


#########################################################################
#Main Branch: End of Code
#########################################################################