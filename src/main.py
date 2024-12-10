import random
from hashlib import sha256
import numpy as np

sub_gen_k = [1, 5, 2, 10, 4, 20, 8, 17, 16, 11, 9, 22, 18, 21, 13, 19, 3, 15, 6, 7, 12, 14] # 7 is primitive for p = 47

b = np.array([2]) # known by prover and verifier

k = np.array([random.randint(2, 13)])
print(f"The selected secret key: {k}")

p = np.array([131])

x = (b**k) % p
print(f"The public key is: {x}")

# def power(x, b, p):
#     if b == 1:
#         return x
#     else:
#         return pow(x, b) % p

def proving_k():
    select_v = random.choice(sub_gen_k)
    v = np.array([select_v])

    unred_s = b**v
    print(f"The unreduced value b^v : {unred_s}")

    s = np.array(unred_s % p) # b^v

    mssg = f'{b},{x},{s}'
    bxs_digest = sha256(mssg.encode('utf-8')).hexdigest()
    # Convert digest to integer value
    int_digest = np.array(int(bxs_digest, 16))

    c = np.array(int_digest % p) # this is c = CRH(b,x,s)

    # print(f"The mod p value of int_digest (This is c BTW!) : {c}")
    # Computing r := v - (k*c) modulo p
    # check if v <= k*c or v > k*c
    skc = k*c
    print(f"The skc = k*c : {skc}")
    red_skc = skc % (p - 1)

    if v < red_skc:
        r = np.array((p-1) + (v - red_skc))
    else:
        r = np.array(v - red_skc)

    proof = np.array([s,r])

    return proof


final_proof = proving_k()
print(f"Here's the proof : {final_proof}")

ver_s = final_proof[0]
ver_r = final_proof[1]
# ver_c = final_proof[2]
print(f"... ver_s : {ver_s}")
print(f"... ver_r : {ver_r}\n")

# Verifying final_proof
def verify_proof():

    # Compute the sha256 digest and convert to field element in F_p
    input_ = f'{b},{x},{ver_s}'
    ver_bxs_digest = sha256(input_.encode('utf-8')).hexdigest()
    int_bxs_digest = np.array(int(ver_bxs_digest, 16))
    ver_c = np.array(int_bxs_digest % p) # this should be same as c = CRH(b,x,s)

    b_to_r_unred = b**ver_r
    b_to_ver_r = b_to_r_unred % p
    print(f".. b^ver_r mod p : {b_to_ver_r}")
    
    x_to_c_unred = x**ver_c
    x_to_ver_c = x_to_c_unred % p
    print(f".. x^ver_c mod p : {x_to_ver_c}")

    # x_power_c = power(x, ver_c, p)

    ver_prod = (b_to_ver_r*x_to_ver_c) % p
    print(f".. final ver product : {ver_prod}\n")

    if ver_prod != ver_s:
        print("Verification failed!")
    else:
        print("** Successfully verified ** :-) \n")
    
    return 0 # b_to_ver_r

verdict = verify_proof()
