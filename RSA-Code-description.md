# Code Description 
The code begins by importing different libraries which will then be used for the code to work 
accordingly.

We will import the following libraries:

- import tkinter as tk
- from tkinter import *
- from tkinter import filedialog, messagebox
- import rsa
- import customtkinter
  
The code will be populated by mostly functions where we will set up what each of our buttons 
on the GUI will do when pressed. We will create a function for the generation of the private and 
public key followed by 2 additional function which will be used to load the private and public 
key. These 2 last functions will return the public and private key and save it as global value 
which is allocated just after the import of our libraries. This will allow us to use the public and 
private key loaded when we are running the application and use them as long as we use the 
application or decide to change them with different keys. Once these keys are loaded different 
function will use these keys as reference to make their operation work accordingly. 

We have 2 additional functions afterwards which will display the content of our public and 
private key. 

The other functions will be encrypted and decrypt the text of a file, or the text inserted inside 
the textbox. This will be defined as decrypt/encrypt file and decrypt/encrypt text. This function 
will take the input from the text box, or the file chosen and use the public key loaded in the 
application to encrypt the file. Once encrypted the user can choose to overwrite the same text 
file or have a second empty text file to write the content of the encryption. Similar process will 
be done with the decryption however in this instance we will use the private key to decrypt the 
message. 

The code has to functionality also the sign and verify the text for integrity check. The sign 
button will be assigned on function which will take the content of the plain text from a file or 
from the textbox and use the user private key to sign the message. The system will prompt the 
user to save the signature somewhere on the computer. On the verification part the user will be 
prompt to select a file and then will be prompt to also select the signature file. The application 
will change the way the verification will work automatically whether the verification will be 
from a file or from the text written on the textbox. This condition will check whether the 
textbox is populated by any character if yes, the function will ask only for the signature file 
otherwise if not character is in the textbox this will mean that the user want to verify a text file. 

Additional functions found in the code is for the deleting the content inside the textbox with 
just one click and the other is a dropdown menu where the user can choose between light or 
dark theme. Furthermore, on the code after all the functions are implemented, we will create 
the frame for our GUI window and then add all the buttons along with the position of each 
button. We will call all these functions on the buttons we create. Every button will have a 
specific call name referring to the library imported to apply the custom design for the tinker 
interface. 
