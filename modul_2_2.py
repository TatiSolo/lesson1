first=input()
second=input()
thrid=input()
if first==second==thrid:
    print(3)
if first==second or first==thrid or second==thrid:
    print(2)
if first!=second!=thrid:
    print(0)