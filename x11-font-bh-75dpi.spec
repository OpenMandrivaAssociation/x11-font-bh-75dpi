Name: x11-font-bh-75dpi
Version: 1.0.3
Release: 9
Summary: Xorg X11 font bh-75dpi
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-bh-75dpi-%{version}.tar.bz2
# We may modify the software, but then we won't be able to use
# "OPEN LOOK" or "Lucida" trademarks. See #38627
License: Lucida
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-75dpi-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bh-75dpi

%prep
%setup -q -n font-bh-75dpi-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/75dpi

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/75dpi/fonts.dir
rm -f %{buildroot}%_datadir/fonts/75dpi/fonts.scale

%post
mkfontscale %_datadir/fonts/75dpi
mkfontdir %_datadir/fonts/75dpi

%postun
mkfontscale %_datadir/fonts/75dpi
mkfontdir %_datadir/fonts/75dpi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/75dpi/lu*.pcf.gz


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-4mdv2011.0
+ Revision: 675439
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-3
+ Revision: 675199
- rebuild for new rpm-setup

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671194
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 618711
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 583193
- new release

* Thu Jan 21 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 494544
- Fix license (#38627)
- New version: 1.0.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 351360
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 225974
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2008.1
+ Revision: 129708
- kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild prep


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:51:46 (51466)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

