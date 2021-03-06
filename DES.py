# DES implimentation , by Spencer Little, mrlittle@uw.edu
import re

s_boxs =  [

[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],

[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

def byter_to_list(byter, as_byte = True):
    bits = []
    bitsfix = []
    as_bits = []
    for num in byter: # parse our byte array
        bits.append(str(bin(num)))
    for bites in bits: # add zeros the left, fix size of the bits in bytes
        byte = bites[2:]
        while len(byte)!=8:
            zeros = "0"*(8-len(byte))
            byte = zeros + byte
        bitsfix.append(byte)
    if not as_byte:
        for byte in bitsfix:
            for bit in byte:
                as_bits.append(bit)
        return as_bits
    return bitsfix

def exp_box(r_bytes):
    r_byt_exp = []
    e_box = [32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]
    for pos in e_box:
        r_byt_exp.append(r_bytes[pos-1])
    return r_byt_exp

def xor_w_key(right_bits, key):
    xored_l = []
    for i in range(len(right_bits)):
        xored_l.append(right_bits[i] ^ key[i])
    return xored_l

def s_boxes(right_b):
    P = [16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25]
    right_byts = []
    right_bits = ""
    right_bit_six = []
    s_row_col = []
    s_out = []
    s_out_bits = ""
    p_out = []
    ind = 0
    for num in right_b:
        bits = format(num, 'b')
        if len(bits)!=8:
            zeros = '0'*(8-len(bits))
            bits = zeros + bits
        right_byts.append(bits)
    for byt in right_byts:
        for bit in byt:
            right_bits += bit
    for i in range(int(len(right_bits)/6)):
        right_bit_six.append(right_bits[ind:(i+1)*6])
        ind = (i+1)*6
    for six_bit in right_bit_six:
        row = six_bit[0]+six_bit[5]
        column = six_bit[1:5]
        row_c = [int(row, 2), int(column, 2)]
        s_row_col.append(row_c)
    for i in range(8): # 0 is row, 1 is col
        s_int = s_boxs[i][(s_row_col[i][0])][(s_row_col[i][1])]
        s_out.append(s_int)
    for num in s_out:
        bits = format(num, 'b')
        if len(bits)<4:
            zeros = '0'*(8-len(bits))
            bits = zeros + bits
        while len(bits)>4:
            bits = bits[1:]
        s_out_bits += bits
    for pos in P:
        p_out.append(s_out_bits[pos-1])
    return p_out

def bit_shift_left(bits): # shifts bits, takes list of bits
    bits_l = []
    for i in range(len(bits)):
        if i==len(bits)-1:
            bits_l.append(bits[0])
        else:
            bits_l.append(bits[i+1])
    return bits_l

def bits_to_int(bits): # bits to intergers, takes list of bits
    byte_l = []
    byte_st = []
    bits_int = []
    ind = 0
    for i in range(int(len(bits)/8)):
        byte_l.append(bits[ind:(i+1)*8])
        ind = (i+1)*8
    for byte in byte_l:
        strbyte = ""
        for bit in byte:
            strbyte+=bit
        byte_st.append(strbyte)
    for byte in byte_st:
        bits_int.append(int(byte, 2))
    return bits_int


def init_perm(byter1): # initial permuattion, takes 8 bytes in a byte array
    perm_seq = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
    blocks = []
    IPbits = []
    bitsfix = byter_to_list(byter1)
    # PKCS5 Padding
    if len(bitsfix)!=8: # <------ probably want to rethink this padding
        req_byts = 8 - len(bitsfix)
        pad = str(bin(req_byts))[2:]
        if len(pad)!=8:
            zeros = "0"*(8-len(pad))
            pad = zeros + pad
        for i in range(req_byts):
            bitsfix.append(pad)
    for byte in bitsfix:
        for bit in byte:
            blocks.append(bit)
    for ind in perm_seq:
        IPbits.append(blocks[ind-1])

    return IPbits

def key_perm(key, perm_num): # key as byetarray, perm_num as int
    c_blk = []
    d_blk = []
    c_sub = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36]

    d_sub = [63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]

    pc_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21,
            10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20,
            13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51,
            45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42,
            50, 36, 29, 32]

    key_bits = []
    par = []
    key_n = []
    cd_blk = []
    l_shfts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] # or these could be cumulative but that would be less efficient

    key_bytes = byter_to_list(key)
    for byte in key_bytes: # saving parity bits
        par.append(byte[7])
    for byte in key_bytes:
        for bit in byte:
            key_bits.append(bit)
    for i in range(28):
        c_blk.append(key_bits[c_sub[i]])
        d_blk.append(key_bits[d_sub[i]])
    for i in range(perm_num):
        for shift in range(l_shfts[i]): # cumulative approach, assuming shifts remain after each round
            c_blk = bit_shift_left(c_blk)
            d_blk = bit_shift_left(d_blk)
    cd_blk = c_blk + d_blk
    for pos in pc_2:
        key_n.append(cd_blk[pos-1])
    key_n = bits_to_int(key_n)
    return key_n # return as intergers for xoring

