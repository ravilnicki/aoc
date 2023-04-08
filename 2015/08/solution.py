import sys


def encode_string(s):
    encoded = ['"']
    for char in s:
        if char == '"':
            encoded.append('\\"')
        elif char == '\\':
            encoded.append('\\\\')
        elif char == '\n':
            encoded.append('\\n')
        elif char == '\r':
            encoded.append('\\r')
        elif char == '\t':
            encoded.append('\\t')
        elif ord(char) < 32 or ord(char) > 126:
            encoded.append('\\x{:02x}'.format(ord(char)))
        else:
            encoded.append(char)
    encoded.append('"')
    return ''.join(encoded)


p1, p2 = 0, 0
for line in sys.stdin:
    line = line.strip()
    l = len(line)
    p1 += l - len(eval(line))
    p2 += len(encode_string(line)) - l
print("Part One:", p1)
print("Part Two:", p2)
