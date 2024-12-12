f1, f2 = map(float, input().split())

fluctuation = ((((1.0 + f1/100.00) * (1.0 + f2/100.00)) - 1.0) * 100.0)

print(f'{fluctuation:.6f}')

""" To go from the formula (final GDP - initial GDP) / initial GDP * 100 to (1 + F1/100) x (1 + F2/100) - 1, we can use the following steps:

We know that the growth rate in the first year, F1, is the percentage change in GDP from the initial year to the end of the first year. So we can express the GDP at the end of the first year, G1, in terms of the initial GDP, G0, as:
G1 = G0 * (1 + F1/100)

Similarly, we can express the GDP at the end of the second year, G2, in terms of the GDP at the end of the first year, G1, as:
G2 = G1 * (1 + F2/100)

Substituting the expression for G1 from step 1 into the expression for G2 from step 2, we get:

G2 = G0 * (1 + F1/100) * (1 + F2/100)

Now, we can express the growth rate for the two-year period as the percentage change from the initial GDP, G0, to the final GDP, G2, using the formula:
(final GDP - initial GDP) / initial GDP * 100

Substituting G2 for the final GDP and G0 for the initial GDP, we get:

(G2 - G0) / G0 * 100

Substituting the expression for G2 from step 2 and simplifying, we get:
[(1 + F1/100) * (1 + F2/100) * G0 - G0] / G0 * 100

= [(1 + F1/100) * (1 + F2/100) - 1] * 100

So the growth rate for the two-year period can be expressed as (1 + F1/100) x (1 + F2/100) - 1, which is the formula we derived earlier. """