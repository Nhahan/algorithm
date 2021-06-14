croatia = input()
changes = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
for change in changes:
    croatia = croatia.replace(change, "!")
print(len(croatia))