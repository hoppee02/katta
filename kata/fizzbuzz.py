def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    
    return str(number)

def fizzbuzz_extended(number: int) -> str:
    result = ""
    str_num = str(number)

    if number % 3 == 0:
        result += "Fizz"
    if '3' in str_num:
        result += "Fizz"

    if number % 5 == 0:
        result += "Buzz"
    if '5' in str_num:
        result += "Buzz"

    if(result != ""):
        return result 
    else: 
     return str_num


# new requirement: append "hi" if the cross sum is divisible by 2
def fizzbuzz_extended_crosssum(number: int) -> str:
    result = ""
    str_num = str(number)

    if number % 3 == 0:
        result += "Fizz"
    if '3' in str_num:
        result += "Fizz"

    if number % 5 == 0:
        result += "Buzz"
    if '5' in str_num:
        result += "Buzz"

    cross_sum = sum(int(d) for d in str_num)
    if cross_sum % 2 == 0:
        result += "hi"

    if(result != ""):
        return result 
    else: 
     return str_num
 
        


if __name__ == "__main__":
    main()