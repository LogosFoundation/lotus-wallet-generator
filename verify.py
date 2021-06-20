import hashlib
from cashaddress.convert import Address
from hdwallet import HDWallet
from getpass import getpass


def main():
    mnemonic = getpass('Enter the seed mnemonic phrase: ')
    passphrase = getpass('Enter the associated passphrase: ')
    passphrase = passphrase or None
    lotus_wallet = HDWallet(symbol='BCH')
    lotus_wallet.from_mnemonic(mnemonic, language='english', passphrase=passphrase)
    wallet = lotus_wallet.from_path("m/44'/10605'/0'/0/0")
    h = hashlib.new('ripemd')
    h.update(hashlib.sha256(bytes.fromhex(wallet.public_key())).digest())
    pkh = h.digest()
    address = Address('P2PKH', list(pkh), 'bitcoincash')
    print('DERIVED PUBKEY:')
    print(' '*4, wallet.public_key())
    print('DERIVED ADDRESS:')
    print(' '*4, address.cash_address())


if __name__ == '__main__':
    main()
