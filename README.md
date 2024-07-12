### Secret Message Decoding Using Shamir's Secret Sharing (SSS)
Shamir’s Secret Sharing Scheme (SSS) is a cryptographic algorithm that allows a secret to be divided into ``` n``` shares, where any subset of ```k``` or more shares can be used to reconstruct the secret. This scheme is based on polynomial interpolation and provides a way to securely distribute a secret among multiple parties.

The foundation of this project is based on Adi Shamir's (1984) research paper:- [**How to Share a Secret**](https://dl.acm.org/doi/10.1145/359230.359256)

## Concept
The main idea behind Shamir's Secret Sharing Scheme is to use a polynomial to encode the secret. The secret is represented as the constant term of a polynomial of degree \( k-1 \), and each share corresponds to a point on this polynomial curve. A subset of shares, when combined, allows the reconstruction of the polynomial and the extraction of the secret.

The polynomial is expressed as follows:  ```[f(x) = a_0 + a_1x + a_2x^2 + ..... + a_{k-1}x^{k-1}]```

- ```a_0```: This is the secret we want to share.
- ```a_1, a_2, .... , a_{k-1}```: These are random coefficients used to construct the polynomial. 

## Encoding the Secret

1. **Construct the Polynomial:** The secret ```a_0``` is embedded as the constant term of a polynomial of degree ```k-1```. The polynomial ```f(x)``` is created with randomly chosen coefficients for ```( a_1, a_2, ...., a_{k-1})```.
2. **Generate Shares:** Evaluate the polynomial at different ```x``` values to create shares. Each share is a pair ```(x_i, f(x_i))```, where ``` x_i``` is a unique index for the share, and ```f(x_i)``` is the polynomial's value at ```x_i```.
   - For example, if ```( x_1, x_2, x_3, ..., x_n )``` are the chosen points, the shares would be ```((x_i, f(x_i))```.
3. **Distribute Shares:** The shares are distributed among the parties. Any subset of ```k``` or more shares can be used to reconstruct the polynomial and recover the secret.


Suppose we want to share the secret a_0 = 123 using a polynomial of degree 2 (k = 3). We create a polynomial like this: f(x) = 123 + a_1x + a_2x^2
Here, a_1 and a_2 are random coefficients. We evaluate this polynomial at different x values to generate shares:
- For \( x_1 = 1 \), the share is \( (1, f(1)) \).
- For \( x_2 = 2 \), the share is \( (2, f(2)) \).
- For \( x_3 = 3 \), the share is \( (3, f(3)) \).
With at least 3 shares, we can reconstruct the polynomial and find a_0, which is the original secret.

## Why Polynomial Representation?

The polynomial representation allows us to encode the secret in such a way that the secret can only be reconstructed when a minimum number of shares are combined. The random coefficients ensure that the polynomial's behavior is complex enough that reconstructing the polynomial requires solving a system of equations based on the shares.

## File
- The ``` secrete_decode.py ``` contains the implementation of the problem.
- Read ```input.json```: Extracts the values for n (total number of shares) and k (minimum number of shares required to reconstruct the secret).
- ```Convert Values```: Converts the values from their respective bases to decimal (base-10).
- ```Lagrange Interpolation```: Uses the Lagrange Interpolation Technique to reconstruct the polynomial and find the constant term, which is the secret. Here
- ```Output```: Prints the constant term of the polynomial, which is the secret code.
