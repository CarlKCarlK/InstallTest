from fastlmmrslib import qf

probability, fault, trace = qf(20.0, [0.001, 0.001, 1.0, 1.0], acc=1e-7)
if fault != 0:
    raise ArithmeticError(f"Davies calculation reported fault {fault}: {trace}")
print(probability)  # approximately 4.5445e-5
assert abs(probability - 4.5445e-5) < 1e-8, probability

print("OK")
