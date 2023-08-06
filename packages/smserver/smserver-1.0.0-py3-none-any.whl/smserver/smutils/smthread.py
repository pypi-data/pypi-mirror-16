#!/usr/bin/env python3
# -*- coding: utf8 -*-

import sys
import datetime
import logging
from threading import Lock

from smserver.smutils import smpacket
from smserver.smutils.smconnections import smtcpsocket, udpsocket

if sys.version_info[1] > 2:
    from smserver.smutils.smconnections import asynctcpserver, websocket

class StepmaniaServer(object):
    _logger = logging.getLogger('stepmania')

    SERVER_TYPE = {
        "classic": smtcpsocket.SocketServer,
        "udp": udpsocket.UDPServer,
        "async": asynctcpserver.AsyncSocketServer if sys.version_info[1] > 2 else None,
        "websocket": websocket.WebSocketServer if sys.version_info[1] > 2 else None
    }

    def __init__(self, servers):
        self.mutex = Lock()
        self._connections = []
        self._servers = []
        for ip, port, server_type in servers:
            self._servers.append(self.SERVER_TYPE[server_type](self, ip, port))

    def is_alive(self):
        """ Check if all the thread are still alive """

        for server in self._servers:
            if not server.is_alive():
                return False

        return True

    def start(self):
        for server in self._servers:
            server.start()

        for server in self._servers:
            server.join()

    @property
    def connections(self):
        with self.mutex:
            return self._connections

    def add_connection(self, conn):
        self._logger.info("New connection: %s on port %s", conn.ip, conn.port)

        with self.mutex:
            self._connections.append(conn)

    def find_connection(self, user_id):
        """ Find the connection where a specific user is """

        for conn in self.connections:
            if user_id in conn.users:
                return conn

        return None

    def room_connections(self, room_id):
        """ Iterator of all the connections in a given room """

        for conn in self.connections:
            if conn.room != room_id:
                continue

            yield conn

    def player_connections(self, room_id):
        """ Iterator of all the connection's player (not spectator) """

        for conn in self.room_connections(room_id):
            if conn.spectate is True:
                continue

            yield conn

    def ingame_connections(self, room_id):
        """ Iterator of all the connections in a given room which have send a NSCGSR packet """

        for conn in self.room_connections(room_id):
            if not conn.songstats.get("start_at"):
                continue

            yield conn

    def sendall(self, packet):
        """
            Send a packet to all the connections in the server

            :param packet: The packet to send
            :type packet: smserver.smutils.smpacket.SMPacket
        """

        for conn in self._connections:
            conn.send(packet)

    def sendroom(self, room_id, packet):
        """
            Send a packet to all the connections in the room

            :param int room_id: Room_id where to send the packet
            :param packet: The packet to send
            :type packet: smserver.smutils.smpacket.SMPacket
        """

        for conn in self.room_connections(room_id):
            conn.send(packet)

    def sendingame(self, room_id, packet):
        """
            Send a packet to all the connections currently playing in the room

            :param int room_id: Room_id where to send the packet
            :param packet: The packet to send
            :type packet: smserver.smutils.smpacket.SMPacket
        """

        for conn in self.ingame_connections(room_id):
            conn.send(packet)

    def sendplayers(self, room_id, packet):
        """
            Send a packet to all the player's connections in the room

            (not to spectator player)

            :param int room_id: Room_id where to send the packet
            :param packet: The packet to send
            :type packet: smserver.smutils.smpacket.SMPacket
        """

        for conn in self.player_connections(room_id):
            conn.send(packet)

    def on_disconnect(self, serv):
        with self.mutex:
            if serv not in self._connections:
                return

            self._connections.remove(serv)

    def on_packet(self, serv, packet):
        PacketHandler(self, serv, packet).handle()


class PacketHandler(object):
    def __init__(self, server, conn, packet):
        self.server = server
        self.packet = packet
        self.conn = conn

    def handle(self):
        func = getattr(self, "on_%s" % self.packet.command.name.lower(), None)
        if not func:
            return None

        func()

    def on_nscping(self):
        self.conn.send(smpacket.SMPacketServerNSCPingR())

    def on_nscpingr(self):
        with self.conn.mutex:
            self.conn.last_ping = datetime.datetime.now()

    def on_nschello(self):
        self.conn.send(smpacket.SMPacketServerNSCHello(version=128, name="Stepmania-Server"))

    def on_nscgsr(self):
        pass

    def on_nscgon(self):
        pass

    def on_nscgsu(self):
        pass

    def on_nscsu(self):
        pass

    def on_nsccm(self):
        pass

    def on_nscrsg(self):
        pass

    def on_nsccuul(self):
        pass

    def on_nsscsms(self):
        pass

    def on_nscuopts(self):
        pass

    def on_nssmonl(self):
        PacketHandler(self.server, self.conn, self.packet["packet"]).handle()

    def on_nscformatted(self):
        pass

    def on_nscattack(self):
        pass

    def on_xmlpacket(self):
        pass

    def on_login(self):
        response = smpacket.SMPacketServerNSCUOpts(
            packet=smpacket.SMOPacketServerLogin(
                approval=1,
                text="Succesfully Login"
            )
        )
        self.conn.send(response)

    def on_enterroom(self):
        pass

    def on_createroom(self):
        pass

    def on_roominfo(self):
        pass

    def send(self, packet):
        self.conn.send(packet)

    def sendall(self, packet):
        self.server.sendall(packet)

    def sendroom(self, room, packet):
        self.server.sendroom(room, packet)

