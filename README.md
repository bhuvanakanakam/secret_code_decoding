# Secret Message Decoding Using Shamir Algorithm

Here, Using shamir algorithm for block chain, we are inputing a json file with secret messages of numbers with different base and values ( 10 base 10, 3 base 6 ), along with n and k values where n is the total number of points and k is going to give the polynomial we have to get, k-1 degree.

Then we have to build a code where it the secret is decoded and then, get the polynomial constant. Used the Lagrange Interpolation Technique from Shamir Research Paper to design the polynomial, We should understand there we should use min k points of the n points given, otherwise you can't get the constants.

Example : points 4 and k 3, we will have a second degree polynomial. Now, we have to use min 3 points to get ax^2+bx+c, the constants in this equation. finally the output is the c value which consists of the secret code to be sent
