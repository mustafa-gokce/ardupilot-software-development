# MAVLink: Micro Air Vehicle Communication Protocol

1. MAVLink is a very lightweight messaging protocol for communicating with drones and between onboard drone components.
2. It is supported by most ground control stations (GCS) and autopilots.
3. Very efficient, light-weight, and reliable.
4. Allows up to 255 concurrent systems on the network (vehicles, ground stations, etc.)
5. Enables both off board and onboard communications:
    * Between a GCS and a drone.
    * Between a drone autopilot and a MAVLink enabled onboard companion computer, smart payload, or onboard process.
    * Between onboard processes and smart payloads.
    * Between an onboard process and another onboard process.
    * Between a drone and a ground-based companion computer.
    * Between a drone and a ground-based process.
    * Between a drone and a ground-based smart payload.
    * Between a ground-based process and a ground-based smart payload.
    * Between a ground-based process and a ground-based process.
    * Between a ground-based smart payload and a ground-based smart payload.
6. MAVLink is a binary telemetry protocol designed for resource-constrained systems and bandwidth-constrained links.
7. Supported by many programming languages and platforms (C, C++, Python, Linux, Windows, MacOS, Android, iOS, etc.).
8. Supports both point-to-point and point-to-multipoint (broadcast) communications.
9. Supports serial (UART) and IP network (UDP, TCP) transports.
10. Supports encryption and authentication (optional).
11. It has many microservices that can be used independently or together such as:
    * Heartbeat: for starting the communication and monitoring the connection.
    * MAVLink FTP: for file transfer.
    * MAVLink Mission Protocol: for mission management.
    * MAVLink Parameter Protocol: for parameter management.
    * MAVLink Time Sync Protocol: for time sync management.
    * MAVLink Command Protocol: for command management.
12. It is a binary protocol that is optimized for size and speed.
13. It is a header-only library that is easy to integrate into embedded systems.
14. MAVLink2 packet format:
    * 1 byte for the header.
    * 1 byte for the payload length.
    * 1 byte for the flags that must be understood by the receiver.
    * 1 byte for the flags that can be ignored by the receiver.
    * 1 byte for the sequence number.
    * 1 byte for the sender system ID.
    * 1 byte for the sender component ID.
    * 3 bytes for the message ID.
    * 0-255 bytes for the payload.
    * 2 bytes for the CRC.
    * 13 bytes for the signature.
15. Packets are sent as a stream of bytes.
16. Payload on the wire may differ from the payload in memory.
    * Larger fields are sent first.
    * Smaller fields are sent last.
17. Empty fields in the payload are not sent.

[Source](https://mavlink.io/en/guide/serialization.html)