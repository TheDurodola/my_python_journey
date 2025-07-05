number = int(input("Enter the 5-digits number: "))


digit = number//10000
digits = number%10000

digit1 = digits//1000
digit1s = digits%1000

digit2 = digit1s //100
digit2s = number%100

digit3 = digit2s //10
digit3s = number%10

digit4 = digit3s //1
digit4s = number%1



print(digit,digit1,digit2,digit3,digit4)