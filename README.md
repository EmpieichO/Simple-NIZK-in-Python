# Simple NIZK in Python
Implementing a simple non-interactive zero-knowledge proof in python

## **Description**
Suppose Alice has to prove knowledge of $k$, which is the log of $x = b^k$, where $x$ and $b$ are publicly known numbers. 

Assuming $k, x$ are integer field elements of a prime field $\mathbb{F}_p$ for an agreed upon prime number $p$. 

And $b$ is a non-zero field element such that $b^{p-1} = 1$, while $b^i \not= 1$ for all other $0 < i \not= p-1$.   


**Remark**: The values of $p$ and $b$ are hardcoded. To avoid memory overflow it is preferable to restrict $p$ to < 120, and $b$ should be chosen to be as small as possible. For example: 
- For $p = 131$, although $b = 17$ and $b = 2$ are valid primitive elements, it is best to choose $b = 2$.   


## **Proving** 
Alice can produce a proof $(s, r)$ as follows, 

- uses a PRF to sample a random integer $v$, 
- then calculates $b^v =: s$  
- uses the system’s CRH to compute $c := CRH(b, x, s)$  
- finally computes $r := v - (k*c)$ 

and publishes $(s, r)$ as the proof that she knows $k$.



## **Verifying** 
Any party can verify Alice's proof as follows, 

- uses the CRH to compute $CRH(b, x, s) =: c$
- checks if  $b^r * x^c = s$ in order to verify that Alice knows $k$.


## **Why does this work?** 

- 1st, note $b^r * x^c = b^{v - (k*c)} * (b^k)^c = b^v * b^{-(k*c)} * b^{k * c} = b^v = s$. 
- 2nd, the outcome $c$ of the hash function CRH was unpredictable. 
- 3rd, it is infeasible to solve the Discrete Log Problem for a large integer $b$. Therefore Alice must have known $k$, because there's no other way she could have correctly computed $r$. 

