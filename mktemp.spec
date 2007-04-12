Summary:	A small utility for safely making /tmp files
Name:		mktemp
Version:	1.5
Release:	%mkrel 14
License:	BSD
Group:		File tools
Url:		http://www.mktemp.org/
Source:		ftp://ftp.mktemp.org/pub/mktemp/mktemp-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The mktemp utility takes a given file name template and overwrites
a portion of it to create a unique file name.  This allows shell
scripts and other programs to safely create and use /tmp files.

Install the mktemp package if you need to use shell scripts or other
programs which will create and use unique /tmp files.

%prep
%setup

%build
%configure2_5x --bindir=/bin
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

perl -pi -e "s!/usr/man!%{_mandir}!g" Makefile

%makeinstall bindir=%{buildroot}/bin

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) /bin/%{name}
%{_mandir}/man1/mktemp.1*


