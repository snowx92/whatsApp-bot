import pywhatkit as kit
import pandas as pd
from tkinter import *
from tkinter import filedialog

def send_whatsapp_message():
    # Create a GUI window
    root = Tk()
    root.title("Send WhatsApp Message")
    root.geometry("400x200")

    # Create a label for the file path
    file_path_label = Label(root, text="CSV File Path:")
    file_path_label.pack()

    # Create an entry for the file path
    file_path_entry = Entry(root)
    file_path_entry.pack()

    # Create a label for the message
    message_label = Label(root, text="Message:")
    message_label.pack()

    # Create an entry for the message
    message_entry = Entry(root)
    message_entry.pack()

    def select_file():
        file_path = filedialog.askopenfilename()
        file_path_entry.delete(0, END)
        file_path_entry.insert(0, file_path)

    def send_message():
        file_path = file_path_entry.get()
        message = message_entry.get()

        df = pd.read_csv(file_path, on_bad_lines='skip')

        # Add country code +20 to each number
        df['Number'] = '+20' + df['Number'].astype(str)

        # Send WhatsApp messag
        #
        #
        # e to all numbers in the sheet
        for index, row in df.iterrows():
            try:

                kit.sendwhatmsg_instantly(row['Number'], message , 25 , True , 5)
                print(f"Message sent successfully to {row['Number']}")
                log_label = Label(root, text=f"Message sent successfully to {row['Number']}")
                log_label.pack()
            except:
                print(f"Failed to send message to {row['Number']}")
                log_label = Label(root, text=f"Failed to send message to {row['Number']}")
                log_label.pack()

    # Create a button to select the CSV file
    select_file_button = Button(root, text="Select CSV File", command=select_file)
    select_file_button.pack()

    # Create a button to send the WhatsApp message
    send_message_button = Button(root, text="Send Message", command=send_message)
    send_message_button.pack()

    root.mainloop()
send_whatsapp_message()