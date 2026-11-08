"""
RECORD CHECK  -  my version
===========================

Name  :Yuvesh Devason
Lane  :  AI 
Date  :06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("records_sample.csv")



# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["value"] / df["limit"])* 100
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" 
    if x >= 100 
        else "WARNING" 
    if x >= 90
        else "OK")


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print("Dataframe:")
print(df)
print("\nNOT OK RECORDS")
print(df[df["status"] != "OK"])
print("\nSTATUS COUNTS")
status_counts = df.groupby("status").size()
print(status_counts)
print("\nSTATUS COUNTS")
status_counts.plot(kind="bar")
plt.title("Status Count")
plt.xlabel("Status")
plt.ylabel("Num of Servers")
plt.savefig("status_chart.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
