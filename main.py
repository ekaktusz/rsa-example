import rsa


def generate_keys():
    public, private = rsa.generate_keys()
    print('Public key: \n e = \n' + str(public[0]) + '\n n = \n' + str(public[1]))
    print('Private key: \n d = \n' + str(private[0]) + '\n n = \n' + str(private[1]))


def encrypt_main():
    print('Give me your public key:')
    e = int(input('e = \n'))
    n = int(input('n = \n'))
    public = (e, n)
    text = input('Type the text you want to encrypt: \n')
    encrypted_text = rsa.encrypt(public, text)
    print('The encrypted text: \n' + str(encrypted_text))


def decrypt_main():
    print('Give me your private key:')
    d = int(input('d = \n'))
    n = int(input('n = \n'))
    private = (d, n)
    encrypted = input('Type the encrypted text: \n')
    decrypted_text = rsa.decrypt(private, int(encrypted))
    print('The decrypted text: \n' + decrypted_text)


def rsa_main():
    print('\nChoose from the following options:: \n (1) Key genereation \n (2) Encryption \n (3) Decryption \n (Anything else) Quit')
    choice = input()
    if choice == '1':
        generate_keys()
        rsa_main()
    elif choice == '2':
        encrypt_main()
        rsa_main()
    elif choice == '3':
        decrypt_main()
        rsa_main()
    else:
        print('Goodbye!')


print('Hello! I am a simple program demonstrating RSA encryption technique!')
rsa_main()
