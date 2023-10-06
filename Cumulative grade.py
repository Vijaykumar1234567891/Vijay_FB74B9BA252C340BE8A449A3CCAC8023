# Importing Pandas package
import pandas as pd

# Creating a Dictionary
d = {
    'Physics': [78, 42, 80, 30],
    'Chemistry': [51, 45, 90, 33],
    'Maths': [23, 45, 28, 33]
}

# Creating a dataframe
df = pd.DataFrame(d)

# Display Original dataframe
print("Created Dataframe:\n",df,"\n")

# Calculating cumulative sum
df['cum_sum'] = df['Chemistry'].cumsum()

# Calculating cumulative percentage
df['cum_perc'] =  100*df['cum_sum']/df['Chemistry'].sum()

# Display modified DataFrame
print("Modified DataFrame:\n",df)
