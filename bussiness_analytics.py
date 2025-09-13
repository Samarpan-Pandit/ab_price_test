import pandas as pd
from scipy import stats

# Load data
df = pd.read_csv("D:/projects/clg_project/data.csv")

# Count per variant
counts = df["Variant"].value_counts()
print("Conversion Counts:\n", counts)

# Conversion Rate (since only clicks are logged, treat count as conversion)
total_A = counts.get("A", 0)
total_B = counts.get("B", 0)
total = total_A + total_B

cr_A = total_A / total if total > 0 else 0
cr_B = total_B / total if total > 0 else 0

print(f"\nConversion Rate A: {cr_A:.2%}")
print(f"Conversion Rate B: {cr_B:.2%}")

# Lift
if cr_B > 0:
    lift = (cr_A - cr_B) / cr_B * 100
    print(f"\nLift of A over B: {lift:.2f}%")

# Chi-square test (significance test)
obs = [[total_A, total_B]]
chi2, p, _, _ = stats.chi2_contingency([ [total_A, total_B], [total_B, total_A] ])
print(f"\nChi-square test: chi2={chi2:.4f}, p-value={p:.4f}")
