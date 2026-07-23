def factorial(n):
    print(f"*At first, n is {n}")
    product = 1
    print(f"at the start product is {product}")
    print(f"* While loop starts")

    while n > 0:
        product *= n
        print(f"* loop iteration starts")
        n -= 1
        print(f"* Decrease n by 1 to {n}")
        print(f"products starts as: {product}")
        print(f"* Multiply product by {n}, making {product}")
        print(f"* loop iteration ends")
        print(f"The final product is: {product}")

    return product

print(f"""
 Running: factorial(5)
Expected: 120
  Actual: {factorial(5)}
""")

