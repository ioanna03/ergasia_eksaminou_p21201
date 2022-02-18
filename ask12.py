from urllib.request import Request, urlopen
from binascii import unhexlify, hexlify
from hashlib import sha256
from math import log
import json


def sha256ToHex(randomness):
    randomnessBytes = bytes(randomness, 'utf-8')
    hexedString = sha256(randomnessBytes).hexdigest()

    return hexedString


def mergeRandomness(randomnessArray):

    mergedRandomness = bytes()
    for randomness in randomnessArray:
        randomness = unhexlify(randomness)
        mergedRandomness += randomness

    return hexlify(mergedRandomness)


def findLatest():

    req = Request(' https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = json.loads(urlopen(req).read().decode())
    latestRound = int(str(data["round"]))

    return latestRound

def hextobinary(randomness_array):
    return bin(int(randomness_array, 16))[2:].zfill(8)


def findRangeOfRounds(latestRound):
    firstRound = latestRound - 100
    randomness_array = []

    for roundNumber in range(firstRound, latestRound + 1):
        req = Request('https://drand.cloudflare.com/public/' + str(roundNumber), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
        data = json.loads(urlopen(req).read().decode())

        randomness_array.append(hextobinary(sha256ToHex(data["randomness"])))

    return randomness_array


def main():
    latestRound = findLatest()
    rangeOfRoundsArray = findRangeOfRounds(latestRound)
    mergedRandomness = mergeRandomness(rangeOfRoundsArray).decode()

if __name__ == "__main__":
    main()