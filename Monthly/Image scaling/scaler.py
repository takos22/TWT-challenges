def scale_to(img, size=64):
    output_img = [[0] * size for _ in range(size)]
    scaler = size // len(img)
    print(scaler)
    for i, line in enumerate(img):
        for j, pixel in enumerate(line):
            for i_off in range(scaler):
                for j_off in range(scaler):
                    output_img[(i * scaler) +
                               i_off][(j * scaler) + j_off] = pixel
    return output_img


print(scale_to(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]],
    16))

print(scale_to([[1, 2], [3, 4]], 4))
