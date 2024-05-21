import os

def encode_txt_data(data):

    file_path = "SecureCommunicationProject\my_app\Sample_cover_files\cover_text.txt"
    absolute_file_path = os.path.abspath(file_path)
    print(f"Checking file at: '{absolute_file_path}'")

    # Check if the file exists, and create it if it doesn't
    if not os.path.exists(file_path):
        print(f"File not found at '{absolute_file_path}'. Creating file.")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as cover_file:
            cover_file.write("This is a sample cover text file used for steganography.")

    print(f"File found or created: '{absolute_file_path}'")

    try:
        # Open the cover text file in read mode
        with open("SecureCommunicationProject\my_app\Sample_cover_files\cover_text.txt", "r") as cover_file:
            cover_text = cover_file.read()

        # Check if secret data is empty
        if not data:
            raise ValueError("Secret data cannot be empty.")

        # *Placeholder for your actual encoding logic* (avoiding sensitive details)
        # This example replaces every third character in the cover text with the secret data:
        encoded_cover_text = ""
        j = 0  # Index for secret data
        for i, char in enumerate(cover_text):
            if i % 3 == 0:  # Replace every third character
                if j < len(data):
                    encoded_cover_text += data[j]
                    j += 1
                else:
                    encoded_cover_text += char
            else:
                encoded_cover_text += char

        # Check if encoded text fits within cover text size (optional)
        if len(encoded_cover_text) > len(cover_text):
            raise ValueError("Secret data is too large to be encoded in the cover text.")

        # *Placeholder for saving the encoded cover text (optional):*
        # You might want to save the encoded text to a different file.
        # with open("encoded_cover_text.txt", "w") as encoded_file:
        #     encoded_file.write(encoded_cover_text)

        print("Secret data encoded successfully (using a simple example technique)!")
        print("Encoded Text:", encoded_cover_text)

    except FileNotFoundError:
        print("Error: Cover text file not found. Please create 'cover_text.txt' in the Sample_cover_files directory.")

def decode_txt_data():
    """
    Decode the text hidden in the cover text file.

    Returns:
        str: The decoded text.
    """
    try:
        # Read the cover text file
        with open("SecureCommunicationProject\my_app\Sample_cover_files/cover_text.txt", "r") as cover_file:
            cover_text = cover_file.read()

        # *Placeholder for your actual decoding logic* (avoiding sensitive details)
        # This example assumes every third character contains encoded data:
        decoded_text = ""
        for i, char in enumerate(cover_text):
            if i % 3 == 0:  # Select every third character
                decoded_text += char
        # Print the decoded text in the terminal console
        print("Decoded Text:", decoded_text)
        return decoded_text

    except FileNotFoundError:
        return "Error: Cover text file not found."