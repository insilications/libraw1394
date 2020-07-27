#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libraw1394
Version  : 2.1.2
Release  : 7
URL      : https://www.kernel.org/pub/linux/libs/ieee1394/libraw1394-2.1.2.tar.gz
Source0  : https://www.kernel.org/pub/linux/libs/ieee1394/libraw1394-2.1.2.tar.gz
Summary  : Streaming library for IEEE1394
Group    : Development/Tools
License  : LGPL-3.0-or-later
Requires: libraw1394-bin = %{version}-%{release}
Requires: libraw1394-lib = %{version}-%{release}
Requires: libraw1394-man = %{version}-%{release}
BuildRequires : findutils
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libraw1394
==========
1. About libraw1394
libraw1394 is the only supported interface to the kernel side raw1394 of
the Linux IEEE-1394 subsystem, which provides direct access to the connected
1394 buses to user space.  Through libraw1394/raw1394, applications can directly
send to and receive from other nodes without requiring a kernel driver for the
protocol in question.

%package bin
Summary: bin components for the libraw1394 package.
Group: Binaries

%description bin
bin components for the libraw1394 package.


%package dev
Summary: dev components for the libraw1394 package.
Group: Development
Requires: libraw1394-lib = %{version}-%{release}
Requires: libraw1394-bin = %{version}-%{release}
Provides: libraw1394-devel = %{version}-%{release}
Requires: libraw1394 = %{version}-%{release}

%description dev
dev components for the libraw1394 package.


%package lib
Summary: lib components for the libraw1394 package.
Group: Libraries

%description lib
lib components for the libraw1394 package.


%package man
Summary: man components for the libraw1394 package.
Group: Default

%description man
man components for the libraw1394 package.


%package staticdev
Summary: staticdev components for the libraw1394 package.
Group: Default
Requires: libraw1394-dev = %{version}-%{release}

%description staticdev
staticdev components for the libraw1394 package.


%prep
%setup -q -n libraw1394-2.1.2
cd %{_builddir}/libraw1394-2.1.2

%build
## build_prepend content
#find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
#autoreconf -fiv
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595838894
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%reconfigure  --enable-static --enable-shared
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'config.status' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
## make_prepend end
make  %{?_smp_mflags}


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1595838894
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dumpiso
/usr/bin/sendiso
/usr/bin/testlibraw

%files dev
%defattr(-,root,root,-)
/usr/include/libraw1394/csr.h
/usr/include/libraw1394/ieee1394.h
/usr/include/libraw1394/raw1394.h
/usr/lib64/libraw1394.so
/usr/lib64/pkgconfig/libraw1394.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libraw1394.so.11
/usr/lib64/libraw1394.so.11.1.0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dumpiso.1
/usr/share/man/man1/sendiso.1
/usr/share/man/man1/testlibraw.1
/usr/share/man/man5/isodump.5

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libraw1394.a
