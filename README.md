# lotus-wallet-generator
Generates a seed phrase based on random keystrokes and CPU provided entropy, and derives the address from the Lotus derivation path 10605.

## Usage

1. Make sure you have a recent Python 3 version installed (works on Python 3.9).
2. Install these packages: `pip install hdwallet cashaddress`.
3. Clone repository `git clone https://github.com/LogosFoundation/lotus-wallet-generator`, `cd lotus-wallet-generator`.
4. Run `python main.py`
5. Type at least 32 random characters from the keyboard, then press Enter.
6. Type a passphrase, or leave empty if no passphrase required, then press Enter.
7. Write down seed phrase on a piece of paper and keep it secure.
8. Share the address with whomever is supposed to send you money.
