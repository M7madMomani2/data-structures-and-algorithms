# Multi Bracket Validation
we need to create a method to check string and assure that Multi Bracket write in wright way

## Approach & Efficiency
**Efficiency**

Big O :
> - O(n) Time


**Approach**

create multi  method that take string

create empty array and an dictionary with this details keys value=> { '(':')', '[':']', '{':'}' }

using a for loop if the number equal one of keys_value then append it to the empty array or pop the array and return a false
if length of the array not equal to zero return a false else: return True
## Solution
[Singly Linked List](https://miro.com/app/board/o9J_lG44R2c=/)
