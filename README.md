# PyNewHope

PyNewHope is an **experimental** (an unstable) Python implementation of the **NewHope quantum-safe key-exchange** cryptographic scheme proposed by Alkim, Ducas, Pöppelmann, and Schwabe: https://eprint.iacr.org/2015/1092

NewHope uses lattice-based cryptography, more precisely Ring-LWE (ring-learning-with-errors), which is designed to be quantum-resistant.

This Python implementation is based on, and duplicates much of the functionality of, the reference C implementation available in the `liboqs` repository: https://github.com/open-quantum-safe/liboqs/tree/master/src/kex_rlwe_newhope

This implementation is designed to be used natively in Python applications, without the need for wrappers or other means of incorporating the C implementation into production software. A testing harness is available in `test_newhope.py`, and documentation is provided as code comments. The code should be readable and usable.

**For educational purposes only!** Avoid using this code in real-world projects.

This work was submitted as a master's capstone advanced lab to the computer science department at the Courant Institute of Mathematical Sciences at New York University. It should be considered open source, free to use and modify.

Python 3.6 must be installed for this implementation to work, as it relies on `hashlib.shake_128()`, which is only available in version 3.6 and later.

Instructions for installing from PyPI:
--------------------------------------

This library is available in the PyPI repository (packaged by [Svetlin Nakov](https://github.com/nakov)). To install it, use this:

```
pip install pynewhope
```

Sample usage:
-------------

```py
from pynewhope import newhope

# Step 1: Alice generates random keys and her public msg to Bob
alicePrivKey, aliceMsg = newhope.keygen()
print("Alice sends to Bob her public message:", aliceMsg)

# Step 2: Bob receives the msg from Alice and responds to Alice with a msg
bobSharedKey, bobMsg = newhope.sharedB(aliceMsg)
print("\nBob sends to Alice his public message:", bobMsg)
print("\nBob's shared key:", bobSharedKey)

# Step 3: Alice receives the msg from Bob and generates her shared secret
aliceSharedKey = newhope.sharedA(bobMsg, alicePrivKey)
print("\nAlice's shared key:", aliceSharedKey)

if aliceSharedKey == bobSharedKey:
    print("\nSuccessful key exchange! Keys match.")
else:
    print("\nError! Keys do not match.")
```

Sample output:
--------------

```
Alice sends to Bob her public message: ([1328, 8117, 8737, 6265, 8128, 12924, 3390, 12041, 4568, 7602, 2673, 7517, 2410, 1291, 2125, 2789, 11486, 1568, 12043, 9209, 6681, 9858, 5936, ..., 1021, 2113, 8424, 8501, 3442, 4238, 9503, 4625, 11250, 11609], b"\r\x8c\x89\xd0\xa0\x06gc8\xd2%:\xb0Z'\x9c\x8cs\xf9\xf8\xe7\x9f\x84T\xb73\x85w\xcc\xe5\xb5\xe1")

Bob sends to Alice his public message: ([2, 0, 3, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 0, 1, 1, 1, 3, 0, 2, 0, 2, 2, 1, 1, 3, 2, 3, 3, 3, 3, 1, 3, 1, 0, 1, 2, 0, 1, 1, 3, 3, 2, 1, 1, 2, 0, 3, 3, 2, 1, 1, 1, 0, 2, 3, 1, ..., 3, 3, 2, 2, 0, 1], [9328, 8906, 2517, 6830, 4517, 2142, 8296, 938, 3333, 10585, 12196, 11496, 3726, 12462, 10271, 4871, 4499, 2899, 11284, 8994, 4732, 7381, 2950, 8675, 4349, 2534, 2161, ..., 6591, 6369, 8664, 5182, 10856, 4314, 7919, 3651, 2352, 4103, 6035, 3990])

Bob's shared key: [92, 122, 75, 33, 239, 164, 84, 241, 245, 204, 106, 197, 142, 230, 28, 189, 54, 112, 190, 124, 176, 66, 129, 69, 108, 66, 110, 42, 115, 70, 17, 107]

Alice's shared key: [92, 122, 75, 33, 239, 164, 84, 241, 245, 204, 106, 197, 142, 230, 28, 189, 54, 112, 190, 124, 176, 66, 129, 69, 108, 66, 110, 42, 115, 70, 17, 107]

Successful key exchange! Keys match.
```

As it is visible from the output, the Alice's public message consists of a sequence of polynomial coefficients + a random seed (sequence of bytes). Bob's public message consists of two sequences of polynomial coefficients. The obtained from Alice and Bob shared key consists also of a sequence of polynomial coefficients.

Instructions for cloning and testing PyNewHope on Mac/Linux:
------------------------------------------------------------

Once you have Python 3.6 and Git installed, open a terminal and enter the following commands:
```
git clone https://github.com/nakov/PyNewHope

cd PyNewHope

python3.6 test_newhope.py
```

Instructions for cloning and testing PyNewHope on Windows:
----------------------------------------------------------

First make sure you have Python 3.6 installed.

Download PyNewHope as a zip file from https://github.com/nakov/PyNewHope using the "Clone or download" button.

Unzip PyNewHope into a directory in your Python PATH.

Open a Python shell and enter the following commands:
```
import test_newhope

test_newhope
```

Contributors:
-------------
 - Originally created by Scott Wyman Neagle (2017) - https://github.com/scottwn/
 - Based on the Open Quantum Safe project (2016) - https://github.com/open-quantum-safe/liboqs/
 - Modified by Svetlin Nakov and uploaded to PyPI (2018) - https://github.com/nakov
