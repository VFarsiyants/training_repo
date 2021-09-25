"""
Закодировать любую строку по алгоритму Хаффмана.
"""


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def encode_huffman(string):
    # calculate letters quantity in string
    letters = []
    letters_qty = []
    for letter in string:
        if letter in letters:
            continue
        letters += [letter]
        letters_qty += [string.count(letter)]
    # sorting list according to quantity of letters in string to be coded
    list_to_code = sorted(list(zip(letters, letters_qty)), key=lambda x: x[1])
    # creating huffman tree
    while len(list_to_code) > 2:
        # combine two letters of list in node
        tree = Node()
        tree.left = list_to_code[0][0]
        tree.right = list_to_code[1][0]
        # every time we combine letter in node we should combine two letters quantities and resort list
        qty = list_to_code[0][1] + list_to_code[1][1]
        list_to_code = sorted([(tree, qty)] + list_to_code[2:], key=lambda x: x[1])
    huffman_tree = Node(None, list_to_code[0][0], list_to_code[1][0])
    # now we should receive huffman code fo each letter
    is_there_nodes = True
    huffman_nodes = [(huffman_tree.left, '0'), (huffman_tree.right, '1')]
    while is_there_nodes:
        is_there_nodes = False
        result = []
        for node in huffman_nodes:
            # we should unpack each node and add 0 or 1 depending on unpacking direction
            if isinstance(node[0], Node):
                result += [(node[0].left, node[1] + '0'), (node[0].right, node[1] + '1')]
                is_there_nodes = True
            else:
                result += [(node[0], node[1])]
        huffman_nodes = result

    huffman_codes = {k: v for k, v in huffman_nodes}
    # print(f'huffman codes table used for encoding')
    # for k, v in huffman_codes.items():
    #     print(f'\'{k}\' - {v}')
    return ''.join([huffman_codes[letter] for letter in string]), huffman_codes


def huffman_decode(huffman_string, huffman_codes):
    huffman_codes = {v: k for k, v in huffman_codes.items()}
    result = ''
    huffman_key = ''
    while huffman_string:
        huffman_key += huffman_string[0]
        huffman_string = huffman_string[1:]
        if huffman_key in huffman_codes.keys():
            result += huffman_codes[huffman_key]
            huffman_key = ''
    return result


string_to_code = 'I can code message like Huffman!'
encoded_string, codes_table = encode_huffman(string_to_code)
print('encoded string')
print(encoded_string)
print(codes_table)
print('*' * 150)
print('decoded_string')
print(huffman_decode(encoded_string, codes_table))

