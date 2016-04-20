import unittest
import best_path

class TestBestPath(unittest.TestCase):

    def test_full_search(self):
        test_cases = [
        ([
            [1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]
        ], 'rrdd'),
        ([
            [0x46B, 0xE59, 0xEA, 0xC1F, 0x45E, 0x63],
            [0x899, 0xFFF, 0x926, 0x7AD, 0xC4E, 0xFFF],
            [0xE2E, 0x323, 0x6D2, 0x976, 0x83F, 0xC96],
            [0x9E9, 0xA8B, 0x9C1, 0x461, 0xF74, 0xD05],
            [0xEDD, 0xE94, 0x5F4, 0xD1D, 0xD03, 0xDE3],
            [0x89, 0x925, 0xCF9, 0xCA0, 0xF18, 0x4D2]
        ], 'ddrrrdddrr')
        ]
        for case, result in test_cases:
            self.assertEquals(best_path.grid_search(case), result)

if __name__ == '__main__':
    unittest.main()
