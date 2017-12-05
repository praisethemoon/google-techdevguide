# Dear Google, Challenge Accepted
# Start Date Tuesday Dec 5th 2017
# End Date: WIP


def getCount(data, pos, length):
    keepStep1 = (pos < length) and str.isdigit(data[pos])
    occNumBuf = ""
    while keepStep1:
        occNumBuf += data[pos]
        pos += 1
        keepStep1 = (pos < length) and str.isdigit(data[pos])
    
    # print(occNumBuf)
    return (pos, int(occNumBuf))

def getString(data, pos, length):
    keepStep2 = (pos < length) and str.isalpha(data[pos])
    dataBuf = ""
    while keepStep2:
        dataBuf += data[pos]
        pos += 1
        keepStep2 = (pos < length) and str.isalpha(data[pos])

    # print(dataBuf)
    return (pos, dataBuf)

def processNextBuf(data, buffer, pos, length):
    # Step 0: Check for immidiate values
    if str.isalpha(data[pos]):
        while (pos < length) and str.isalpha(data[pos]):
            buffer += data[pos]
            pos += 1

        return pos
            
    
    # Step 1: Extracting occurences number
    pos, count = getCount(data, pos, length)

    # Step 2: Extracting string recursively if needed
    pos += 1
    if data[pos] == ']':
        return pos + 1

    if str.isdigit(data[pos]):
        localBuffer = []
        while data[pos] != ']':
            pos = processNextBuf(data, localBuffer, pos, length)
        pos = pos+1
        buffer.append("".join(localBuffer) * count)
        
    else:
        pos, string = getString(data, pos, length)
        buffer.append(string * count)
        pos += 1
    
    return pos

def decompress(data):
    buffer = []
    length = len(data)
    pos = 0
    while(pos < length):
        pos = processNextBuf(data, buffer, pos, length)

    return "".join(buffer)

def run():
    data = "a[]b"
    dstring = decompress(data)

    print(dstring)


if __name__ == '__main__':
    run()
