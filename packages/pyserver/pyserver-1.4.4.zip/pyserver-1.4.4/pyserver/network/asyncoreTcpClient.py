#!/usr/bin/python
'''
@file asyncoreTcpClient.py
@author Woong Gyu La a.k.a Chris. <juhgiyo@gmail.com>
        <http://github.com/juhgiyo/pyserver>
@date March 10, 2016
@brief AsyncoreTcpClient Interface
@version 0.1

@section LICENSE

The MIT License (MIT)

Copyright (c) 2016 Woong Gyu La <juhgiyo@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@section DESCRIPTION

AsyncoreTcpClient Class.
'''
import asyncore, socket
from threading import *
import sys
from collections import deque
from asyncoreController import AsyncoreController
from inspect import isfunction
from sets import Set
from preamble import *
from pyserver.network import *
import traceback

'''
Interfaces
variables
- hostname
- port
- addr = (hostname,port)
- callbackObj
functions
- def send(data)
- def close() # close the socket
'''


class AsyncoreTcpClient(asyncore.dispatcher):
    def __init__(self, hostname, port, callbackObj, noDelay=True):
        asyncore.dispatcher.__init__(self)
        self.isClosing = False
        self.callbackObj = None
        if callbackObj is not None and isinstance(callbackObj, ITcpSocketCallback):
            self.callbackObj = callbackObj
        else:
            raise Exception('callbackObj is None or not an instance of ITcpSocketCallback class')
        self.hostname = hostname
        self.port = port
        self.addr = (hostname, port)
        self.sendQueue = deque()  # thread-safe dequeue
        self.transport = {'packet': None, 'type': PacketType.SIZE, 'size': SIZE_PACKET_LENGTH, 'offset': 0}

        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        if noDelay:
            self.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.set_reuse_addr()
        err = None
        try:
            self.connect((hostname, port))
            AsyncoreController.Instance().add(self)
        except Exception as e:
            err = e
        finally:
            def callbackConnection():
                if self.callbackObj is not None:
                    self.callbackObj.onNewConnection(self, err)

            thread = Thread(target=callbackConnection)
            thread.start()

    def handle_connect(self):
        pass

    def handle_read(self):
        try:
            data = self.recv(self.transport['size'])
            readSize = 0
            if data == None or len(data) == 0:
                return
            if self.transport['packet'] is None:
                self.transport['packet'] = data
            else:
                self.transport['packet'] += data
            readSize = len(data)
            if readSize < self.transport['size']:
                self.transport['offset'] = self.transport['offset'] + readSize
                self.transport['size'] = self.transport['size'] - readSize
            else:
                if self.transport['type'] == PacketType.SIZE:
                    shouldReceive = Preamble.toShouldReceive(self.transport['packet'])
                    if shouldReceive < 0:
                        preambleOffset = Preamble.checkPreamble(self.transport['packet'])
                        self.transport['offset'] = len(self.transport['packet']) - preambleOffset
                        self.transport['size'] = preambleOffset
                        self.transport['packet'] = self.transport['packet'][
                                                   len(self.transport['packet']) - preambleOffset:]
                        return
                    self.transport = {'packet': None, 'type': PacketType.DATA, 'size': shouldReceive, 'offset': 0}
                else:
                    receivePacket=self.transport
                    self.transport = {'packet': None, 'type': PacketType.SIZE, 'size': SIZE_PACKET_LENGTH, 'offset': 0}
                    self.callbackObj.onReceived(self, receivePacket['packet'])
        except Exception as e:
            print e
            traceback.print_exc()

    def writable(self):
        return len(self.sendQueue) != 0

    def handle_write(self):
        if len(self.sendQueue) != 0:
            sendObj = self.sendQueue.popleft()
            state = State.SUCCESS
            try:
                sent = asyncore.dispatcher.send(self, sendObj['data'][sendObj['offset']:])
                if sent < len(sendObj['data']):
                    sendObj['offset'] = sendObj['offset'] + sent
                    self.sendQueue.appendLeft(sendObj)
                    return
            except Exception as e:
                print e
                traceback.print_exc()
                state = State.FAIL_SOCKET_ERROR
            try:
                if self.callbackObj != None:
                    self.callbackObj.onSent(self, state, sendObj['data'])
            except Exception as e:
                print e
                traceback.print_exc()

    def close(self):
        if not self.isClosing:
            self.handle_close()

    def handle_error(self):
        if not self.isClosing:
            self.handle_close()

    def handle_close(self):
        try:
            self.isClosing = True
            asyncore.dispatcher.close(self)
            AsyncoreController.Instance().discard(self)
            if self.callbackObj is not None:
                self.callbackObj.onDisconnect(self)
        except Exception as e:
            print e
            traceback.print_exc()

    def send(self, data):
        self.sendQueue.append({'data': Preamble.toPreamblePacket(len(data)) + data, 'offset': 0})

    def gethostbyname(self, arg):
        return self.socket.gethostbyname(arg)

    def gethostname():
        return self.socket.gethostname()
