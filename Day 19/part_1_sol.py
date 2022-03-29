import numpy as np
PUZZLE_INPUT_FILE = "puzzle_input_extra.txt"

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
                    #print("Rotation", xi, yi, zi, "not yet done!")
                    scanner_rot = np.matmul(rot_z, scanner.T)
                    arrangements.append(scanner_rot.T)
                    rotations_done.append(rot_z)
                    rotations.append(rot_z)
                #else:
                    #print("Rotation", xi, yi, zi, "already done...")
                
    return arrangements, rotations

def array2matrix(array, len_diff):
    return np.repeat(np.reshape(array, (len(array), 1, 3)), len(array)+len_diff, axis=1)

def overlap_v2(scanner1, scanner2):
    len_diff = len(scanner2) - len(scanner1)
    scanner1_matrix = array2matrix(scanner1, len_diff)
    arrgs_s2, rotations = gen_arrangements(scanner2)

    for arrg_s2, rotation in zip(arrgs_s2, rotations):
        scanner2_matrix = np.transpose(array2matrix(arrg_s2, -len_diff), axes=(1, 0, 2))
        matrix_diff = scanner1_matrix - scanner2_matrix
        
        #input()
        matrix_diff_reshaped = matrix_diff.reshape(matrix_diff.shape[0] * matrix_diff.shape[1], matrix_diff.shape[2])
        unique_diff, unique_counts = np.unique(matrix_diff_reshaped, return_counts=True, axis=0)
        coords_count = max(unique_counts)
        if coords_count >= 12:
            # fetch the overlap from scanner2
            coords = unique_diff[np.argmax(unique_counts)]
            #print(coords)
            #print(matrix_diff.shape)
            #print((matrix_diff == coords).all(axis=2))
            #input()
            filter_diff = (np.transpose(matrix_diff, axes=(1, 0, 2)) == coords).all(axis=2)
            overlap = array2matrix(scanner2, -len_diff)[filter_diff]
            return overlap, np.array(coords), rotation
    
    return None, None, None

def overlap(scanner1, scanner2):
    #arrgs_s1 = gen_arrangements(scanner1)
    arrgs_s2, rotations = gen_arrangements(scanner2)

    for beacon in scanner1:
        for arrg_s2, rotation in zip(arrgs_s2, rotations):
            #print("Let's try a new arrangement for scanner2...")
            for i, beacon2 in enumerate(arrg_s2):
                overlap_beacons = []
                candidate_s2_coords = beacon - beacon2
                #print("Comparing beacon", beacon, "with beacon", beacon2)
                #print("Candidate coords are", candidate_s2_coords)
                
               # if np.array_equal(candidate_s2_coords, [68,-1246,-43]):
                #    input()
                temp_s1 = scanner1.copy()
                temp_s2 = arrg_s2.copy()
                for i, beacon1temp in enumerate(temp_s1):
                    for j, beacon2temp in enumerate(temp_s2):
                       # if np.array_equal(candidate_s2_coords, [68,-1246,-43]):
                        #    print("Comparing beacon", beacon1temp, "with beacon", beacon2temp)
                         #   input()
                        if len(overlap_beacons) + len(temp_s1) < 12:
                         #   print("Not enough overlap left...")
                            overlap_beacons = []
                            break
                        elif np.array_equal(beacon1temp-beacon2temp, candidate_s2_coords):
                          #  print("New overlap!", beacon1temp, "with ", beacon2temp)
                           # print(beacon1temp - beacon2temp)
                            #print(candidate_s2_coords)
                            overlap_beacons.append(scanner2[j])
                            #temp_s1 = np.delete(temp_s1, i, axis=0)
                            #temp_s2 = np.delete(temp_s2, j, axis=0)
                            break
                if len(overlap_beacons) >= 12:
                    return overlap_beacons, candidate_s2_coords, rotation
                
    return None, None

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

    #ol, coords = overlap_v2(scanners[0], scanners[1])

    beacons = np.array(scanners[0])
    beacons_map = []
    coords = {"0->-1": np.zeros((3))}
    rotations = {"0->-1": np.identity(3)}
    path = {"0": -1}
    conversions = {0: np.zeros((3))}
    while len(conversions.keys()) < len(scanners):
        for i in range(len(scanners)):
            for j in range(len(scanners)):
                if j in conversions.keys() or i == j:
                    print("Skipping", i, "with beacon", j)
                    continue
                else:
                    print("Comparing beacon", i, "with beacon", j)
                overlap, new_coords, rotation = overlap_v2(scanners[i], scanners[j])
                if overlap is None:
                    print("No overlap lul")
                    continue
                coords[f"{j}->{i}"] = new_coords
                rotations[f"{j}->{i}"] = rotation
                if path.get(str(j)) is None:
                    path[str(j)] = i
                
                #calculate which of the new beacons to add
                i_conversion = i
                j_conversion = j
                converted_overlap = overlap
                prev_coords = None
                conversion_coords = np.zeros((3))
                print(new_coords)
                converted_overlap = overlap
                while j_conversion != -1:
                    
                    key = f"{j_conversion}->{i_conversion}"
                    print(key)
                    print(coords[key])
                    print(prev_coords)
                    conversion_rotation_matrix = rotations[key]
                    
                    print(conversion_rotation_matrix)
                    conversion_rotation_matrix = np.linalg.inv(rotations[key])
                    print(converted_overlap)
                    converted_overlap = np.matmul(conversion_rotation_matrix, converted_overlap.T).T + coords[key]
                    print(converted_overlap)
                    if prev_coords is not None:
                        
                        print(conversion_rotation_matrix)
                        conversion_coords += np.matmul(conversion_rotation_matrix, prev_coords)
                    print(conversion_coords)
                    input()
                    if i_conversion == -1:
                        break
                    j_conversion = i_conversion
                    i_conversion = path[str(i_conversion)]
                    prev_coords = coords[key]
                conversions[j] = conversion_coords
        
    print(conversions)

    beacons = beacons[beacons[:, 0].argsort()]
    print(beacons)
    print(len(beacons))
    

    #print(ol)
    #print(len(ol))
    #print(coords)
    #print(gen_arrangements(scanners[1]))
    #print(len(arrgs))
    #print(beacons)
    #print(len(beacons))
