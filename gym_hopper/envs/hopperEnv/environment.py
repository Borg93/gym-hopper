import gym
from gym import spaces
import sys
import socket
import numpy as np


def setupServer(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    try:
        sock.bind(server_address)
        sock.listen(1)
    except:
        print("Unknown error: " + str(sys.exc_info()[0]))
    return sock, server_address


class GymHopper(gym.Env):

    def __init__(self):
        print("Initialization done.")

    def sendMessage(self, msg):
        self.connectionSend.sendall(str(msg + '&').encode())

    def _step(self, action):
        self.sendMessage("instruction: control path, nozzle state, etc etc pp pp pp pp, and lots of other stuff you spas")
        print("Waiting for an answer...")
        answer = self.connectionRecv.recv(128)
        print(answer.decode())
        observation = 0.0
        reward = 0.0
        done = False
        info = {}
        return observation, reward, done, info

    def _reset(self):
        ipRI = raw_input("Please enter IP (hit enter for localhost): ")
        if ipRI == "":
            ipRI = '127.0.0.1'
        psRI = raw_input("Please enter send port: ")
        prRI = raw_input("Please enter receive port: ")
        print("Setting up communication servers.")
        self.sockSend, self.send_Address = setupServer(ipRI, int(psRI))
        self.sockRecv, self.recv_Address = setupServer(ipRI, int(prRI))
        print("Waiting for send connection...")
        self.connectionSend, self.clientAddressSend = self.sockSend.accept()
        print("...done.")
        print("Waiting for receive connection...")
        self.connectionRecv, self.clientAddressRecv = self.sockRecv.accept()
        print("...done.")
        print("Reset done.")

    def _render(self, mode='human', close=False):
        print("Render done.")

    def closeConnection(self):
        self.connectionSend.close()
        self.connectionRecv.close()
        self.sockRecv.close()
        self.sockRecv.close()

