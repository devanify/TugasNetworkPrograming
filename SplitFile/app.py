import os

def split_file(input_file, max_lines=100):
    # Membaca file teks
    try:
        with open(input_file, 'r', encoding='latin-1') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return

    # Membuat folder untuk menyimpan file-file yang dipecah
    output_folder = "split_files"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Menghitung jumlah file yang akan dihasilkan
    num_file = 1
    num_lines = 0

    split_file_name = f"{os.path.splitext(os.path.basename(input_file))[0]}_split_{num_file}.txt"
    with open(os.path.join(output_folder, split_file_name), 'w', encoding='utf-8') as file:
        for line in lines:
            if num_lines < max_lines:
                file.write(line)
                num_lines += 1
            else:
                num_file += 1
                num_lines = 0
                split_file_name = f"{os.path.splitext(os.path.basename(input_file))[0]}_split_{num_file}.txt"
                file = open(os.path.join(output_folder, split_file_name), 'w', encoding='utf-8')
                file.write(line)
                num_lines += 1

    print(f"{num_file} file telah dibuat di folder {output_folder}.")

def main():
    # Input path file teks
    input_file = input("Masukkan path dari file teks: ").strip()

    # Input jumlah baris maksimal
    max_lines_input = input("Masukkan jumlah baris maksimal (default: 100): ").strip()
    if max_lines_input:
        max_lines = int(max_lines_input)
    else:
        max_lines = 100

    split_file(input_file, max_lines)

if __name__ == "__main__":
    main()
