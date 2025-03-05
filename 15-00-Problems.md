# Pattern Problems
1. Number patterns

```
1 
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
```
    
```python
def pattern(n):
  print('\n'.join([' '.join([str(y) for y in range( 1, x + 1)]) for x in range(1, n + 1)]))

pattern(5)
```
