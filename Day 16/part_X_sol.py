PUZZLE_INPUT_FILE = "puzzle_input.txt"

def hex2bin(hexa):
    return bin(int(hexa, 16))[2:].zfill(4)

def bin2dec(binary):
    return int(binary, 2)

def parse_literal(binary):
    accum = binary[1:5]

    while binary[0] != "0":
        binary = binary[5:]
        accum += binary[1:5]

    return bin2dec(accum), binary[5:]

def parse_operation(binary, type_id, version_sum):
    length_type = binary[0]
    if length_type == "0":
        length_end = 15
    else:
        length_end = 11

    length = bin2dec(binary[1:1+length_end])
    over = False
    
    binary = binary[1+length_end:]
    original_len = len(binary)
    #print(original_len)

    packets_parsed = 0
    result = 0
    packet_results = []

    while not over:
        new_result, new_binary, version_sum = parse_packet(binary, version_sum)
        packet_results.append(new_result)
        #print(len(new_binary))
        packets_parsed += 1
        if length_type == "0" and (original_len - len(new_binary)) == length:
            over = True
        elif length_type == "1" and packets_parsed == length:
            over = True
        binary = new_binary

    if type_id == 0:
        result = sum(packet_results)
    elif type_id == 1:
        result = 1
        for x in packet_results:
            result *= x
    elif type_id == 2:
        result = min(packet_results)
    elif type_id == 3:
        result = max(packet_results)
    elif type_id == 5:
        result = int(packet_results[0] > packet_results[1])
    elif type_id == 6:
        result = int(packet_results[0] < packet_results[1])
    elif type_id == 7:
        result = int(packet_results[0] == packet_results[1])

    return result, binary, version_sum

def parse_packet(binary, version_sum):
    #print(binary)
    version = bin2dec(binary[:3])
    type_id = bin2dec(binary[3:6])

    version_sum += version

    binary = binary[6:]
    if type_id == 4:
        result, binary = parse_literal(binary)
    else:
        result, binary, version_sum = parse_operation(binary, type_id, version_sum)
    return result, binary, version_sum
    

if __name__ == "__main__":
    puzzle_hex = open(PUZZLE_INPUT_FILE, "r").read()
    puzzle_bin = "".join([hex2bin(h) for h in puzzle_hex])

    print(parse_packet(puzzle_bin, 0))

