import libbitcoin.bitcoin_utils

def binary_str_to_bytes(str):
    split = lambda str: [str[x:x + 8] for x in range(0, len(str), 8)]
    add_padding = lambda str: str + ((8 - len(str)) * "0")
    result = b""
    for bin_byte in split(str):
        bin_byte = add_padding(bin_byte)
        value = int(bin_byte, 2)
        assert value < 256
        result += bytes([value])
    return result

# For more info see libbitcoin/include/bitcoin/bitcoin/utility/binary.hpp
class Binary:

    BitsPerBlock = 8

    @staticmethod
    def blocks_size(bitsize):
        if bitsize == 0:
            return 0;
        return (bitsize - 1) // Binary.BitsPerBlock + 1

    def __init__(self, size, blocks):
        """Set bitsize and block data."""
        self._size = size
        self._blocks = blocks

    @classmethod
    def from_string(cls, repr):
        if type(repr) != str and set("01") != set(repr):
            return None
        return cls(len(repr), binary_str_to_bytes(repr))

    @classmethod
    def from_address(cls, address):
        _, address_hash = \
            libbitcoin.bitcoin_utils.bc_address_to_hash_160(address)
        return cls(160, address_hash)

    def resize(self, size):
        self._size = size
        blks_size = Binary.blocks_size(self._size)
        self._blocks = self._blocks[:blks_size]
        # Pad with zero bytes any remaining space.
        self._blocks += b"\x00" * (blks_size - len(self._blocks))

    def __getitem__(self, i):
        assert i < self._size
        block_index = i // Binary.BitsPerBlock
        block = self._blocks[block_index]
        offset = i - (block_index * Binary.BitsPerBlock)
        bitmask = 1 << (Binary.BitsPerBlock - offset - 1)
        return (block & bitmask) > 0

    @property
    def blocks(self):
        """Return block data."""
        return self._blocks
    @property
    def size(self):
        """Return bitsize of binary value."""
        return self._size

    def __repr__(self):
        result = ""
        for i in range(self._size):
            if self[i]:
                result += "1"
            else:
                result += "0"
        return result

    def __eq__(self, other):
        min_size = min(self._size, other._size)
        for i in range(min_size):
            if self[i] != other[i]:
                return False
        return True

if __name__ == "__main__":
    import binascii
    print(Binary.blocks_size(100))
    assert Binary.blocks_size(100) == 13
    b = Binary.from_string("101110101")
    print(b)
    c = Binary.from_string("101110101")
    d = Binary.from_string("101001101")
    # Same as b but with more bits
    b_ext = Binary.from_string("10111010111")
    assert b == c
    assert b != d
    assert b == b_ext
    print("(%s: %s)" % (b.size, binascii.hexlify(b.blocks)))
    print("Resizing", b, "to 3 bits...")
    b.resize(3)
    print("Result:", b)
    assert b == Binary.from_string("101")

    address = "13ejSKUxLT9yByyr1bsLNseLbx9H9tNj2d"
    _, blocks = libbitcoin.bitcoin_utils.bc_address_to_hash_160(address)
    b = Binary.from_address(address)
    assert b._blocks == blocks
    assert b._size == 160
    c = Binary.from_string("0001110")
    b.resize(7)
    assert b == c
    assert str(b) == "0001110"

