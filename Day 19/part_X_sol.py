import numpy as np
PUZZLE_INPUT_FILE = "puzzle_input.txt"

rx = np.array([
    [1, 0, 0],
    [0, 0, -1],
    [0, 1, 0]
])

ry = np.array([
    [0, 0, 1],
    [0, 1, 0],
    [-1, 0, 0]
])

rz = np.array([
    [0, -1, 0],
    [1, 0, 0],
    [0, 0, 1]
])

def gen_arrangements(scanner):
    arrangements = []
    rotations_done = []
    rotations = []

    scanner = np.array(scanner)
    for xi in range(4):
        rot_mat_x = np.linalg.matrix_power(rx, xi)
        for yi in range(4):
            rot_mat_y = np.linalg.matrix_power(ry, yi)
            rot_y = np.matmul(rot_mat_x, rot_mat_y)
            for zi in range(4):
                rot_mat_z = np.linalg.matrix_power(rz, zi)
                rot_z = np.matmul(rot_y, rot_mat_z)
                if not any(np.array_equal(rot_z, x) for x in rotations_done):
                    scanner_rot = np.matmul(rot_z, scanner.T)
                    arrangements.append(scanner_rot.T)
                    rotations_done.append(rot_z)
                    rotations.append(rot_z)
                
    return arrangements, rotations

def array2matrix(array, len_diff):
    return np.repeat(np.reshape(array, (len(array), 1, 3)), len(array)+len_diff, axis=1)

def overlap(scanner1, scanner2):
    len_diff = len(scanner2) - len(scanner1)
    scanner1_matrix = array2matrix(scanner1, len_diff)
    arrgs_s2, rotations = gen_arrangements(scanner2)

    for arrg_s2, rotation in zip(arrgs_s2, rotations):
        scanner2_matrix = np.transpose(array2matrix(arrg_s2, -len_diff), axes=(1, 0, 2))
        matrix_diff = scanner1_matrix - scanner2_matrix

        matrix_diff_reshaped = matrix_diff.reshape(matrix_diff.shape[0] * matrix_diff.shape[1], matrix_diff.shape[2])
        unique_diff, unique_counts = np.unique(matrix_diff_reshaped, return_counts=True, axis=0)
        coords_count = max(unique_counts)
        if coords_count >= 12:
            # fetch the overlap from scanner2
            coords = unique_diff[np.argmax(unique_counts)]
            filter_diff = (np.transpose(matrix_diff, axes=(1, 0, 2)) == coords).all(axis=2)
            overlap = array2matrix(scanner2, -len_diff)[filter_diff]
            return overlap, np.array(coords), rotation
    
    return None, None, None

def manhattan(scanner1, scanner2):
    return sum([abs(scanner1[i] - scanner2[i]) for i in range(3)])

def largest_manhattan(conversions_dict):
    dists = []
    values_lst = list(conversions_dict.values())
    for i in range(len(values_lst)-1):
        for j in range(i+1, len(values_lst)):
            dists.append(manhattan(values_lst[i], values_lst[j]))
    return int(max(dists))

if __name__ == "__main__":
    scanners = []
    lines = open(PUZZLE_INPUT_FILE, "r").readlines()
    scanner = []
    for line in lines:
        if line.startswith("--"):
            scanners.append(scanner)
            scanner = []
        elif line.strip() == "":
            continue
        else:
            scanner.append(np.array([int(a) for a in line.split(",")]))
    scanners.append(scanner)
    scanners = scanners[1:] # 1: to remove that first []

    beacons = np.array(scanners[0])
    beacons_map = []
    coords = {"0->-1": np.zeros((3))}
    rotations = {"0->-1": np.identity(3)}
    path = {"0": -1}
    conversions = {0: np.zeros((3))}
    while len(conversions.keys()) < len(scanners):
        for i in range(len(scanners)):
            if i not in conversions.keys():
                continue
            for j in range(len(scanners)):
                if j in conversions.keys() or i == j:
                    continue
                new_overlap, new_coords, rotation = overlap(scanners[i], scanners[j])
                if new_overlap is None:
                    continue
                coords[f"{j}->{i}"] = new_coords
                rotations[f"{j}->{i}"] = rotation
                if path.get(str(j)) is None:
                    path[str(j)] = i
                
                #calculate which of the new beacons to add
                i_conversion = i
                j_conversion = j
                prev_coords = None
                conversion_coords = np.zeros((3))
                converted_beacons = np.array(scanners[j])
                while j_conversion != -1: 
                    key = f"{j_conversion}->{i_conversion}"
                    converted_beacons = np.matmul(rotations[key], converted_beacons.T).T + coords[key]
                    if prev_coords is not None:
                        conversion_coords += prev_coords
                        conversion_coords = np.matmul(rotations[key], conversion_coords)
                    if i_conversion == -1:
                        break
                    j_conversion = i_conversion
                    i_conversion = path[str(i_conversion)]
                    prev_coords = coords[key]
                conversions[j] = conversion_coords
                beacons = np.append(beacons, converted_beacons, axis=0)
        


    beacons = beacons[beacons[:, 0].argsort()]
    unique_beacons = np.unique(beacons, axis=0)

    print(len(unique_beacons))

    print(largest_manhattan(conversions))