# Table: Users

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# Return the result table ordered by user_id.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+
# Output: 
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+

# Write your MySQL query statement below
SELECT user_id, CONCAT(UCASE(SUBSTRING(name, 1, 1)), LCASE(SUBSTRING(name, 2))) AS name
FROM Users
 ORDER BY user_id;

SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;

Python code: 
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
     users['name'] = users['name'].str.capitalize()
     return users.sort_values(by='user_id')
    
