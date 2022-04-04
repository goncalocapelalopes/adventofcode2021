PUZZLE_INPUT_FILE = "puzzle_input.txt"

def pad_image(image, char):
    image = [char*2 + line + char*2 for line in image]
    image = [char*len(image[0])] * 2 + image + [char*len(image[0])] * 2
    return image

def pixels2number(pixels):
    binary = "".join(["1" if p=="#" else "0" for p in pixels])
    return int(binary, 2)

def count_lit_pixels(image):
    return sum([sum([1 if p=="#" else 0 for p in row]) for row in image])

def enhance_image(image, algorithm, last_pad):
    new_image = []
    for i in range(1, len(image)-1):
        row = ""
        for j in range(1, len(image[0])-1):
            pixels = image[i-1][j-1:j+2] + image[i][j-1:j+2] + image[i+1][j-1:j+2]
            number = pixels2number(pixels)
            new_pixel = algorithm[number]
            row += new_pixel
        new_image.append(row)
    if last_pad == "." and algorithm[0] == "#":
        pad_char = "#"
    elif last_pad == "#" and algorithm[-1] == ".":
        pad_char = "."
    else:
        pad_char = last_pad
    
    return pad_image(new_image, pad_char), pad_char

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
    image = pad_image(image, ".")
    last_pad = "."
    print("Lit pixels ->", count_lit_pixels(image))
    for _ in range(50):
        image, last_pad = enhance_image(image, algorithm, last_pad)
        #for row in image:
        #    print(row)
        #if last_pad == "#":
        #    print("Lit pixels -> infinite")
        #else:
        #    print("Lit pixels ->", count_lit_pixels(image))
    print("Lit pixels ->", count_lit_pixels(image))
