from pynewhope import newhope

# Step 1: Alice generates random keys and her public msg to Bob
aliceMsg = newhope.keygen()
print("Alice sends to Bob his message:", aliceMsg)

# Step 2: Bob receives the msg from Alice and responds to Alice with a msg
bobMsg = newhope.sharedb(aliceMsg)
print("Bob's message:", bobMsg)
print("Bob's key:", str(newhope.b_key))

# Step 3: Bob receives the msg from Alice and responds to Alice with a msg
newhope.shareda(bobMsg)
print("Alice's key:", str(newhope.a_key))

if newhope.a_key == newhope.b_key:
    print("Successful handshake! Keys match.")
else:
    print("Error! Keys do not match.")
