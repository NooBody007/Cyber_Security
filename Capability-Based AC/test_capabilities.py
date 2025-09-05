# test_capabilities.py
from capability_system import *

print("Capability-Based Access Control Tests")


alice = Subject("Alice")
bob = Subject("Bob")
charlie = Subject("Charlie")
dave = Subject("Dave")
eve = Subject("Eve")

file1 = Object("File1")
file2 = Object("File2")

# Test 1 - Single Owner Modification
# Alice owns 'File1' and gives Bob read/write permission
alice.capabilities.append(Capability(file1, ['own']))
file1.owners.append(alice)


print("\n==Test1 - Single Owner Modification==\n")
print("Alice owns File1:\t", check_access(alice,file1,'own'))

add_capability(alice, bob, file1, ['read', 'write'])

print("Bob can read File1:\t", check_access(bob, file1, 'read'))   # True
print("Bob can write File1:\t", check_access(bob, file1, 'write')) # True
print("Bob owns File1:\t\t", check_access(bob, file1, 'own'))     # False


# Test 2 - Multiple Ownership
# Alice and Bob owns File2, either can grant Charlie access.
alice.capabilities.append(Capability(file2, ['own']))
bob.capabilities.append(Capability(file2, ['own']))
file2.owners.extend([alice, bob])


print("\n==Test2 - Multiple Ownership==\n")
print("Alice owns File1:\t", check_access(alice,file2,'own'))
print("Bob owns File1:\t\t", check_access(bob,file2,'own'))

add_capability(alice, charlie, file2, ['read'])
add_capability(bob, charlie, file2, ['write'])

print("Alice grants Charlie read:", check_access(charlie, file2, 'read'))   # True
print("Bob grants Charlie write:", check_access(charlie, file2, 'write')) # True



# 3. Dave is not an owner, yet tries to grant Eve access to 'File1'
print("\n==Test3 - Unauthorized Modification==\n")
try:
    add_capability(dave, eve, file1, ['read'])
except PermissionError as e:
    print("Unauthorized modification:", e)

# 4. Alice revokes Charlie's write access to 'File2'
print("\n==Test4 - Revocation Scenario==\n")
remove_capability(alice, charlie, file2,'write')
print("Charlie can read File2:\t", check_access(charlie, file2, 'read'))   # True
print("Charlie can write File2:", check_access(charlie, file2, 'write')) # False

# 5. Alice removes Bob's ownership on 'File2'
print("\n==Test5 - Ownership Removal==\n")
remove_capability(alice, bob, file2,'own')
print("Bob owns File2:\t", check_access(bob, file2, 'own'))             # False
print("File2 owners:\t", get_owners(file2))                   # ['Alice']
