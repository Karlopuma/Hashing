import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read the file in chunks to handle large files
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def save_hash_to_file(file_path, output_file):
    hash_value = calculate_sha256(file_path)
    with open(output_file, "w") as output:
        output.write(hash_value)

if __name__ == "__main__":
    input_file = "C:/Users/Bergquist/OneDrive - Innlandet fylkeskommune/Organisering og Programmering/Administrasjon og avtaler/ADMAT- Arbeidskrav 4/OriginalFile.docx"  
    output_file = "hashes.txt"

    save_hash_to_file(input_file, output_file)