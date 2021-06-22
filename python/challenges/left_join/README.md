## Code Challenge: Class 30 | Hash Table Implementation

# 33- Left Join
LEFT JOIN returns all rows from the left table, even if there are no matches in the right table. This means that if the ON clause matches 0 (zero) records in the right table; the join will still return a row in the result, but with NULL in each column from the right table

## Challenge Description
Implement a simplified LEFT JOIN for 2 Hashmaps

## Approach & Efficiency
getting keys of the first hashmap then append it with its values as any array to and empty array then for every key search if the other one caontains it if yes append the value for the array

Big O of time --> O(n^2)
Big O of space --> O(n)

## Solution
![image](../../assets/left_join.jpg)
