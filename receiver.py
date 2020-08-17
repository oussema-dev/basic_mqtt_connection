#!/usr/bin/python3
import tkinter
import paho.mqtt.client as mqtt
import threading

topic = None
message = None
desc = None


def dataReceived(client, userdata, msg):
    global message
    global topic
    global desc

    #print(msg.topic+" "+str(msg.payload)[2:-1])

    topic.configure(state="normal")
    topic.delete(0, 'end')
    topic.insert(0, str(msg.topic))
    topic.configure(state="disabled")

    message.configure(state="normal")
    message.delete(0, 'end')
    message.insert(0, str(msg.payload)[2:-1])
    message.configure(state="disabled")

    desc.configure(state="normal")
    desc.delete(0, 'end')
    if(float(str(msg.payload)[2:-1]) <= 30):
        desc.insert(0, "Température acceptable")
    else:
        desc.insert(0, "Température elevée")
    desc.configure(state="disabled")


def do_this():
    client = mqtt.Client(client_id="receiver", clean_session=False)
    client.on_message = dataReceived
    client.connect("temani49.ddns.net", 1883, 60)
    client.subscribe("IoT", 1)
    client.loop_forever()
    return


def start_listener():
    thread = threading.Thread(target=do_this).start()
    thread.join()


def main():
    global message
    global topic
    global desc

    window = tkinter.Tk()
    window.title("Receiver")
    window.geometry("500x200+300+100")

    labelTopic = tkinter.Label(window, text="Topic: ").grid(row=0)
    topic = tkinter.Entry(window, state='disabled')
    topic.grid(row=0, column=1)

    labelMesg = tkinter.Label(window, text="Message: ").grid(row=1)
    message = tkinter.Entry(window, state='disabled')
    message.grid(row=1, column=1)

    labelDesc = tkinter.Label(window, text="Description: ").grid(row=2)
    desc = tkinter.Entry(window, state='disabled')
    desc.grid(row=2, column=1)

    tkinter.Button(window, text="Start listener", command=start_listener).grid(
        row=3, column=1, sticky=tkinter.W, pady=4)

    window.mainloop()


if __name__ == "__main__":
    main()
