SUBDIRS += Dispatcher
SUBDIRS += Wfdm16Logger
SUBDIRS += Wfdm16Monitor
SUBDIRS += Wfdm16Reader

.PHONY: $(SUBDIRS)

all: $(SUBDIRS)
	@set -e; for dir in $(SUBDIRS); do $(MAKE) -C $${dir} $@; done

clean:
	@set -e; for dir in $(SUBDIRS); do $(MAKE) -C $${dir} $@; done
