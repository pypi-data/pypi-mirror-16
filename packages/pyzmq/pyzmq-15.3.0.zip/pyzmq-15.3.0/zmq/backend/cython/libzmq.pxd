"""All the C imports for 0MQ"""

#
#    Copyright (c) 2010 Brian E. Granger & Min Ragan-Kelley
#
#    This file is part of pyzmq.
#
#    pyzmq is free software; you can redistribute it and/or modify it under
#    the terms of the Lesser GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    pyzmq is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Lesser GNU General Public License for more details.
#
#    You should have received a copy of the Lesser GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Import the C header files
#-----------------------------------------------------------------------------

cdef extern from *:
    ctypedef void* const_void_ptr "const void *"
    ctypedef char* const_char_ptr "const char *"

cdef extern from "zmq_compat.h":
    ctypedef signed long long int64_t "pyzmq_int64_t"

include "constant_enums.pxi"

cdef extern from "zmq.h" nogil:

    void _zmq_version "zmq_version"(int *major, int *minor, int *patch)
    
    ctypedef int fd_t "ZMQ_FD_T"
    
    enum: errno
    char *zmq_strerror (int errnum)
    int zmq_errno()

    void *zmq_ctx_new ()
    int zmq_ctx_destroy (void *context)
    int zmq_ctx_set (void *context, int option, int optval)
    int zmq_ctx_get (void *context, int option)
    void *zmq_init (int io_threads)
    int zmq_term (void *context)
    
    # blackbox def for zmq_msg_t
    ctypedef void * zmq_msg_t "zmq_msg_t"
    
    ctypedef void zmq_free_fn(void *data, void *hint)
    
    int zmq_msg_init (zmq_msg_t *msg)
    int zmq_msg_init_size (zmq_msg_t *msg, size_t size)
    int zmq_msg_init_data (zmq_msg_t *msg, void *data,
        size_t size, zmq_free_fn *ffn, void *hint)
    int zmq_msg_send (zmq_msg_t *msg, void *s, int flags)
    int zmq_msg_recv (zmq_msg_t *msg, void *s, int flags)
    int zmq_msg_close (zmq_msg_t *msg)
    int zmq_msg_move (zmq_msg_t *dest, zmq_msg_t *src)
    int zmq_msg_copy (zmq_msg_t *dest, zmq_msg_t *src)
    void *zmq_msg_data (zmq_msg_t *msg)
    size_t zmq_msg_size (zmq_msg_t *msg)
    int zmq_msg_more (zmq_msg_t *msg)
    int zmq_msg_get (zmq_msg_t *msg, int option)
    int zmq_msg_set (zmq_msg_t *msg, int option, int optval)
    const_char_ptr zmq_msg_gets (zmq_msg_t *msg, const_char_ptr property)
    int zmq_has (const_char_ptr capability)

    void *zmq_socket (void *context, int type)
    int zmq_close (void *s)
    int zmq_setsockopt (void *s, int option, void *optval, size_t optvallen)
    int zmq_getsockopt (void *s, int option, void *optval, size_t *optvallen)
    int zmq_bind (void *s, char *addr)
    int zmq_connect (void *s, char *addr)
    int zmq_unbind (void *s, char *addr)
    int zmq_disconnect (void *s, char *addr)

    int zmq_socket_monitor (void *s, char *addr, int flags)
    
    # send/recv
    int zmq_sendbuf (void *s, const_void_ptr buf, size_t n, int flags)
    int zmq_recvbuf (void *s, void *buf, size_t n, int flags)

    ctypedef struct zmq_pollitem_t:
        void *socket
        int fd
        short events
        short revents

    int zmq_poll (zmq_pollitem_t *items, int nitems, long timeout)

    int zmq_device (int device_, void *insocket_, void *outsocket_)
    int zmq_proxy (void *frontend, void *backend, void *capture)

cdef extern from "zmq_utils.h" nogil:

    void *zmq_stopwatch_start ()
    unsigned long zmq_stopwatch_stop (void *watch_)
    void zmq_sleep (int seconds_)
    int zmq_curve_keypair (char *z85_public_key, char *z85_secret_key)

