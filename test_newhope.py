from pynewhope import newhope

# Step 1: Alice generates random keys and her public msg to Bob
alicePrivKey, aliceMsg = newhope.keygen()
print("Alice sends to Bob his message:", aliceMsg)

# Step 2: Bob receives the msg from Alice and responds to Alice with a msg
bobSharedKey, bobMsg = newhope.sharedb(aliceMsg)
print("Bob's message:", bobMsg)
print("Bob's key:", bobSharedKey)

# Step 3: Alice receives the msg from Bob and generates her shared secret
aliceSharedKey = newhope.shareda(bobMsg, alicePrivKey)
print("Alice's key:", aliceSharedKey)

if aliceSharedKey == bobSharedKey:
    print("Successful key exchange! Keys match.")
else:
    print("Error! Keys do not match.")
