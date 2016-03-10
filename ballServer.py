# -*- coding: utf-8 -*-

from ball import Ball
from time import sleep
from testserver import SessionServer
import socket


class BallSessionServer(SessionServer):
    def __init__(self, host, port, commandCallback):
        SessionServer.__init__(self, host, port)
        self._host = host
        self._port = port
        self.cmdFun = commandCallback

    def run(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        st.bind((self._host, self._port))
        st.listen(1)
        conn, origin = st.accept()
        while True:
            data = conn.recv(1024).strip()
            if not data:
                break
            print "RX:", data
            if data in ["Up", "Down", "Left", "Right"]:
                conn.sendall("Ok")
                self._cmdFun(data)
            else:
                conn.sendall("??")

        conn.close()


if __name__ == "__main__":
    # MAIN

    b1 = Ball()
    b1.start()

    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 25000  # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    sessions = []
    print "Ball listening on port", PORT
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        PORT += 1
        conn.sendall(str(PORT))
        session = BallSessionServer(HOST, PORT, b1.command)
        session.start()
        sessions.append(session)
        sleep(0.1)
        activeSessions = 0
        for t in sessions:
            if t.is_alive():
                activeSessions += 1
        if activeSessions == 0:
            conn.close()
            break
