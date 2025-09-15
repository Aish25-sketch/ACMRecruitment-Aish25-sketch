A = 5
B = 3
SUM = 0

print("Initial: A =", A, ", B =", B, ", SUM =", SUM)

for i in range(1, B + 1):
    print(f"\nStep {i}:")
    print("Before: SUM =", SUM)
    SUM = SUM + A
    print(f"Operation: SUM = SUM + A → {SUM}")

print("\nFinal Output:", SUM)


Trace Table:
| Iteration (i) | Value of SUM before | Operation Performed | Value of SUM after |
| ------------- | ------------------- | ------------------- | ------------------ |
| 1             | 0                   | SUM = 0 + 5         | 5                  |
| 2             | 5                   | SUM = 5 + 5         | 10                 |
| 3             | 10                  | SUM = 10 + 5        | 15                 |


Final Output:
15
