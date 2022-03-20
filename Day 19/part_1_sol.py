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
                #else:
                    #print("Rotation", xi, yi, zi, "already done...")
                
    return arrangements


def overlap(scanner1, scanner2):
    #arrgs_s1 = gen_arrangements(scanner1)
    arrgs_s2 = gen_arrangements(scanner2)

    for beacon in scanner1:
        for arrg_s2 in arrgs_s2:
            overlap_beacons = []
            print("Let's try a new arrangement for scanner2...")
            for i, beacon2 in enumerate(arrg_s2):
                candidate_s2_coords = beacon - beacon2
                print("Comparing beacon", beacon, "with beacon", beacon2)
                print("Candidate coords are", candidate_s2_coords)
                
                
                for j, beacon2test in enumerate(arrg_s2):
                    if candidate_s2_coords.tolist() == [68,-1246,-43 ]:
                        print("THIS HAS TO WORK!!")
                        print(beacon2test)
                        print(beacon - beacon2test)
                        print(candidate_s2_coords)
                        input()
                    #if beacon2test.tolist() == [336, -658, -858]:
                     #   print()
                      #  input()
                    if len(arrgs_s2[i:][j:]) < (12 - len(overlap_beacons)):
                        print("Not enough overlap...")
                        overlap_beacons = []
                        break
                    else:
                        if np.array_equal(beacon - beacon2test, candidate_s2_coords):
                            print("New overlap!", beacon2test)
                            overlap_beacons.append(scanner2[j])
                if len(overlap_beacons) == 12:
                    return overlap_beacons
                #input()
    return []

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
            scanner.append([int(a) for a in line.split(",")])
    scanners.append(scanner)
    scanners = scanners[1:] # 1: to remove that first []

    
    ol = overlap(scanners[0], scanners[1])
    print(ol)
    #print(gen_arrangements([[-336, 658, 858]]))
    #print(len(arrgs))
    #print(beacons)
    #print(len(beacons))
