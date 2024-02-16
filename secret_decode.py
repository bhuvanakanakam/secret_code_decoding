# reading the input.json file, then extract the base and values.
import json

with open('input.json', 'r') as file:
    json_input = json.load(file)
print("Keys in json_input:", json_input.keys())

n = json_input['keys']['n']
k = json_input['keys']['k']
xy_values = []

for i in range(1, n+1):
    share_key = str(i)
    if share_key in json_input:
        base = int(json_input[share_key]['base'])
        value = json_input[share_key]['value']
        decimal_value = int(value, base=base)
        xy_values.append([i, decimal_value])
    else:
        print(f"Share {share_key} is missing.")
print("2D array of x and y values of the shares:")
for pair in xy_values:
    print(pair)

# now, with the converted decimal inputs, have to extrapolate using laplace interpolation and find the polynomial

def denom(arr, n, i):
    ans = 1
    for j in range(n):
        if i != j:
            ans *= (arr[i][0] - arr[j][0])
    return ans

def lagrange_interpolation(arr, n):
    prod = 1
    for i in range(n):
        prod *= arr[i][0]

    soln = 0.0
    for i in range(n):
        soln += ((prod / arr[i][0]) / denom(arr, n, i)) * arr[i][1]

    return soln

constant_term = lagrange_interpolation(xy_values, len(xy_values))
print("Constant term of the polynomial:", constant_term)
