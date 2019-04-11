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

## Distributed Peer-2-Peer Networks

Blockchains copied across multiple computers. More difficult to attack since you'd have to alter the chain over more than 50% of the computers. 

[The Meaning of Decentralization](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274)

## Mining

Block normally stores several transactions. 

```
Block #3
-----------
Nonce:
-----------
Data
Kirill -> Hadeline 500 hadcoins
Kirill -> Ebay 100 hadcoins
Hadelin -> Joe 70 hadcoins
-----------
Prev Hash: 000DF......
Hash: 8285C31.......
```

Nonce ("number used only once"). Changing the nonce changes the hash. 

## Byzantine Fault Tolerance

[Understanding Byzantine Fault Tolerance](https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419)

## Consensus Protocols

