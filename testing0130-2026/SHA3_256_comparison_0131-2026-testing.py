#0130-2026 script to confirm SHA 256 signatures
# NOTE: powershell lacks SHA3-256 algorithm, so this script was necessary

import hashlib

# update two lines below for each different file 
path = "c:/Users/TJ/Downloads/sqlite-tools-win-x64-3510200.zip"
signature_expected ="d8f6cbab468c0b7a60fb7c1ebbeb1d14ffda25336d9295473c218532266e85d9"

with open(path, "rb") as file:
    s = hashlib.sha3_256(file.read())
    # print(s.name)
    # print(s.digest_size)
    # print(s.hexdigest())
    
    signature_down_file = s.hexdigest()
    print(signature_down_file)
    print(len(signature_down_file))
    print(signature_expected)
    print(len(signature_expected))

    if signature_down_file == signature_expected:
        print("yes they match ")
    else:
        print("WARNING SHA SIGNATURES DONT MATCH")