# P01 Behavioral Specification

| sel | a | b | Required y |
|---:|---:|---:|---:|
| 0 | 0 | X | 0 |
| 0 | 1 | X | 1 |
| 1 | X | 0 | 0 |
| 1 | X | 1 | 1 |

Functional definition:

```
y = a, if sel = 0
y = b, if sel = 1
```
