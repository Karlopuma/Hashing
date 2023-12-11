import hashlib #Importerer hashlib som er nødvendig for å få python til å forstå hash verdier.

def calculate_hash(file_path, algorithm='sha256'):
    """
    Denne funksjonen kalkulerer hashen til dokumentet i url'en.

    Parameters:
    - file_path: URL'en til dokumentet
    - algorithm: Setter standard hash algoritme til SHA256

    Returns:
    - hash_objects.update oppdaterer hashen hexidigest.
    - Returnerer hash_objects.hexdigest som er hashen til dokumentet.
    """
    hash_object = hashlib.new(algorithm)
    with open(file_path, 'rb') as file:
        # Read the file in chunks to handle large files
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()

def check_file_integrity(file_path, stored_hash):
    """
    Denne funksjonen sjekker om filen er endret

    Parametere:
    - file_path: URL til filen
    - stored_hash: Hash verdien for den originale filen.

    Returns:
    - Returnerer om filen ikke er endret, blir "false" om den ikke er lik og returnerer ikke. 
    """
    current_hash = calculate_hash(file_path)
    return current_hash == stored_hash

def main():

    # URL til filen som skal sammenlignes med den lagrede hashen
    file_path = 'C:/Users/Bergquist/OneDrive - Innlandet fylkeskommune/Organisering og Programmering/Administrasjon og avtaler/ADMAT- Arbeidskrav 4/OriginalFile.docx'

    # Hash'en til den originale filen
    stored_hash = '547963e569aafd4a3a0736cadf1461b4632ab8f73113999dedb14933c8b431de'

    if check_file_integrity(file_path, stored_hash): #Sjekker om filene er like, starter funksjonen check_file_integrity
        print("Filen er ikke endret.")
    else:
        print("Filen er endret.")

if __name__ == "__main__":
    main() # Starter funksjonen main()