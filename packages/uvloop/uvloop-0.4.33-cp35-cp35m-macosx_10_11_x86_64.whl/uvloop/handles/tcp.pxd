cdef class TCPServer(UVStreamServer):

    cdef:
        uv.uv_tcp_t _handle_data

    cdef open(self, int sockfd)
    cdef bind(self, system.sockaddr* addr, unsigned int flags=*)

    @staticmethod
    cdef TCPServer new(Loop loop, object protocol_factory, Server server,
                       object ssl, unsigned int flags)


cdef class TCPTransport(UVStream):

    cdef:
        uv.uv_tcp_t _handle_data
        bint __peername_set
        bint __sockname_set
        system.sockaddr_storage __peername
        system.sockaddr_storage __sockname

    cdef bind(self, system.sockaddr* addr, unsigned int flags=*)
    cdef open(self, int sockfd)
    cdef connect(self, system.sockaddr* addr)

    @staticmethod
    cdef TCPTransport new(Loop loop, object protocol, Server server,
                          object waiter)
