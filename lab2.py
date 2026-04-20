import unittest

def is_possible_to_paint(lengths, painters_limit, max_work_per_painter):
    painters_needed = 1
    current_workload = 0
    
    for length in lengths:
        if current_workload + length > max_work_per_painter:
            painters_needed += 1
            current_workload = length
            
            if painters_needed > painters_limit:
                return False
        else:
            current_workload += length
            
    return True

def get_minimum_painting_time(K, T, L):
    if not L:
        return 0
        
    low_bound = max(L)
    high_bound = sum(L)
    
    optimal_max_length = high_bound
    
    while low_bound <= high_bound:
        mid = (low_bound + high_bound) // 2
        
        if is_possible_to_paint(L, K, mid):
            optimal_max_length = mid
            high_bound = mid - 1
        else:
            low_bound = mid + 1
            
    return optimal_max_length * T


class TestPaintersPartition(unittest.TestCase):
    
    def test_example_case(self):
        K = 10
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]
        expected_time = 100
        self.assertEqual(get_minimum_painting_time(K, T, L), expected_time)

    def test_single_painter(self):
        K = 1
        T = 2
        L = [10, 20, 30]
        expected_time = 120
        self.assertEqual(get_minimum_painting_time(K, T, L), expected_time)

    def test_two_painters(self):
        K = 2
        T = 1
        L = [10, 20, 30, 40]
        expected_time = 60
        self.assertEqual(get_minimum_painting_time(K, T, L), expected_time)
        
    def test_more_painters_than_boards(self):
        K = 5
        T = 10
        L = [5, 15, 10]
        expected_time = 150
        self.assertEqual(get_minimum_painting_time(K, T, L), expected_time)
        
    def test_empty_boards(self):
        self.assertEqual(get_minimum_painting_time(5, 10, []), 0)


if __name__ == '__main__':
    unittest.main()