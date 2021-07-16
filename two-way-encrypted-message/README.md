# Two-Way-Encrypted-Messaging-using-DES-and-Diffie-Hellman

In this project, using a client-server architecture to show the mechanism, I have implemented encryption-decryption procedure using DES and Diffie-Hellman Key Exchange. The steps regarding the algorithm are already in the files as comments at every step. The algorithms are:

  1. DES (Data Encryption Standard): It is a symmetric key algorithm which one can crack with brute force in 2^56 iterations.
  2. Diffie-Hellman Key Exchange: It is the key exchange algorithm in order for the interacting systems to derive to the same shared key that will be used by DES for the encryption-decryption purposes.

The basic steps involved would be:
  1. The server would be listening for any incoming requests to connect to a client
  2. The client will send a request for connection and after the TCP 3-Way Handshake, the client and server can start talking to each other one after the other.
  3. The global parameters are selected by the server and the client is notified of them
  4. The public-private key pair are generated and public keys are exchanged to get the session key to be used for DES
  5. The message the sender wants to send is encrypted and encoded and sent to the receiver.
  6. The receiver would decode and decrypt the message and print the message on the terminal
