# Blockchain Course Notes

## Understanding SHA256 Hash

A fingerprint is an identifier of a person. SHA256 Hash is similar to this for the identity of digital documents. 
"SHA" stands for "Secure Hash Algorithm" and 256 is the number of bits in memory. It's a hexadecimal hash. 
64 characters. 

[Online Tool for SHA256](https://emn178.github.io/online-tools/sha256.html)

5 requirements for Hash algorithms:

* One-way -> cannot restore document from hash
* Deterministic -> same document will generate exact same result
* Fast computation
* Avalanche effect -> any change (no matter how tiny) will totally change the hash
* Must withstand collisions -> can't recreate / forge

Chapter 1: [Cryptocgraphy in Context](https://www.staff.science.uu.nl/~tel00101/liter/Books/CrypCont.pdf)

## The Immutable Ledger

X = blockchain

Each blockchain is connected. 

X <---> X <---> X <---> X <---> X

If one blockchain is changed, the cryptographic link between the blockchains will no longer work. In order to 
tamper with the blockchain, it's very difficult to change a single block. 

Use Cases

* Property Transactions
* Diamonds

[The Blockchain Economy: A Beginner's Guide to Institutional Crypteconomics](https://medium.com/cryptoeconomics-australia/the-blockchain-economy-a-beginners-guide-to-institutional-cryptoeconomics-64bf2f2beec4)

## Distributed P2P Network


