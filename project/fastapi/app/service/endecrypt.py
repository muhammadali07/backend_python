from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

def endecrypt(key, plaintext):
    # textended = b""
    if key == 'e':
        ciphertext = f.encrypt(plaintext)
        print(ciphertext)
    else:
        decryptedtext = f.decrypt(plaintext)
        print(decryptedtext)


endecrypt(key="d", plaintext=b'gAAAAABkEnYuRvzFeVnjzKG8cGG5QgaYhlIbqWJpsU5m_a22QeJYu0rDRPJmhCSb7z6MIrBHwqXGO6PgPxm0KoREbGubVNPjRg==')