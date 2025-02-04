import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (you can replace this with actual data reading from a file)
data = {
    'Constituency': ['Mumbai North', 'Pune', 'Nashik', 'Nagpur', 'Thane', 'Aurangabad', 
                     'Solapur', 'Kolhapur', 'Amravati', 'Jalgaon'],
    'Candidate Name': ['Pritam Munde', 'Girish Bapat', 'Dr. Hemant Deshmukh', 'Nitin Gadkari', 
                        'Rajan Vichare', 'Imtiaz Jaleel', 'Shivaji Kharat', 'Dhananjay Munde', 
                        'Anil Deshmukh', 'Suresh Jain'],
    'Party': ['BJP', 'BJP', 'Shiv Sena', 'BJP', 'Shiv Sena', 'AIMIM', 'NCP', 'NCP', 'Congress', 'BJP'],
    'Votes': [512000, 800000, 750000, 600000, 650000, 400000, 470000, 590000, 460000, 520000],
    'Year': [2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Basic analysis: Total votes per party
party_votes = df.groupby('Party')['Votes'].sum()

# Plotting the results
party_votes.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Total Votes per Party in Maharashtra (2024)')
plt.xlabel('Party')
plt.ylabel('Total Votes')
plt.xticks(rotation=45)
plt.show()

# Analysis: Constituency-wise vote percentage for each party
df['Vote Percentage'] = df.groupby('Constituency')['Votes'].transform(lambda x: x / x.sum() * 100)

# Displaying vote percentage by constituency
print(df[['Constituency', 'Candidate Name', 'Party', 'Vote Percentage']])

# Additional Analysis: Finding the highest votes
max_votes_row = df.loc[df['Votes'].idxmax()]
print(f"Highest votes received by: {max_votes_row['Candidate Name']} from {max_votes_row['Party']} in {max_votes_row['Constituency']}")
