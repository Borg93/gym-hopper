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
        print("[ env ] Unknown error: " + str(sys.exc_info()[0]))
    return sock, server_address


def _print(msg):
    print("[ env ] " + msg)


class GymHopperPC(gym.Env):

    def sendMessage(self, msg):
        try:
            self.connectionSend.sendall(str(msg + '&').encode())
        except:
            _print("Unknown error during send: " + str(sys.exc_info()[0]))

    def interpret_answer(self, result):
        #self.axis_state = 
        return np.array([0.0, 0.0, 0.0]), 0.0, False, {}

    def __init__(self):
        self.action_space = spaces.Box(low=0.0, high=1.0, shape=(4,))
        self.axis_state = spaces.Box(low=0.0, high=1.0, shape=(6,))
        #quantec kr210 3100 ultra
        self.axis_limits = np.array([
            [-185.0, 185.0]
            [-130.0, 0.0]
            [-40.0, 148.0]
            [-350.0, 350.0]
            [-120.0, 120.0]
            [-350.0, 350.0]])
        self.tcp
        _print("Initialization done.")

    def _step(self, action):
        _print(">>> sending: ")
        self.sendMessage(str(action))
        while True:
            data = self.connectionRecv.recv(256)
            answer = data.decode()
            if not answer == "":
                _print("<<< answer: " + answer)
                observation, reward, done, info = self.interpret_answer(answer)
                return observation, reward, done, info
                break

    def _reset(self):
        ipRI = raw_input("[ env ] Please enter IP (hit enter for localhost): ")
        if ipRI == "":
            ipRI = '127.0.0.1'
        psRI = raw_input("[ env ] Please enter send port: ")
        prRI = raw_input("[ env ] Please enter receive port: ")
        _print("Setting up communication servers.")
        self.sockSend, self.send_Address = setupServer(ipRI, int(psRI))
        self.sockRecv, self.recv_Address = setupServer(ipRI, int(prRI))
        _print("Waiting for client on send server...")
        self.connectionSend, self.clientAddressSend = self.sockSend.accept()
        _print("...Connected")
        _print("Waiting for client on receive server...")
        self.connectionRecv, self.clientAddressRecv = self.sockRecv.accept()
        _print("...Connected")
        _print("Reset done.")

    def _render(self, mode='human', close=False):
        _print("Render done.")

    def closeConnection(self):
        self.connectionSend.close()
        self.connectionRecv.close()
        self.sockRecv.close()
        self.sockRecv.close()
