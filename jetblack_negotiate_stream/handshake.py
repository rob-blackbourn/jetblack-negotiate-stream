"""The handshake record used in the connection negotiation"""

from __future__ import annotations

import enum
import struct


class HandshakeState(enum.IntEnum):
    """The handshake state.

    The state is either in-progress, done or error."""

    DONE = 0x14
    ERROR = 0x15
    IN_PROGRESS = 0x16


class HandshakeRecord:
    """The record exchanged during the handshake."""

    FORMAT = ">BBBH"

    def __init__(
            self,
            state: HandshakeState,
            major: int,
            minor: int,
            payload_size: int
    ) -> None:
        self.state = state
        self.major = major
        self.minor = minor
        self.payload_size = payload_size

    def pack(self) -> bytes:
        return struct.pack(
            self.FORMAT,
            self.state,
            self.major,
            self.minor,
            self.payload_size
        )

    @classmethod
    def unpack(cls, buf: bytes) -> HandshakeRecord:
        (state, major, minor, payload_size) = struct.unpack(cls.FORMAT, buf)
        return HandshakeRecord(state, major, minor, payload_size)
