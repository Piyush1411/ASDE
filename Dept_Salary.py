import pandas as pd

# Read CSV files into pandas DataFrames
employees = pd.read_csv("C:/Users/pkgpr/Downloads/EMPLOYEES.csv")
departments = pd.read_csv("C:/Users/pkgpr/Downloads/DEPARTMENTS.csv")
salaries = pd.read_csv("C:/Users/pkgpr/Downloads/SALARIES.csv")

# Merge the DataFrames to get the necessary data
merged_data = employees.merge(departments, left_on='DEPT_ID', right_on='DEPT_ID')
merged_data = merged_data.merge(salaries, left_on='EMP_ID', right_on='EMP_ID')

# Calculate average monthly salary for each department
average_salaries = merged_data.groupby(['DEPT_ID', 'DEPT_NAME'])['AMT (USD)'].mean().reset_index()

# Sort departments based on average salary in descending order
sorted_departments = average_salaries.sort_values('AMT (USD)', ascending=False)

# Fetch top 3 departments
top_departments = sorted_departments.head(3)

# Generate report
report = "Top 3 Departments by Average Monthly Salary:\n"
for index, row in top_departments.iterrows():
    report += "Department Name: {}\n".format(row['DEPT_NAME'])
    report += "Average Monthly Salary: ${}\n".format(row['AMT (USD)'])
    report += "-------------------------\n"

# Print the report
print(report)