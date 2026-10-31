print('OPERATIONS ON NUMBERS')
print('1 Sum of digit')
print('2 Reverse of number')
print('3 Amstrong number')
print('4 Palindrome')
x=int(input('Enter a choice (1-4):'))
match x:
  case 1:
    print("Sum of digit")
    n=int(input('Enter a number:'))
    sum=0
    while n>0:
      d=n%10
      sum=sum+d
      n=n//10
      print(sum)
  case 2:
    print("Reverse of number")
    n=int(input('Enter a number:'))
    rev=0
    while n>0:
      d=n%10
      rev=rev*10+d
      n=n//10
      print(rev)
  case 3:
    print("Armstrong number:")
    n=int(input('Enter a number:'))
    sum=0
    temp=n
    while temp>0:
      d=temp%10
      sum=sum+d**3
      temp=temp//10
    print(sum)
  case 4:
    print("Palindrome:")
    n=int(input('Enter a number:'))
    temp=n
    rev=0
    while temp>0:
      d=temp%10
      rev=rev*10+d
      temp=temp//10
      print(rev)
      if n==rev:
        print('palindrome')
      else:
        print('not palindrome')