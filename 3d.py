import gilbert3d
import sliding_window
import math
import numpy as np
from sys import argv

output = open("boilerplate.txt", "r").read()

points = list(gilbert3d.gilbert3d(int(argv[1]), int(argv[2]), int(argv[3])))
print(points)

# How a tile is oriented depends on the orientation of the previous tile which is stored in the orientation matrix
orientation = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
for window in sliding_window.sliding_window(points[1:], 2):
    window = np.array(window)

    absolute_block_direction = window[1] - window[0]
    relative_block_direction = np.matmul(
        np.linalg.inv(orientation), absolute_block_direction
    )

    is_turn = False
    if (relative_block_direction == [1, 0, 0]).all():
        # Straight
        output += "Straight4\n"
        output += "Straight4\n"
    elif (relative_block_direction == [0, -1, 0]).all():
        # Left
        output += "Turn4\n"
        is_turn = True
    elif (relative_block_direction == [0, 0, -1]).all():
        # Down
        output += "Turn4,1\n"
        is_turn = True
    elif (relative_block_direction == [0, 1, 0]).all():
        # Right
        output += "Turn4,2\n"
        is_turn = True
    elif (relative_block_direction == [0, 0, 1]).all():
        # Up
        output += "Turn4,3\n"
        is_turn = True
    else:
        raise Exception("UNKNOWN DIRECTION")  # Should be unreachable

    if is_turn:
        # Change orientation
        # a and b are known absolute vectors, x and y are known vectors relative to the orientation
        # c and z are helper vectors, which are needed to complete the coordinate systems abc, xyz
        # Goal is to find the orientation
        a = np.matmul(orientation, [1, 0, 0])  # Direction of current orientation
        b = absolute_block_direction  # Absolute direction of where the turn is going
        if np.linalg.norm(np.cross(a, b)) == 0:
            raise Exception("ZERO CROSS PRODUCT")  # Should be unreachable
        c = np.cross(a, b) / np.linalg.norm(np.cross(a, b))
        abc = np.array([a, b, c]).transpose()
        x = np.array([0, 1, 0])
        y = np.array([1, 0, 0])
        z = np.cross(x, y) / np.linalg.norm(np.cross(x, y))
        xyz = np.array([x, y, z]).transpose()

        orientation = np.matmul(
            np.linalg.inv(xyz.transpose()), abc.transpose()
        ).transpose()

    if not (np.matmul(orientation, [1, 0, 0]) == absolute_block_direction).all():
        raise Exception("INVALID ORIENTATION")  # Should be unreachable

print(output)
