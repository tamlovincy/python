def is_palindrome(n):
    m=1
    if m<=n-1:
    return str(n)[:m]==str(n)[:(m+1)]
    m=m+1
    
print(list(filter(is_palindrome,range(10,1000)))
