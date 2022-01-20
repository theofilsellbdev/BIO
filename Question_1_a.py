def take_input():
    arr = ""
    while not arr:
        temp = input('enter word: ')
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

word = take_input()
decoded = decode(word)
print(convert_to_text(decoded))

