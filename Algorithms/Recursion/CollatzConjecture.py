def col(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + col(n//2)
    else:
        return 1 + col(3*n + 1)
    
print(col(4))

# Lift your skinny fists like antennas to heaven - Godspeed You! Black Emperor
# Atrocity Exhibition - Danny Brown
# To Pimp a Butterfly - Kendrick Lamar
# Downward Spiral - Nine Inch Nails
# 36 Chambers - Wu-Tang Clan
# Vespertine - Bjork
# In the court of the crimson king - King Crimson
# House of Balloons - The Weeknd
# Bonito Generation - Kero Kero Bonito
# Madvillainy - Madvillain
# OK Computer - Radiohead
# Abbey Road - The Beatles
# The Glow Pt. 2 - The Microphones
# The Disintegration - The Cures
# LP1 - FKA Twigs
# MAster of Puppets - Metallica
# Saturation - Brockhampton

