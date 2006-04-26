nobase_xcbinclude_HEADERS = xcb.xsd \
                            xcb_types.xml \
                            xproto.xml \
                            extensions/bigreq.xml \
                            extensions/composite.xml \
                            extensions/damage.xml \
                            extensions/dpms.xml \
                            extensions/glx.xml \
                            extensions/randr.xml \
                            extensions/record.xml \
                            extensions/render.xml \
                            extensions/res.xml \
                            extensions/screensaver.xml \
                            extensions/shape.xml \
                            extensions/shm.xml \
                            extensions/sync.xml \
                            extensions/xc_misc.xml \
                            extensions/xevie.xml \
                            extensions/xf86dri.xml \
                            extensions/xfixes.xml \
                            extensions/xprint.xml \
                            extensions/xtest.xml \
                            extensions/xv.xml    \
                            extensions/xvmc.xml

if HAVE_XMLLINT
check-local:
	$(XMLLINT) --noout --schema $(srcdir)/xcb.xsd \
	           $(srcdir)/*.xml $(srcdir)/extensions/*.xml
endif
