def pairStrings(out_buf, a, b, n):
    k = 0
    i = 0
    j = 0

    while i < n or j < n:
        if (k & 1) == 0:
            out_buf[k] = a[i]
            i += 1
        else:
            out_buf[k] = b[j]
            j += 1
        k += 1


def makeSerial(userId):
    realKey = bytearray(0x31)

    pairStrings(realKey[0x00:], userId[0x12:], userId[9:], 8)
    pairStrings(realKey[0x10:], userId[:], userId[0x12:], 8)
    pairStrings(realKey[0x20:], userId[9:], userId[:], 8)

    realKey[0x30] = 0
    return realKey


userId = bytearray(input("user id: ").encode())

key = makeSerial(userId)

print(key.decode(errors="ignore"))