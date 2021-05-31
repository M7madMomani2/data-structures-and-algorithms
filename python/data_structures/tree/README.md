# Max of  Tree
> - we need to implement max method that return max element of tree


## Approach & Efficiency
**Efficiency**

Big O :
> - O(n) Time and O(1) space performance for includes method.


**Approach**
> - in constructor create variable maxVal
> - create method find_maximum_value()that take tree object
> - inside  find_maximum_value create recursive function name _walk and check all elements in tree and each time check if maxVal > left & right and reassign maxVal based on result
> - when _walk finish return maxVal


## Solution
[Max of  Tree](https://miro.com/app/board/o9J_lG44R2c=/)

-----------------------------------------
# Breadth First
> - we need to implement method that retun tree as Breadth First

## Approach & Efficiency
**Efficiency**

Big O :
> - O(n) Time and O(1) space performance for includes method.


**Approach**
- create method breadth_first()that take 2 argument (self and tree object )

- create tow list temp and result

- each level append nods to result until we pass node that don't have children's


## Solution
[Breadth First](https://miro.com/app/board/o9J_lG44R2c=/)

