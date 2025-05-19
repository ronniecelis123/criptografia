
Sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b,
    0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
    0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7, 0xfd, 0x93, 0x26,
    0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2,
    0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
    0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed,
    0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f,
    0x50, 0x3c, 0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
    0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
    0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14,
    0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
    0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 0xe7, 0xc8, 0x37, 0x6d,
    0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f,
    0x4b, 0xbd, 0x8b, 0x8a, 0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
    0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11,
    0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f,
    0xb0, 0x54, 0xbb, 0x16
]
InvSbox = [0]*256
for i in range(256): InvSbox[Sbox[i]] = i
Rcon = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

def xtime(a): return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else a << 1
def gmul(a,b):
    p = 0
    for _ in range(8):
        if b&1: p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi: a ^= 0x1B
        b >>= 1
    return p

def sub_bytes(s): return [Sbox[b] for b in s]
def inv_sub_bytes(s): return [InvSbox[b] for b in s]

def shift_rows(s):
    return [s[0],s[5],s[10],s[15], s[4],s[9],s[14],s[3],
            s[8],s[13],s[2],s[7], s[12],s[1],s[6],s[11]]
def inv_shift_rows(s):
    return [s[0],s[13],s[10],s[7], s[4],s[1],s[14],s[11],
            s[8],s[5],s[2],s[15], s[12],s[9],s[6],s[3]]

def mix_columns(s):
    out = []
    for i in range(4):
        col = s[i*4:i*4+4]
        out += [
            gmul(col[0],2)^gmul(col[1],3)^col[2]^col[3],
            col[0]^gmul(col[1],2)^gmul(col[2],3)^col[3],
            col[0]^col[1]^gmul(col[2],2)^gmul(col[3],3),
            gmul(col[0],3)^col[1]^col[2]^gmul(col[3],2)
        ]
    return out

def inv_mix_columns(s):
    out = []
    for i in range(4):
        col = s[i*4:i*4+4]
        out += [
            gmul(col[0],14)^gmul(col[1],11)^gmul(col[2],13)^gmul(col[3],9),
            gmul(col[0],9)^gmul(col[1],14)^gmul(col[2],11)^gmul(col[3],13),
            gmul(col[0],13)^gmul(col[1],9)^gmul(col[2],14)^gmul(col[3],11),
            gmul(col[0],11)^gmul(col[1],13)^gmul(col[2],9)^gmul(col[3],14)
        ]
    return out

def add_round_key(s, rk): return [b ^ r for b, r in zip(s, rk)]

def key_expansion(key):
    w = list(key)
    i = 1
    while len(w) < 176:
        temp = w[-4:]
        if len(w) % 16 == 0:
            temp = [Sbox[temp[1]] ^ Rcon[i-1], Sbox[temp[2]], Sbox[temp[3]], Sbox[temp[0]]]
            i += 1
        for j in range(4):
            temp[j] ^= w[-16 + j]
        w.extend(temp)
    return [w[i:i+16] for i in range(0, 176, 16)]

def aes_encrypt_block(p, key):
    state = list(p)
    rkeys = key_expansion(key)
    state = add_round_key(state, rkeys[0])
    for r in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, rkeys[r])
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, rkeys[10])
    return state

def aes_decrypt_block(c, key):
    state = list(c)
    rkeys = key_expansion(key)
    state = add_round_key(state, rkeys[10])
    for r in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, rkeys[r])
        state = inv_mix_columns(state)
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, rkeys[0])
    return state

# Utilidades para test
def str_to_bytes(s): return list(s.encode('utf-8'))
def bytes_to_str(b): return bytes(b).decode('utf-8', errors='ignore')
def pad16(b): return b + [0] * (16 - len(b)) if len(b) < 16 else b[:16]




def menu():
    while True:
        print("\n--- AES-128 en modo ECB ---")
        print("1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            key = input("Ingresa la llave (mínimo 16 caracteres): ")
            texto = input("Ingresa el texto a cifrar (máximo 16 caracteres): ")

            key_bytes = pad16(str_to_bytes(key))
            texto_bytes = pad16(str_to_bytes(texto))

            cifrado = aes_encrypt_block(texto_bytes, key_bytes)
            print("Texto cifrado (hex):", ''.join(f"{x:02X}" for x in cifrado))

        elif opcion == '2':
            key = input("Ingresa la llave (mínimo 16 caracteres): ")
            texto_hex = input("Ingresa el texto cifrado en hexadecimal (32 caracteres): ")

            # Convertir texto_hex a lista de bytes
            try:
                texto_bytes = [int(texto_hex[i:i+2], 16) for i in range(0, len(texto_hex), 2)]
            except ValueError:
                print("Texto cifrado inválido")
                continue

            key_bytes = pad16(str_to_bytes(key))
            descifrado = aes_decrypt_block(texto_bytes, key_bytes)
            print("Texto descifrado:", bytes_to_str(descifrado))

        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
