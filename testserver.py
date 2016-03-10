# -*- coding: utf-8 -*-

# Test server program
import socket
from threading import Thread
from time import sleep


class SessionServer(Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self._host = host
        self._port = port

    def run(self):
        st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        st.bind((self._host, self._port))
        st.listen(1)
        conn, origin = st.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall("Ok")
            print "RX:", data
        conn.close()


# MAIN
if __name__ == '__main__':
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 25000              # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    sessions = []
    print "Listening on port", PORT
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print 'Connected by', addr
        PORT += 1
        conn.sendall(str(PORT))
        session = SessionServer(HOST, PORT)
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

