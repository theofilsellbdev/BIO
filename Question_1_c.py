def prepare_word():
    arr = ""
    while not arr:
        temp = 'OLYMPIAD'
        temp = temp.lower()
        arr = []
        for item in temp:
            if item.isalnum():
                arr.append(int(ord(item) - 96))
        return arr

def encode(arr):
    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i-1]
        if arr[i] > 26:
            arr[i] -= 26
    convert_to_text(arr)
    return arr

def decode(arr):
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i] - arr[i-1]
        if arr[i] <= 0:
            arr[i] += 26
    return arr

def convert_to_text(arr):
    converted = []
    for item in arr:
        converted.append(chr(item+96))
    converted = ''.join(converted)
    converted.upper()
    return converted.upper()

word = prepare_word()


word = encode(word)
encryptions = 1

while convert_to_text(word) != 'OLYMPIAD':
    word = encode(word)
    encryptions += 1

print(convert_to_text(word), encryptions)