
# convert text to integer in one-to-one correspondence
def text_to_integer(text):
    return int.from_bytes(text.encode(), 'big')

# convert intteger to text in one-to-one correspondence
def integer_to_text(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
