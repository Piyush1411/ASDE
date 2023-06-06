[ASDE Assignment.xlsx](https://github.com/Piyush1411/ASDE_Assignment/files/11660887/ASDE.Assignment.xlsx)
# ASDE_Assignment
## Task-1 SQL
Fetch top 3 departments along with their name and average monthly salary. Below is the format of the report.

| DEPT_NAME | AVG_MONTHLY_SALARY (USD) |

## Task-1 Solution(Using PostGreSQL Syntax)

```sql 
SELECT d.NAME AS Dept_Name, CONCAT('$', CAST(AVG(s.AMT) AS DECIMAL(10, 2))) AS "Average_Monthly_Salary(USD)"
FROM DEPARTMENTS d, Salaries s, employees e
WHERE d.ID = e.DEPT_ID AND e.ID = s.EMP_ID
GROUP BY d.NAME
ORDER BY "Average_Monthly_Salary(USD)" DESC
LIMIT 3;
```

## Task 1 Tools used- 
PostgreSQL

## Task-1 Explanation

The SQL query you provided is used to fetch the top 3 departments along with their average monthly salary. It joins the Departments, Salaries, and employees tables based on the specified conditions (d.ID = e.DEPT_ID and e.ID = s.EMP_ID) and calculates the average salary for each department. The result is then sorted in descending order(DESC) of the average monthly salary and limited to the top 3 records using limit clause.

## Task-2 Scripting

With the same attachment, use each worksheet as a CSV file and write a Python script that generates the same report. Data is to be read from the CSV files not from a database.

## Task-2 Solution

```python
#### importing pandas package
import pandas as pd

#### Read CSV files into pandas DataFrames
employees = pd.read_csv("filePath/EMPLOYEES.csv")
departments = pd.read_csv("filePath/DEPARTMENTS.csv")
salaries = pd.read_csv("filePath/SALARIES.csv")

#### Merge the DataFrames to get the necessary data
merged_data = employees.merge(departments, left_on='DEPT_ID', right_on='DEPT_ID')
merged_data = merged_data.merge(salaries, left_on='EMP_ID', right_on='EMP_ID')

#### Calculate average monthly salary for each department
average_salaries = merged_data.groupby(['DEPT_ID', 'DEPT_NAME'])['AMT (USD)'].mean().reset_index()

#### Sort departments based on average salary in descending order
sorted_departments = average_salaries.sort_values('AMT (USD)', ascending=False)

#### Fetch top 3 departments
top_departments = sorted_departments.head(3)

#### Generate report
report = "Top 3 Departments by Average Monthly Salary:\n"
for index, row in top_departments.iterrows():
    report += "Department Name: {}\n".format(row['DEPT_NAME'])
    report += "Average Monthly Salary: ${}\n".format(row['AMT (USD)'])
    report += "-------------------------\n"

#### Print the report
print(report)
##### end of pyhton file;
```

## Task-2 tools used-

Jupyter note book where a Jupyter notebook consists of a sequence of cells. The flow of a notebook is sequential. You enter code into an input cell, and when you run the cell, the notebook runs the code and prints the output of the computation to an output cell.

## Task-2 Explanation

The above code essentially reads the employee, department, and salary data from CSV files, merges them based on common columns, calculates the average salary for each department, sorts the departments in descending order of average salary, selects the top 3 departments, and generates a report displaying the department name and average monthly salary.

## Task-3 Debugging

Given below is a Bash / Python script that performs following computation on an integer input (n):
1.	If n is less than 10: Calculate its Square
  a.	Example: 4 => 16
2.	If n is between 10 and 20: Calculate the factorial of (n-10)
  a.	Example: 15 => 120
3.	If n is greater than 20: Calculate the sum of all integers between 1 and (n-20)
  a.	Example: 25 => 15
<
The task is to identify the bugs in the script, fix them and share the new script. Only one of the two scripts required Python. Hint: You can correct the script by only changing 3-4 characters.

### Script (Python)
```python
def compute(n):
    if n < 10:                         ##### Square Calculation
        out = n ** 2
    elif n < 20:                       ##### Factorial Calculation
        out = 1
        for i in range(1, n-10):       ##### last element should be n-10 not n-11
            out *= i
    Else:                              ##### Sum Calculation
        lim = n - 20
        out = lim * lim                ##### instead these 3 lines 
        out = out - lim                ##### we can use 
        out = out / 2                  ##### sum function
    print(out)

n = int(input("Enter an integer: "))
compute(n)
```

### Correct Script (Python)
```python
def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n-10 +1):    ##### Fixed the range to include n - 10
            out *= i
    else:
        lim = n - 20
        out = sum(range(1, lim + 1))    ##### Changed the calculation to sum of integers
    print(out)                          

n = int(input("Enter an integer: "))
compute(n)
```

## Task-3 tools used-

VS Code Editor the code is debugeed using python kernel provided by microsoft. By selecting a line and pressing F9 keyword on the selected line of the code, the breakpoint is defined in the code. This breakpoint of the code is debugged by pressing the play button.

## Task-3 Explanation

1. In the factorial calculation, the range should include n - 10 to ensure the correct factorial calculation.
2. For the case when 'n' is greater than 20, the sum of integers between 1 and '(n-20)' is calculated using the 'sum()' function on the range.
3. The 'lim * lim' operation in the else block has been removed as it doesn't align with the desired computation.