def main_crypt_seq(bytes_crypt, key, e_c): # takes ints as byes, and key as bytearray
    p_i = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]
    pad_pattern = r"(.*,+(2,){2,2}|.*,+(3,){3,3}|.*,+(4,){4,4}|.*,+(5,){5,5}|.*,+(6,){6,6}|.*,+(7,){7,7})$"
    bytes_crypt = init_perm(bytes_crypt) # inital permuattion
    if len(bytes_crypt)!=64:
        print("Something is wrong. Input not 8 bytes")
        return 1
    lr_bits = []
    left_bits = bytes_crypt[0:32]
    right_bits = bytes_crypt[32:]
    out_bits = []
    out_bits_int = []
    o_bits_str = ""
    round_rng = range(16) if e_c==True else range(15, -1, -1)
    stop = 15 if e_c==True else 0
    for i in round_rng:
        temp = exp_box(right_bits)
        temp = xor_w_key(bits_to_int(temp), key_perm(key, i))
        temp = s_boxes(temp)
        left_bits = xor_w_key(bits_to_int(left_bits), bits_to_int(temp))
        left_bits = byter_to_list(left_bits, False)
        if i == stop:
            break
        place_hld = right_bits
        right_bits = left_bits
        left_bits = place_hld
    lr_bits = left_bits + right_bits
    for pos in p_i: # final permutation
        out_bits.append(lr_bits[pos-1])
    out_bits_int = bits_to_int(out_bits)
    for num in out_bits_int:              # see if there is more efficient way to do this
        o_bits_str += str(num) + ","           # if only one byte is padded, it remains after decryption
    if re.match(pad_pattern, o_bits_str): # check for padding and remove
        for i in range(o_bits_str[-2]): # should I only check last 64 bits of file?
            out_bits_int.pop(-1)
    out_bytes = bytearray(out_bits_int)

    return out_bytes

def main_crypt_trp(bytes_crypt, key, e_c):
    if e_c:
        enc_byte = main_crypt_seq(bytes_crypt, key[:8], True)
        enc_byte = main_crypt_seq(enc_byte, key[8:16], False)
        enc_byte = main_crypt_seq(enc_byte, key[16:], True)
    else:
        enc_byte = main_crypt_seq(bytes_crypt, key[16:], False)
        enc_byte = main_crypt_seq(enc_byte, key[8:16], True)
        enc_byte = main_crypt_seq(enc_byte, key[:8], False)
    return enc_byte

if __name__=='__main__':
    user_f = input("File to be ciphered (path to file, or filename if running from directory: ")
    user_f_cf = input("Desired name of output file: ")
    enc_dec = input("1. Encryption 0. Decryption: ")
    trp_d = int(input("1. Triple-DES, 0. Normal DES"))
    if trp_d:
        key_u = input("192-bit key:")
    else:
        key_u = input("64-bit key: ")
    key = []
    for val in key_u:                   # key can be int array of bytearray
        if val not in list(range(10)):  # simplest to use interger array
            key.append(ord(val))
        else:
            key.append(val)

    encrypt = int(enc_dec)
    enc_file = user_f
    wrt_file = user_f_cf
    byte_r = []
    enc_byte_r = []
    with open(enc_file, 'rb') as textf:
        bytef = textf.read(8)
        while bytef:
            print(bytef)
            byte_r.append(bytef)
            bytef = textf.read(8)
    for fbytes in byte_r:
        if trp_d:
            enc_byte_r.append(main_crypt_trp(fbytes, key, encrypt))
        else:
            enc_byte_r.append(main_crypt_seq(fbytes, key, encrypt))
    with open(wrt_file, 'wb') as wrtf:
        for fbytes in enc_byte_r:
            wrtf.write(fbytes)

    print("encryption successful.")
