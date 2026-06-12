import hashlib

class Block:
    def __init__(self, log, previous_hash):
        self.log = log
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = self.log + self.previous_hash
        return hashlib.sha256(data.encode()).hexdigest()

# Create blockchain logs
block1 = Block("User Login", "0")
block2 = Block("File Uploaded", block1.hash)
block3 = Block("Payment Successful", block2.hash)

print("=== ORIGINAL BLOCKCHAIN ===")

for i, block in enumerate([block1, block2, block3], start=1):
    print(f"\nBlock {i}")
    print("Log:", block.log)
    print("Previous Hash:", block.previous_hash)
    print("Current Hash :", block.hash)

# Tampering with Block 1
print("\n\n=== TAMPERING BLOCK 1 ===")

block1.log = "Hacker Login"
block1.hash = block1.calculate_hash()

print("Modified Log:", block1.log)
print("New Hash:", block1.hash)

# Verify chain
print("\n=== CHAIN VERIFICATION ===")

if block2.previous_hash == block1.hash:
    print("Blockchain is Valid")
else:
    print("Blockchain is Broken!")
