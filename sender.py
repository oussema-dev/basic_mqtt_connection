#!/usr/bin/python3
import tkinter
import paho.mqtt.client as mqtt


def publish(msg):
    client = mqtt.Client(client_id="sender", clean_session=False)
    client.connect("temani49.ddns.net", 1883, 60)
    client.publish("IoT", str(msg.get()), 1, True)
    client.disconnect()


def main():
    window = tkinter.Tk()
    window.title("Sender")
    window.geometry("500x200+300+100")

    label = tkinter.Label(window, text="message:").grid(row=0)
    msg = tkinter.Entry(window)
    msg.grid(row=0, column=1)

    tkinter.Button(window, text="send", command=lambda: publish(
        msg)).grid(row=3, column=1, sticky=tkinter.W, pady=4)

    window.mainloop()


if __name__ == "__main__":
    main()
