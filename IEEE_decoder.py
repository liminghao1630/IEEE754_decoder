import struct

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]


def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)


def binaryToFloat(value):
    hx = hex(int(value, 2))
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]


def IEEE754_to_float(hex_str):
    #     hex_str = "407ad00000000000"
    scale = 16  ## equals to hexadecimal
    num_of_bits = 64
    bin_str = bin(int(hex_str, scale))[2:].zfill(num_of_bits)

    result_float = binaryToFloat(bin_str)
    #     print('Decimal equivalent of ' + bin_str)
    #     print(result_float)
    return result_float


def BBox_decoder(BBox_list):
    result_list = []
    for hex in BBox_list:
        result_list.append(IEEE754_to_float(hex))
    return result_list

if __name__ == '__main__':
    # 4049d51666666667 4082b47f33333333 404d6f8ccccccccd 40828ee266666666
    # 51 598 58 593
    print(IEEE754_to_float('404d6f8ccccccccd'))
