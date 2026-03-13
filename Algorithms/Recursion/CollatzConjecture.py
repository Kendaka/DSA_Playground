def col(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + col(n//2)
    else:
        return 1 + col(3*n + 1)
    
print(col(4))

# To Pimp a Butterfly - Kendrick Lamar
# Vespertine - Bjork
# In the court of the crimson king - King Crimson
# Bonito Generation - Kero Kero Bonito
# OK Computer - Radiohead
# The Glow Pt. 2 - The Microphones
# The Disintegration - The Cures

