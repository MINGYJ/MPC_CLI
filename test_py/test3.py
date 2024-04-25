from secretshare import Secret, SecretShare, Share

s=Secret()
shamir=SecretShare(10,10,secret=s)
shares=shamir.split()
print(shares)

get_shamir=SecretShare(10,10,shares=shares)
print(get_shamir.combine().value)