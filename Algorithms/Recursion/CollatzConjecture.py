def col(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + col(n//2)
    else:
        return 1 + col(3*n + 1)
    
print(col(4))

# Lift your skinny fists like antennas to heaven - Godspeed You! Black Emperor
# To Pimp a Butterfly - Kendrick Lamar
# 36 Chambers - Wu-Tang Clan
# Vespertine - Bjork
# In the court of the crimson king - King Crimson
# House of Balloons - The Weeknd
# Bonito Generation - Kero Kero Bonito
# Madvillainy - Madvillain
# OK Computer - Radiohead
# The Glow Pt. 2 - The Microphones
# The Disintegration - The Cures
# Saturation - Brockhampton

