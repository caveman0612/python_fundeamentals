def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    answer = 0
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()
    for i in range(len(redShirtSpeeds)):
        answer += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return answer


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, True))