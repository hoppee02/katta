from fizzbuzz import fizzbuzz, fizzbuzz_extended, fizzbuzz_extended_crosssum

def test_fizzbuzz():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizzbuzz_extended():
    assert fizzbuzz_extended(53) == "FizzBuzz"
    assert fizzbuzz_extended(35) == "FizzBuzzBuzz"
    assert fizzbuzz_extended(51) == "FizzBuzz"
    assert fizzbuzz_extended(33) == "FizzFizz"
    
def test_fizzbuzz_extended_crosssum():
    assert fizzbuzz_extended_crosssum(1) == "1" 
    assert fizzbuzz_extended_crosssum(11) == "hi"    
    assert fizzbuzz_extended_crosssum(20) == "Buzzhi"
    assert fizzbuzz_extended_crosssum(13) == "Fizzhi"
    assert fizzbuzz_extended_crosssum(22) == "hi"


