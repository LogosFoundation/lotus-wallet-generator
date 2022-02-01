from hashlib import sha256

import base58


def lotus_address(prefix: str, pkh: bytes) -> str:
    script = b'\x76\xa9\x14' + pkh + b'\x88\xac'
    payload = b'\0' + script
    checksum_msg = prefix.encode() + b'_' + payload
    checksum = sha256(checksum_msg).digest()[:4]
    payload_b58 = base58.b58encode(payload + checksum).decode()
    return prefix + '_' + payload_b58


if __name__ == '__main__':
    print(lotus_address('lotus', bytes(20)))
