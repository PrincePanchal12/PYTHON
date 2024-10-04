class Solution:
    def isPalindrome(self, x: int(input("")) -> bool:
        rev_num = 0
        original_x=x      #store the original valuse of x
        while x>0:
            rev_num = rev_num * 10 + (x % 10)
            x //= 10
        return original_x == rev_num # will retuen True or false 

#_________________________________________________________________________________________________________________________________________________________________________________________#
num=121
def reverse(num):
    rev_num=0
    while num>0:
        lst_digit=num%10
        rev_num=rev_num*10+lst_digit
        num//=10
    return rev_num
rev=reverse(num)
if rev==num:
    print(f"The number {num} is a pailndrome number")
else:
    print("This is not a Pailndrome number ")
