#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.57)
AC_INIT([XCBProto],
        0.9,
        [xcb@lists.freedesktop.org])
AC_CONFIG_SRCDIR([xcb-proto.pc.in])
AM_INIT_AUTOMAKE([foreign dist-bzip2])

xcbincludedir='${includedir}/X11/XCB'
AC_SUBST(xcbincludedir)

AC_OUTPUT([Makefile src/Makefile xcb-proto.pc])
