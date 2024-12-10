# Pick a prime number p and test for a primitive field element in F_p 
# primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, ... 
# ...  67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137

n = 17
p = 131
mul_grp = []

for i in range(0, p):
    z = (n**i) % p
    if i >= 2 and z == 1:
        print(f"Found identity at: {i}")
        break
    mul_grp.append(z)

n_to_p_l_1 = (n**(p - 1)) % p

print(mul_grp)
print(f"For {n} ... : \n")
print(f"Now n^(p-1) ... {n_to_p_l_1} \n")
print(f"Size of the printed set : {len(mul_grp)}")
