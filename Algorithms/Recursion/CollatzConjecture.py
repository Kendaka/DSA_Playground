def col(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + col(n//2)
    else:
        return 1 + col(3*n + 1)
    
print(col(4))

# 1. Two Headed Boy - Neutral Milk Hotel
# 2. Institutionalized - Kendrick Lamar
# 3. CLoudbusting - Kate Bush
# 4. Kashmir - Led Zeppelin
# 5. Let Down - Radiohead
# 6. Like a Rolling Stone - Bob Dylan
# 7. Pagan Poetry - Bjork
# 8. Wicked Games - The Weeknd
# 9. CREAM - Wu Tang Clan
# 10. The Moon - The Microphones
# 11. Devil in a New Dress - Kanye West
# 12. Wish You Were Here - Pink Floyd
# 13. 10 mile stereo - Beach House
# 14. When the doves cry - Prince
# 15. Dead Presidents - Jay Z
# 16. Change - Big Thief
# 17. Fish Bowl - Kero Kero Bonito
# 18. Epitaph - King Crimson
# 19. Kids - MGMT
# 20. Self Control - Frank Ocean
# 21. Starman - David Bowie
# 22. Andromeda - Weyes Blood
# 23.1539 N. Calvert - JPEGMafia
# 24. Helpelessness Blues - Fleet Foxes
# 25. Tunnels - Arcade Fire
# 26. Eraser - Nine Inch Nails
# 27. Dirty Boots - Sonic Youth
# 28. Two Weeks - FKA Twigs
# 29. Run Away With Me - Carly Rae Jepsen
# 30. Skinny Love - Bon Iver
# 31. All along the Watchtower - Jimi Hendrix