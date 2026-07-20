def factorial(n):
    ret=1
    for i in range(n):
        ret*=i+1
    return ret

if __name__=="__main__":
    print(factorial(5))