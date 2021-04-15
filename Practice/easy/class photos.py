def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if blueShirtHeights[0] > redShirtHeights[0]:
        blue_in_back = True
    else:
        blue_in_back = False
    for i in range(len(blueShirtHeights)):
        if blue_in_back:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
    return True


# redShirtHeights = [5,8,1,3,4]
# blueShirtHeights = [6,9,2,4,5]

redShirtHeights = [6]
blueShirtHeights = [6]

print(classPhotos(redShirtHeights, blueShirtHeights))