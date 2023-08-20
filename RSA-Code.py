import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import rsa
import customtkinter

global private_key
global public_key
global signature


def generatekeys():
    (publicKey, privateKey) = rsa.newkeys(1024)

    pubkey = filedialog.asksaveasfilename(defaultextension=".PEM",
                                          title="Save Public Key")

    privkey = filedialog.asksaveasfilename(defaultextension=".PEM",
                                           title="Save Private Key")

    with open(pubkey, 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(privkey, 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


def loadpubkey():
    global public_key
    try:
        # messagebox.showinfo("", "Choose a public Key")
        pubkey = filedialog.askopenfilename(title='Select the Public Key')
        with open(pubkey, 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        return public_key
    except:
        messagebox.showinfo("", "You did not selected a Public key")


def view_pub_key():
    messagebox.showinfo("", public_key)


def loadprivkey():
    global private_key
    try:
        # messagebox.showinfo("", "Choose a private Key")
        privkey = filedialog.askopenfilename(title='Select the Private Key')
        with open(privkey, 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key
    except:
        messagebox.showinfo("", "You did not selected a Private key")


def view_priv_key():
    messagebox.showinfo("", private_key)


def encrypt_content(content, key):
    return rsa.encrypt(content.encode('ascii'), key)


def decrypt_content(content, key):
    return rsa.decrypt(content, key)


def encrypt_file():
    try:
        message = filedialog.askopenfile(mode='r',
                                         title='Select a message to encrypt')
        encrypt_msg = message.read()
        message.close()
    except:
        messagebox.showinfo("", "You did not choose a file!")

    try:
        encrypted_msg = encrypt_content(encrypt_msg, public_key)

    except:
        messagebox.showinfo("", "The message could not be Encrypted!")

    encrypted = filedialog.askopenfile(mode='wb',
                                       title='Save the encrypted message')
    encrypted.write(encrypted_msg)
    encrypted.close()


def decrypt_file():
    try:
        message = filedialog.askopenfile(mode='rb',
                                         title='Select a message to decrypt')
        decrypt_msg = message.read()
        message.close()
    except:
        messagebox.showinfo("", "You did not choose a file!")

    try:
        encrypted_msg = decrypt_content(decrypt_msg, private_key)
    except:
        messagebox.showinfo("", "The message could not be Decrypted!")

    encrypted = filedialog.askopenfile(mode='wb',
                                       title='Save the decrypted message')
    encrypted.write(encrypted_msg)
    encrypted.close()



def encrypt_text():
    text = text_entered.get("1.0", 'end-1c')

    text_entered.delete("1.0", 'end-1c')

    # Encrypt Content
    enc_content = encrypt_content(text, public_key)
    text_entered.insert(tk.END, enc_content)
    with open('encryption.txt', 'wb') as f:
        f.write(enc_content)


def decrypt_text():
    text = open('encryption.txt', 'rb')
    text_content = text.read()
    text_entered.delete("1.0", 'end-1c')

    # Decrypt the content
    dec_content = decrypt_content(text_content, private_key)
    text_entered.insert(tk.END, dec_content)
    decrypted = open("encryption.txt", 'wb')
    decrypted.write(dec_content)
    decrypted.close()
    with open("encryption.txt", 'r+') as f:
        f.truncate(0)


def sign_text():
    text = text_entered.get("1.0", 'end-1c')
    text_converted = bytes(text, 'utf-8')
    print(len(text))
    if len(text) > 0:
        try:
            signature = rsa.sign(text_converted, private_key, 'SHA-1')
            signed = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  title="Save Signature Text")
            with open(signed, 'wb') as f:
                f.write(signature)
        except:
            messagebox.showinfo("",
                                "The message could not be Signed Check Parameter")
    else:

        file = filedialog.askopenfile(mode='rb', title='Select the File to sign')
        file_read = file.read()
        file.close()
        try:
            signature = rsa.sign(file_read, private_key, 'SHA-1')
            signed = filedialog.asksaveasfilename(defaultextension=".txt",
                                                  title="Save Signature")
            with open(signed, 'wb') as f:
                f.write(signature)
        except:
            messagebox.showinfo("",
                                "The message could not be Signed Check Parameter")


def verify_text():
    text = text_entered.get("1.0", 'end-1c')
    text_converted = bytes(text, 'utf-8')

    if len(text) > 0:
        signature = filedialog.askopenfile(mode='rb',
                                           title='Select signature File text')
        signature_file = signature.read()
        signature.close()
        try:
            verify = rsa.verify(text_converted, signature_file,
                                public_key) == 'SHA-1'
            if verify:
                messagebox.showinfo("", "The message is verified")
        except:
            messagebox.showinfo("", "The message is not verified!!")
    else:
        file = filedialog.askopenfile(mode='rb', title='Select the File to verify')
        file_read = file.read()
        file.close()
        signature = filedialog.askopenfile(mode='rb',
                                           title='Select signature File')
        signature_file = signature.read()
        signature.close()
        try:
            verify = rsa.verify(file_read, signature_file, public_key) == 'SHA-1'
            if verify:
                messagebox.showinfo("", "The message is verified")
        except:
            messagebox.showinfo("", "The message is not verified!!")


def delete_text():
    text_entered.delete('1.0', END)


def change_appearance_mode(theme):
    customtkinter.set_appearance_mode(theme)


def change_color_mode(theme):
    customtkinter.set_default_color_theme(theme)


frame = customtkinter.CTk()
frame.title('RSA-Encryption Tool')
frame.geometry("510x400")

text_entered = Text(frame, width=59, height=11)
text_entered.pack(pady=40)
text_entered.place(x=20, y=75)

generate = customtkinter.CTkButton(frame, text="Generate Key", command=generatekeys)
generate.place(x=190, y=25)

loadpub = customtkinter.CTkButton(frame, text="Load Public Key", command=loadpubkey)
loadpub.place(x=20, y=10)

view_pub = customtkinter.CTkButton(frame, text="View", command=view_pub_key)
view_pub.place(x=20, y=42)

view_priv = customtkinter.CTkButton(frame, text="View", command=view_priv_key)
view_priv.place(x=350, y=42)

loadpriv = customtkinter.CTkButton(frame, text="Load Private Key", command=loadprivkey)
loadpriv.place(x=350, y=10)

encrypt_file = customtkinter.CTkButton(frame, text="Encrypt File ", command=encrypt_file)
encrypt_file.place(x=20, y=300)

decrypt_file = customtkinter.CTkButton(frame, text="Decrypt File ", command=decrypt_file)
decrypt_file.place(x=350, y=300)

encrypt_text = customtkinter.CTkButton(frame, text="Encrypt Text", command=encrypt_text)
encrypt_text.place(x=20, y=270)

decrypt_text = customtkinter.CTkButton(frame, text="Decrypt Text", command=decrypt_text)
decrypt_text.place(x=350, y=270)

delete_text = customtkinter.CTkButton(frame, text="Delete", command=delete_text)
delete_text.place(x=185, y=290)

option_menu = customtkinter.CTkComboBox(frame, values=("Dark", "Light"), command=change_appearance_mode)
option_menu.place(x=20, y=335)

sign_text = customtkinter.CTkButton(frame, text="Sign", command=sign_text)
sign_text.place(x=350, y=335)

verify_text = customtkinter.CTkButton(frame, text="Verify", command=verify_text)
verify_text.place(x=185, y=335)

frame.mainloop()
