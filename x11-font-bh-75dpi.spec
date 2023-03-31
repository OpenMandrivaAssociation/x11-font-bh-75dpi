Name: x11-font-bh-75dpi
Version: 1.0.4
Release: 2
Summary: Xorg X11 font bh-75dpi
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-bh-75dpi-%{version}.tar.xz
# We may modify the software, but then we won't be able to use
# "OPEN LOOK" or "Lucida" trademarks. See #38627
License: Lucida
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font bh-75dpi.

%prep
%autosetup -p1 -n font-bh-75dpi-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/75dpi
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.scale

%post
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%postun
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%files
%doc COPYING
%{_datadir}/fonts/75dpi/lu*.pcf.gz
