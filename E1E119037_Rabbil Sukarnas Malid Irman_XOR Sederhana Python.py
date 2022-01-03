#XOR Cipher Sederhana
#Rabbil Sukarnas Malid Irman
#E1E119037

def xor_string (string,key):
    result =""
    for c in string:
        result += chr(ord(c) ^ key)
    return result;
print(xor_string ("KRIPTOGRAFI UHO", 0x25))
