from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding

# Student generates a key pair
student_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
student_public_key = student_private_key.public_key()

# Unique ID encrypted with the student's public key
student_id = b"STUDENT_123"
encrypted_id = student_public_key.encrypt(
    student_id,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Student decrypts the ID using their private key
decrypted_id = student_private_key.decrypt(
    encrypted_id,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Student prepares the assignment and combines it with the decrypted ID
assignment = b"Assignment content"
combined_data = assignment + decrypted_id

# Student calculates the hash of the combined data
hasher = hashes.Hash(hashes.SHA256())
hasher.update(combined_data)
combined_hash = hasher.finalize()

# Student signs the hash with their private key
signature = student_private_key.sign(
    combined_hash,
    asym_padding.PSS(
        mgf=asym_padding.MGF1(hashes.SHA256()),
        salt_length=asym_padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Instructor verifies the submission
try:
    # Combine the received assignment and decrypted ID
    combined_data_check = assignment + decrypted_id

    # Calculate the hash of the combined data
    hasher = hashes.Hash(hashes.SHA256())
    hasher.update(combined_data_check)
    combined_hash_check = hasher.finalize()

    # Verify the signature
    student_public_key.verify(
        signature,
        combined_hash_check,
        asym_padding.PSS(
            mgf=asym_padding.MGF1(hashes.SHA256()),
            salt_length=asym_padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Submission verified. The assignment is accepted.")
except Exception as e:
    print("Verification failed:", e)