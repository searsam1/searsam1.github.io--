
class Test:
    tests_passed = 0 

    def assert_equals(a,b):
        print(a,"->",b)
        Test.tests_passed += 1
        assert a == b




def min_swaps(s1, s2):
    s1, s2 = int(s1,2), int(s2,2)
    return (s1 ^ s2).bit_count() // 2

print(
    min_swaps("10011001", "01100110")
)        


Test.assert_equals(min_swaps("1001", "1001"), 0)
Test.assert_equals(min_swaps("1100", "1001"), 1)
Test.assert_equals(min_swaps("110011", "010111"), 1)
Test.assert_equals(min_swaps("1100", "0011"), 2)
Test.assert_equals(min_swaps("110011", "001111"), 2)
Test.assert_equals(min_swaps("10011001", "01100101"), 3)
Test.assert_equals(min_swaps("11111000001100", "10110010100110"), 3)
Test.assert_equals(min_swaps("01100100100111", "10110010100110"), 3)
Test.assert_equals(min_swaps("11110011001", "01100110111"), 3)
Test.assert_equals(min_swaps("100110001", "010100110"), 3)
Test.assert_equals(min_swaps("100101011", "011001101"), 3)
Test.assert_equals(min_swaps("10011001", "01100110"), 4)
print(f"Number of Tests Passed: {Test.tests_passed}")