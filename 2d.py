import gilbert2d
import sliding_window
import numpy as np
from sys import argv

output = open("boilerplate.txt", "r").read()

points = list(gilbert2d.gilbert2d(int(argv[1]), int(argv[2])))
print(points)
flipped = False
for window in sliding_window.sliding_window(points, 3):
    ab = (window[1][0] - window[0][0], window[1][1] - window[0][1])
    bc = (window[2][0] - window[1][0], window[2][1] - window[1][1])

    angle = np.cross(ab, bc)

    if angle < 0:
        if flipped:
            output += "Turn4,2\n"
            flipped = not flipped
        else:
            output += "Turn4\n"
    elif angle > 0:
        if flipped:
            output += "Turn4\n"
        else:
            output += "Turn4,2\n"
            flipped = not flipped
    else:
        output += "Straight4\nStraight4\n"

output += "EndContinue4"

print(output)
