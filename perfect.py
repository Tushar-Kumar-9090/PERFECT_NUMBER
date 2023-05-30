
## WAP to check given number is prefect number or not??


n=int(input("Enter The Number: "))
summ=0
for i in range(1,n//2+1):
    if n%i==0:
        summ+=i
if summ==n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
