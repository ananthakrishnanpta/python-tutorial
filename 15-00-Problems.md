# Pattern Problems
1. ```
        1 
        1 2    
        1 2 3
        1 2 3 4 
        1 2 3 4 5
    ```
    
```python
# solution 1
def pattern(n):
  print('\n'.join([' '.join([str(y) for y in range( 1, x + 1)]) for x in range(1, n + 1)]))

# solution 2
def pattern(n):
  for i in range(1, n+1):
    for j in range(1, i + 1):
      print(j, end = ' ')
    print()

pattern(5)
```


2. ```
          #
         #-#
        #-#-#
       #-#-#-#
        #-#-# 
         #-# 
          #
   ```

```python
def pattern(n):
  symbols = -1 # no of times to print '#-'
  spaces = n # no of spaces to add to the left
  for row in range(1, (n)*2):
    if row <= (n // 2) + 2: # Until half the pattern is reached, 
      symbols  += 1         # we have to increase no of times '#-' is printed.
      spaces -= 1           # Reducing spaces by 1 for each row.
    else:                   # Once half pattern in complete, now no of spaces is 0 and '#-' is printed 'n-1' times.
      symbols -= 1          # Decrement no of '#-'.
      spaces += 1           # Increment 1 space in each iteration
    print(" " * spaces + "#-" * symbols + "#") # prints necessary spaces, then '#-' repeated ending with '#' symbol.

pattern(4)
```
