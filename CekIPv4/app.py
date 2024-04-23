import re

def is_valid_ipv4(ip):
    # Pattern untuk validasi IPv4
    pattern = re.compile(r"""
        ^              # Start of string
        (?:            # Non-capturing group
          (?:          # Non-capturing group
            25[0-5]|   # Matches 250-255
            2[0-4][0-9]| # Matches 200-249
            1[0-9][0-9]| # Matches 100-199
            [1-9][0-9]| # Matches 10-99
            [0-9]       # Matches 0-9
          )            # End non-capturing group
          \.           # Matches .
        ){3}           # Exactly three times
        (?:            # Non-capturing group
          25[0-5]|     # Matches 250-255
          2[0-4][0-9]| # Matches 200-249
          1[0-9][0-9]| # Matches 100-199
          [1-9][0-9]|  # Matches 10-99
          [0-9]        # Matches 0-9
        )              # End non-capturing group
        $              # End of string
        """, re.X)
    
    return pattern.match(ip) is not None

def find_class(ip):
    first_octet = int(ip.split('.')[0])
    if first_octet >= 1 and first_octet <= 126:
        return 'A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'D'
    elif first_octet >= 240 and first_octet <= 254:
        return 'E'
    else:
        return None

def main():
    while True:
        ip_address = input("Masukkan IP Address (IPv4): ")

        if is_valid_ipv4(ip_address):
            ip_class = find_class(ip_address)
            print(f"IP Address {ip_address} adalah IPv4 yang valid.")
            print(f"Kelas default dari IP Address tersebut adalah kelas {ip_class}.")
            break
        else:
            print("IP Address tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
