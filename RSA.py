import math

def gcd(a, b):
    """Calculate the Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a

def generate_keypair(p, q):
    """Generate public and private keys from two prime numbers."""
    # n is the product of the primes, used as the modulus for both keys
    n = p * q

    # Calculate the totient (phi) of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = 17
    while gcd(e, phi) != 1:
        e += 2

    # Compute the modular inverse of e to find the private key exponent d
    d = pow(e, -1, phi)
    
    # Return Public Key (e, n) and Private Key (d, n)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext_msg):
    """Encrypt a numerical message using the public key."""
    e, n = public_key
    # Formula: c = (m ^ e) % n
    ciphertext = pow(plaintext_msg, e, n)
    return ciphertext

def decrypt(private_key, ciphertext_msg):
    """Decrypt a numerical message using the private key."""
    d, n = private_key
    # Formula: m = (c ^ d) % n
    plaintext = pow(ciphertext_msg, d, n)
    return plaintext

# --- Execution Example ---
if __name__ == "__main__":
    # 1. Select two distinct prime numbers
    prime1 = 61
    prime2 = 53
    
    # 2. Generate the keys
    public, private = generate_keypair(prime1, prime2)
    print(f"Public Key (e, n): {public}")
    print(f"Private Key (d, n): {private}\n")
    
    # 3. Define a secret message (must be smaller than n)
    secret_message = 42
    print(f"Original Message: {secret_message}")
    
    # 4. Encrypt the message
    encrypted_msg = encrypt(public, secret_message)
    print(f"Encrypted Ciphertext: {encrypted_msg}")
    
    # 5. Decrypt the message back
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted Plaintext: {decrypted_msg}")