import secrets
import hashlib
from cashaddress.convert import Address
from hdwallet import HDWallet
from getpass import getpass

from lotus import lotus_address


def main():
    user_entropy = getpass('Button-smash the keyboard for some random entropy: ')
    if len(user_entropy) < 32:
        print('ERROR: Enter at least 32 characters!')
        return
    user_entropy = hashlib.sha256(user_entropy.encode()).digest()
    random_entropy = secrets.token_bytes(32)
    entropy = hashlib.sha256(user_entropy + random_entropy).digest()
    entropy = entropy[:16]
    print('Generated entropy.')
    passphrase = getpass('Enter a passphrase (or leave empty if none): ')
    passphrase = passphrase or None
    lotus_wallet = HDWallet(symbol='BCH')
    lotus_wallet.from_entropy(entropy.hex(), language='english', passphrase=passphrase)
    print('SEED PHRASE (keep this secret):')
    print(' '*4, lotus_wallet.mnemonic())
    wallet = lotus_wallet.from_path("m/44'/10605'/0'/0/0")
    h = hashlib.new('ripemd')
    h.update(hashlib.sha256(bytes.fromhex(wallet.public_key())).digest())
    pkh = h.digest()
    address = Address('P2PKH', list(pkh), 'bitcoincash')
    print('ADDRESS (share this with someone who wants to send you money):')
    print(' '*4, address.cash_address())
    print(' '*4, lotus_address('lotus', pkh))


if __name__ == '__main__':
    main()
