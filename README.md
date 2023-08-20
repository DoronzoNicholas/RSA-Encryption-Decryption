# RSA-Encryption-Description
For RSA project I created a python code which implements the RSA encryption and decryption with the additional possibility to sign and verify the message. This implementation was developed around a GUI interface so that it can be used also without a clear knowledge of coding.


# Application Overview
The interface of the GUI was made possible with “TKinter” which is a built-in option in python for the creation of GUI. Furthermore, for the esthetic of the GUI different library was used. For this GUI I have used “CustomTkinter” library which was available via GitHub. 

GitHub - https://github.com/TomSchimansky/CustomTkinter

Some of the functions implemented are the possibility of loading the public key and the private key only once as long as the window is kept opened or changed by the user. This allows multiples file and messages to be encrypted and/or decrypted easily without loading key all the time. For these 2 keys is possible to see also the content after it is loaded.  
The python code allows the user to have 2 options one to type or paste the message straight inside the text box and the other to select a file to then encrypt and/or decrypt the message. There are 2 buttons for each option the “encrypt/decrypt” are for the file and the “encrypt/decrypt file” is for the files.  
2 more buttons are for the text of file to be signed and/or verified texts or files.  
The last button is a “delete” one just for the text box in case the user wants to quickly delete the text. 
Additional appearance available is to change them of the whole interface from dark to light from the drop down on the left corner of the window. 

# Interface and functionality
In this following section we will have shown in pictures how the application looks once it is run along with all the functionality available. Figure 1 shows the GUI interface of the application once opened. 

 ![image](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/0e7a79ce-98a8-4690-a214-4f6e6dfa71f9)

(Figure 1 – GUI interface)


In order to begin to operate with the encryption and decryption we will first generate our public and private keys as it shows in figure 2&3.


![2](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/27e40cde-1786-4823-9d63-6b2a2f4a100f)

(Figure 2 – Save the public Key)

      

  ![3 pivate key](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/23866d39-18c0-48fc-9095-aa707986286f)
                    
(Figure 3 - Save the private key)

Now that our keys are saved, we can now load them on the application. Once these keys are loaded any buttons which will require the public or private key will use the key loaded at the beginning without asking once again. Figure 4


![4 Load keys](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/d8fce053-e5c4-4ff7-8981-dcdbac0ad38e)

(Figure 4 – Select the key)

We have underneath the load key a view button in the instances we would like to view the 
content of our key. Figure 5&6

![5 View Public_Key](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/61e04935-c591-4ad2-9b6e-92250f54a888)

(Figure 5 – View Public Key)


![6 View Private Key](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/86fc29a4-5cd7-41c4-9a04-dca80bafe27c)


(Figure 6 – View Private Key)

Now we can begin our encryption. We will create a TXT file and write a text of our choice inside. Figure 7


![7 Create a text File](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/60fe3d4f-3974-4916-b945-bfa816fa3ee2)

(Figure 7 – Create a TXT file)

Now we click on the “Encrypt File” button and select the file we want to encrypt. Once we click the encrypt button, we have to select a TXT file were to write the content. Figure 8

![8 Click encrypt file](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/fa81eb86-9610-48fc-92a6-724f9b57174a)

(Figure 8 – Save the encrypted text into a File)

This encrypted content will look as it is shown in figure 9.

![9 File encrypted](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/6010de43-51e3-416e-81d2-8ffe03089449)

(Figure 9 – Encrypted file content)

For the decryption we will do the opposite. We will select the file with the encrypted content. Figure 10


![10 decrypting a file](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/7dc5bab0-a052-4052-8c4f-2ae3fa2c99d9)

(Figure 10 – Select the file containing the encrypted text)

We will be prompt to select the encrypted file. The decrypted file will be saved into another empty “.txt” file created named as “Decripted_File”.  The content of the decrypted file is shown in figure 11.


![11 file decrypted](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/8f3b7315-e397-4333-89fd-c2aca248fdab)

(Figure 11 – Showing the content of the encrypted and decrypted file)


In order to sign a file, we will click on the sign button, and we will be prompt to select a file to sign. Figure 12

![12 sign a file](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/661ac53e-66fe-497a-bee6-5120df4f4c3a)

(Figure 12 – Selcet a file to sign)

After we select the file, we will be prompt to save the signature for that specific file. We will save on the desktop the signature of the file. Figure 13


![13 save signature](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/6311544b-261c-4974-a47c-c70ef1b8ff98)

(Figure 13 – Save the signature of the file)

We can now open the signature file and look at the content. Figure 14

![14 view signature](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/623f0030-4057-43e1-abd2-83f4ca3dd443)

(Figure 14 – View the signature of the file)

If we want to verify the file, we can click on the verify button and we will be prompt to select a file that we want to verify. Figure 15 

![15 Select file to verify](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/2bd91c61-61ef-4205-9bb3-432f056b77bd)

(Figure 15 – Select a file to verify)

Straight after we select the file to verify, we will be prompt to select out signature file.
Figure 16

![16 Selet file signature](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/c68b2bd1-e9e1-4d8f-803e-adcfb058d7e5)

(Figure 16 – Select the signature file)


If the file content was not modified from the time we have last signed the file then we should have pop up window saying the message is verified. In this instance we will assume that the content of the file was not modified. Figure 17

![17 File verified](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/164733b1-19d3-4f39-bdde-18c611c29a53)

(Figure 17 – File has been verified)


By changing the content of the file by a single minor modification we can see we will be prompt with a pop-up window informing us that the message is not verified. In the following picture we have changed from the text content only the exclamation. Figure 18

![18 File verification Denied](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/b403754d-6adc-4d65-9fba-d0786d441a8d)

(Figure 18 – File has not been verified)

In the instances we want to just copy and paste a text for the encryption of the description we can use the same concept . Once we load our public and private key, we can write our text on the textbox and then click on the “Encrypt Text” button. This will encrypt the text content inside the textbox and show us straight away the encrypted text. Figure 19&20


![19 text encryption](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/7ec9ffef-240d-47f7-a8cd-b0b22eec573c)

(Figure 19 – Plain text)                                                     


![20 text encrypted](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/572de6dc-bfaa-414c-bbf6-012c0326545b)

(Figure 20 – ciphertext)

We can verify and the sign the text content in the same way shown for the file signature and verification. 


Furthermore, we can change the look of our application by simply chose one of the options inside our dropdown menu. Figure 21 

(Figure 21 – GUI in light mode)


![21 light mode](https://github.com/DoronzoNicholas/RSA-Encryption-Description/assets/123806307/9db97dbf-7c3b-422b-b1e9-d46731e5ac5d)

(Figure 21 – GUI in light mode)


























































