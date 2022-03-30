PUZZLE_INPUT_FILE = "puzzle_input.txt"

def pad_image(image):
    image = [".." + line + ".." for line in image]
    image = ["."*len(image[0])] * 2 + image + ["."*len(image[0])] * 2
    return image

def pixels2number(pixels):
    binary = "".join(["1" if p=="#" else "0" for p in pixels])
    return int(binary, 2)

def count_lit_pixels(image):
    total_sum = 0
    for row in image:
        for c in row:
            if c == "#":
                total_sum += 1
    return total_sum
    #return sum([sum([1 if p=="#" else 0 for p in row]) for row in image])

def enhance_image(image, algorithm):
    new_image = []
    for i in range(1, len(image)-1):
        row = ""
        for j in range(1, len(image[0])-1):
            pixels = image[i-1][j-1:j+2] + image[i][j-1:j+2] + image[i+1][j-1:j+2]
            number = pixels2number(pixels)
            new_pixel = algorithm[number]
            row += new_pixel
        new_image.append(row)
    return pad_image(new_image)

if __name__ == "__main__":
    lines = open(PUZZLE_INPUT_FILE, "r").readlines()
    algorithm = ""
    for i, line in enumerate(lines):
        if line == "\n":
            break
        else:
            algorithm += line.strip("\n")
    # Create padded image
    image = [line.strip("\n") for line in lines[i+1:]]
    image = pad_image(image)
    
    print(algorithm)
    print("Lit pixels ->", count_lit_pixels(image))
    for i in range(2):
        
        image = enhance_image(image, algorithm)
        for row in image:
            print(row)
        print("Lit pixels ->", count_lit_pixels(image))
