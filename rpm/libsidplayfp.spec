Name:       libsidplayfp
Summary:    SID playback library
Version:    3.1.1
Release:    1
License:    GPLv2+
URL:        https://github.com/sailfishos/libsidplayfp
Source:     %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(libresidfp)

%description
Libsidplayfp is a fork of sidplay2 born with the aim to improve the quality
of emulating the 6581, 8580 chips and the surrounding C64 system in order to
play SID music better.

%package devel
Summary:    Libsidplayfp development headers and libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files required for using libsidplayfp library.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%configure
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libsidplayfp.so.*
%{_libdir}/libstilview.so.*

%files devel
%{_libdir}/libsidplayfp.a
%{_libdir}/libsidplayfp.so
%{_libdir}/libstilview.a
%{_libdir}/libstilview.so
%{_libdir}/pkgconfig/libsidplayfp.pc
%{_libdir}/pkgconfig/libstilview.pc
%dir %{_includedir}/stilview
%{_includedir}/stilview/stildefs.h
%{_includedir}/stilview/stil.h
%dir %{_includedir}/sidplayfp
%{_includedir}/sidplayfp/sidbuilder.h
%{_includedir}/sidplayfp/SidConfig.h
%{_includedir}/sidplayfp/SidDatabase.h
%{_includedir}/sidplayfp/siddefs.h
%{_includedir}/sidplayfp/SidInfo.h
%{_includedir}/sidplayfp/sidplayfp.h
%{_includedir}/sidplayfp/SidTune.h
%{_includedir}/sidplayfp/SidTuneInfo.h
%{_includedir}/sidplayfp/sidversion.h
%dir %{_includedir}/sidplayfp/builders
%{_includedir}/sidplayfp/builders/sidlite.h
%{_includedir}/sidplayfp/builders/residfp.h
