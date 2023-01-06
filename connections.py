"""
This file conatins the heuristic values and connections between cities
"""


# Dictionary to hold heristic values
heuristic_map = {
        "St. Joseph": {"St. Joseph": 0, "Kansas City": 56, "Joplin": 205, "Springfield": 221, "Rolla": 277, "Jefferson City": 215, "Columbia": 181, "Moberly": 157, "Hannibal": 194, "Troy": 254, "St. Charles": 286, "St. Louis": 303, "Lebanon": 237},
         "Kansas City": {"St. Joseph": 56, "Kansas City": 0, "Joplin": 156, "Springfield": 165, "Rolla": 219, "Jefferson City": 157, "Columbia": 124, "Moberly": 159, "Hannibal": 210, "Troy": 211, "St. Charles": 228, "St. Louis": 248, "Lebanon": 176},
         "Joplin": {"St. Joseph": 205, "Kansas City": 56, "Joplin": 0, "Springfield": 74, "Rolla": 179, "Jefferson City": 205, "Columbia": 235, "Moberly": 270, "Hannibal": 310, "Troy": 282, "St. Charles": 288, "St. Louis": 284, "Lebanon": 123},
         "Springfield": {"St. Joseph": 221, "Kansas City": 165, "Joplin": 74, "Springfield": 0, "Rolla": 112, "Jefferson City": 138, "Columbia": 169, "Moberly": 203, "Hannibal": 242, "Troy": 215, "St. Charles": 221, "St. Louis": 217, "Lebanon": 54},
         "Rolla": {"St. Joseph": 277, "Kansas City": 219, "Joplin": 179, "Springfield": 112, "Rolla": 0, "Jefferson City": 63, "Columbia": 93, "Moberly": 128, "Hannibal": 168, "Troy": 105, "St. Charles": 110, "St. Louis": 106, "Lebanon": 58},
         "Jefferson City": {"St. Joseph": 215, "Kansas City": 157, "Joplin": 205, "Springfield": 138, "Rolla": 63, "Jefferson City": 0, "Columbia": 32, "Moberly": 66, "Hannibal": 106, "Troy": 96, "St. Charles": 113, "St. Louis": 133, "Lebanon": 82},
         "Columbia": {"St. Joseph": 181, "Kansas City": 124, "Joplin": 235, "Springfield": 169, "Rolla": 93, "Jefferson City": 66, "Columbia": 0, "Moberly": 36, "Hannibal": 98, "Troy": 87, "St. Charles": 105, "St. Louis": 125, "Lebanon": 113},
         "Moberly": {"St. Joseph": 157, "Kansas City": 159, "Joplin": 270, "Springfield": 203, "Rolla": 128, "Jefferson City": 106, "Columbia": 36, "Moberly": 0, "Hannibal": 70, "Troy": 120, "St. Charles": 137, "St. Louis": 157, "Lebanon": 148},
         "Hannibal": {"St. Joseph": 194, "Kansas City": 210, "Joplin": 310, "Springfield": 242, "Rolla": 168, "Jefferson City": 96, "Columbia": 98, "Moberly": 70, "Hannibal": 0, "Troy": 63, "St. Charles": 97, "St. Louis": 117, "Lebanon": 188},
         "Troy": {"St. Joseph": 254, "Kansas City": 211, "Joplin": 282, "Springfield": 215, "Rolla": 105, "Jefferson City": 70, "Columbia": 87, "Moberly": 120, "Hannibal": 63, "Troy": 0, "St. Charles": 35, "St. Louis": 55, "Lebanon": 161},
         "St. Charles": {"St. Joseph": 286, "Kansas City": 228, "Joplin": 288, "Springfield": 221, "Rolla": 110, "Jefferson City": 113, "Columbia": 105, "Moberly": 137, "Hannibal": 97, "Troy": 35, "St. Charles": 0, "St. Louis": 23, "Lebanon": 167},
         "St. Louis": {"St. Joseph": 303, "Kansas City": 248, "Joplin": 284, "Springfield": 217, "Rolla": 106, "Jefferson City": 133, "Columbia": 125, "Moberly": 157, "Hannibal": 117, "Troy": 55, "St. Charles": 23, "St. Louis": 0, "Lebanon": 163},
         "Lebanon": {"St. Joseph": 237, "Kansas City": 176, "Joplin": 123, "Springfield": 54, "Rolla": 58, "Jefferson City": 82, "Columbia": 113, "Moberly": 148, "Hannibal": 188, "Troy": 161, "St. Charles": 167, "St. Louis": 163, "Lebanon": 0},
        }

# Dictionary to hold distances between connected cities
connections = {
        "St. Joseph": {"Kansas City": 56},
         "Kansas City": {"St. Joseph": 56, "Joplin": 156, "Columbia": 124},
         "Joplin": {"Kansas City": 56, "Springfield": 74},
         "Springfield": {"Joplin": 74, "Lebanon": 54},
         "Rolla": {"Jefferson City": 63, "St. Louis": 106, "Lebanon": 58},
         "Jefferson City": {"Rolla": 63, "Columbia": 32},
         "Columbia": {"Kansas City": 124, "Jefferson City": 66, "Moberly": 36, "St. Charles": 105},
         "Moberly": {"Columbia": 36, "Hannibal": 70},
         "Hannibal": {"Moberly": 70, "Troy": 63},
         "Troy": {"Hannibal": 63, "St. Charles": 35},
         "St. Charles": {"Columbia": 105, "Troy": 35, "St. Louis": 23},
         "St. Louis": {"Rolla": 106, "St. Charles": 23},
         "Lebanon": {"Springfield": 54, "Rolla": 58},
        }