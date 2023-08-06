import sys
from jkspy.modules import crypto
from Crypto.PublicKey import RSA
from jkspy.helpers import readFile, writeFile
""" Currently, the output to the console is done by the
    print() function, and not by the return statement """

def test():
    print(">>> Running jkspy TEST")
    for i in range(0, 10):
        print(i)
    print(">>> TEST Completed")
    
def checksum(filepath, *options):
    try:
        print(crypto.get_checksum(filepath, *options))
    except TypeError:
        print("Please provide a filepath.")
        print("  (Example)  >> jkspy checksum test.txt")

def keygen(filepath, kind=16, format='PEM'):
    if int(kind) > 0:
        keyfile = open(filepath, 'wb')
        keyfile.write(crypto.make_key(int(kind)))
        keyfile.close()
        print("New random key created at "+filepath)
    elif kind == 'pair':
        keypair = crypto.make_keypair()
        crypto.save_keypair(keypair, filepath, format)
        print("New keypair created as "+filepath+'.private and '+filepath+'.public')
    
def encrypt(pubkeypath, filepath):
    pubkey = crypto.open_keypair(pubkeypath)
    content = readFile(filepath)
    
    crypto = crypto.encrypt(pubkey, content)
    
    writeFile(filepath+'.secret', crypto, True)
    
def decrypt(prvkeypath, filepath):
    try:
        prvkey = crypto.open_keypair(prvkeypath)
        content = readFile(filepath, True)
        
        plain = crypto.decrypt(prvkey, content).decode()
        
        writeFile(filepath+'.plain', plain)
    except ValueError:
        print("Could not decrypt ["+filepath+"]")
        
def sencrypt(passphrase, filepath):
    plaintext = readFile(filepath)
    ciphertext = crypto.sencrypt(passphrase, plaintext)
    print( ciphertext )
    writeFile(filepath+'.locked', ciphertext, bytestring=True)

def sdecrypt(passphrase, filepath):
    ciphertext = readFile(filepath, bytestring=True)
    plaintext = crypto.sdecrypt(passphrase, ciphertext)
    print( plaintext )
    writeFile(filepath+'.unlocked', plaintext)