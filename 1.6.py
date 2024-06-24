def reverseNum(number):
    reversed_str = str(number)[::-1]
    reversed_num = int(reversed_str)
    return reversed_num

def isPalindrome(number):
    return str(number) == str(number)[::-1]

def revAndAddTillPalindrome(original):
    current = original
    
    while True:
        reversed_num = reverseNum(current)
        new_num = current + reversed_num
        
        print(f"{current} + {reversed_num} = {new_num}")
        
        if isPalindrome(new_num):
            print(f"{new_num} is a palindrome.")
            break
        
        current = new_num


original = int(input("Enter a number: "))
print(f"Starting with number: {original}")
revAndAddTillPalindrome(original)
