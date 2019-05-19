#Name : HARI HARA KUMAR NAKSHATRALA
#ID : 1001102740

# Importing the libraries that are used
import socket
from threading import Thread
from tkinter import *
import time
import threading

#Creating the global variables
global count  #This variable is used to count the clients connected
global button #This is used to create the pull button
global client_list  # This has the list of all the connected clients
global operations  #All the operations sent by the clients are saved in this variable
global local_value  #The value of the local variable from all the operations will be saved in this
host = ''
port = 80
post = "POST /"
http = "HTTP/1.1 \n"
host_name = "Host:" + str(host) +"\n"
user_agent = "User-Agent: Python/3.6 + \n"
content_type = "text/html \n"
operations = '1'
count = 0
local_value = 0

#creating the lock to lock the shared memory so that only on client uses
lock = threading.Lock()

#Creating the socket
skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host, port))

#making the server waiting for the clients
skt.listen(5)

#Creating the Tkinter GUI window
display = Tk()
display.title("Server")
display.geometry("500x500")
text = Text(display, height=15, width=60)

#printing that the server is waiting for clients
text.insert(INSERT, "Waiting for connections")

def receive(c): # This method will be called recursively taking the client connection as the argument it will ask all the client to send the operations
    global operations
    try:
        c.send(bytes("pull", 'utf-8'))
        temp = c.recv(1024).decode('utf-8')

        #locking the operations variable so that the sequence is preserved
        lock.acquire()
        operations += temp
        lock.release()
    except:
        print("This client is closed")

#This method will be called when the pull button is pressed
def pull():
    global button
    global client_list
    global operations
    global local_value
    for i in client_list:
        th =Thread(target=receive, args=(i, ))
        th.start()
    time.sleep(4)
    print("operations final is:")
    print(operations)
    text.insert(INSERT, "Operations received are :" + operations)
    local_value = eval(operations)
    text.insert(INSERT, "The updated local value is: " + str(eval(operations)))
    for i in client_list:
        try:
            i.send(str(local_value).encode('utf-8'))
        except:
            print("This client is closed")
    operations = str(local_value)

pull_button = Button(display, text="pull", command=pull)

#The method which is used to run multi threaded clients. This will be the targer method for each client thread
def client_thread(client, c_ip, c_skt):
    try:
        global t
        global button
        get_username_str = "GET /Username HTTP/1.1 \n Host: 127.0.0.1 " + "\n UserAgent: Python/3.6"
        print(get_username_str)

        # requesting the client to send its username
        client.send(bytes(get_username_str, 'utf-8'))

        # receiving the response from the client
        username_header_bytes = client.recv(1024)
        username_header = username_header_bytes.decode('utf-8')
        print(username_header)

        # receiving the username from the client
        username_bytes = client.recv(1024)
        username = username_bytes.decode('utf-8')
        print(username)

        # Displaying that the server is connected to the client
        print("Connected to client: " + username)
        text.insert(INSERT, "\n Connected to client: " + username+"\n")

    except:
        print("Server is closed")

#This is the Main method which will accept the clients and create threads
def main():
    global count
    global client_list
    client_list =[]
    print("Waiting for Connection")
    try:
        while True:
            client, (client_ip, client_socket) = skt.accept()
            client_list.append(client)
            t = Thread(target=client_thread, args=(client, client_ip, client_socket))
            t.start()
    except:
        print("Server is stopped")

#This method will be called once the exit button on the server is clicked
def close_connection():
    skt.close()
    display.quit()

#Creating the exit button on the server
button = Button(display, text="exit", command=close_connection)

#This method is first executed which will initiate the gui and call the main method
def initial():
    text.pack()
    button.pack()
    pull_button.pack()
    th = Thread(target=main)
    th.start()
    display.mainloop()

if __name__ == '__main__':
    initial()

################################################################### #References: #https://docs.python.org/2/library/socket.html
#https://stackoverflow.com/questions/21153262/sending-html-through-python-socket-server
#http://blog.wachowicz.eu/?p=256
#https://www.thoughtco.com/building-a-simple-web-server-2813571
#https://elearn.uta.edu/bbcswebdav/pid-7205400-dt-content-rid-132005341_2/courses/2185-COMPUTER-NETWORKS-54684-003/Programming%20Assignment%201_reference_Python.pdf
 #https://stackoverflow.com/questions/32168871/tkinter-with-multiple-threads
 #https://stackoverflow.com/questions/42222425/python-sockets-multiple-messages-on-same-connection
 #https://www.programcreek.com/python/example/105552/tkinter.Message
 #https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
 #https://scorython.wordpress.com/2016/06/27/multithreading-with-tkinter/
 #https://docs.python.org/3/tutorial/classes.html
 #https://stackoverflow.com/questions/46788776/update-tkinter-widget-from-main-thread-after-worker-thread-completes
 #https://stackoverflow.com/questions/3567238/threaded-tkinter-script-crashes-when-creating-the-second-toplevel-widget
 #https://stackoverflow.com/questions/10556479/running-a-tkinter-form-in-a-separate-thread/10556698#10556698
 #https://bugs.python.org/issue11077
 #https://github.com/dojafoja/GUI-python-server/blob/master/server.py
 #https://likegeeks.com/python-gui-examples-tkinter-tutorial/
 #https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
 #https://www.geeksforgeeks.org/python-gui-tkinter/
 #https://stackoverflow.com/questions/9342757/tkinter-executing-functions-over-time
 #https://stackoverflow.com/questions/9776718/how-do-i-stop-tkinter-after-function
 #https://stackoverflow.com/questions/49432915/how-to-break-out-of-an-infinite-loop-with-a-tkinter-button
 #https://stackoverflow.com/questions/49742217/python-socket-threading-tkinter-how-to-know-the-message-sender
#https://www.python-course.eu/tkinter_entry_widgets.php
###################################################################


