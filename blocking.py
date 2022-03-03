import tkinter as tk
import time
from tkinter import font
# Creates the needed variables to have website blocked
location = "C:\Windows\System32\drivers\etc\hosts"
id = "127.0.0.1"

def website_blocker(user_website):
    '''
    This will take the users inputted website that they desire to be blocked and using the
    host file, they will write out the website in the file with a few modifications to have
    it blocked on the users computers.
    user_website: A string representing the name of the website the user wants blocked
    '''
    # The information that will be written to the host file to block the website
    website_one = id + " " +  user_website + ".com"
    website_two = id + " " + "www." + user_website + ".com"
    # Adds the website to the end of the file
    host_file = open(location, "a+")
    host_file.write(website_one + '\n')
    host_file.write(website_two + '\n')
    # Closes the file
    host_file.close()
    # Calls the two needed functions
    blocked_websites(user_website)
    line_writter()
    # Clears out the entry box
    entry.delete(0, tk.END)
    # Delays the program slightly
    time.sleep(0.2)


def blocked_websites(website):
    '''
    This will write each blocked website into a text file to keep track of which websites the user
    has blocked.
    website: A string representing the name of the website the user wants blocked
    '''
    # Writes the website in text file file and creates the text file if it is not yet created
    try:
        website_file = open("website_file.txt", "a+")
        website_file.write(website + '\n')
        website_file.close()
    except:
        website_file = open("website_file.txt", "w")
        website_file.write("Blocked Websites: " + '\n')
        website_file.write(website + '\n')
        website_file.close()

def line_writter():
    '''
    This will write each line of website file into the lower label
    '''
    websites = open("website_file.txt", "r")
    # Reads through each line of the file
    label['text'] = ""
    for website in websites:
        label['text'] = label['text'] + website
    websites.close()

def website_unblock():
    '''
    This will remove all the lines on the host file that were blocking the users inputted websites
    as well as removing the websites that were written in the text file.
    '''
    # rewrites the text file to not be holding any website names in it
    websites = open("website_file.txt", "w")
    websites.write("Blocked Websites:\n")
    websites.close()
    # Reads each line of the host file
    host_file = open(location, 'r')
    file_lines = host_file.readlines()
    host_file.close()
    host_file = open(location, 'w')
    # Determines which lines of the file are used to block the websites and which are not
    for line in file_lines:
        if line[0] == "#":
            host_file.write(line)
    host_file.close()
    line_writter()


# Sets the height, width and the root
HEIGHT, WIDTH = 500, 600
root = tk.Tk()

# Creates the canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Creates the background color
background = tk.Label(root, bg='#ECF9EB')
background.place(relwidth=1, relheight=1)

# Creates the text asking user to type in a website
text_question = tk.Label(root, bg='#ECF9EB', text='Enter a website you want to be blocked', font=('Roboto Condensed', 13))
text_question.place(relx=-.018, relwidth=.7, relheight=.1)

# Creates the frame where the user inputs their desired website to block
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=.1, rely=.1, relwidth=.8, relheight=.13)

# Creates the entry box
entry = tk.Entry(frame, font=('Roboto Condensed', 17))
entry.place(relwidth =.7, relheight=1)

# Creates the button to block an inputted website
button = tk.Button(frame, text="Block Website", font=('Roboto Condensed', 11), command=lambda: website_blocker(entry.get()))
button.place(relx=.72, relwidth = .28, relheight = 1)

# Creates the lower frame to display blocked websites
lower_frame = tk.Frame(root, bg = "#80c1ff", bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.8, relheight=.73, anchor='n')

# Creates the label to display the blocked websites
label = tk.Label(lower_frame, font=('Roboto Condensed', 22), anchor = 'nw', justify='left', bd=4)
label.place(relwidth=1,relheight=1)

# Creates the website unblock button
remove_button = tk.Button(lower_frame, text="Unblock All Websites", bg='#80c1ff', font=('Roboto Condensed', 11),command=lambda: website_unblock())
remove_button.place(relx=.62, rely=.02, relwidth=.35, relheight=0.2)

line_writter()

root.mainloop()
