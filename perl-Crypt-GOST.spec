%define real_name Crypt-GOST

Summary:	Crypt-GOST module for perl 

Name:		perl-%{real_name}
Version:	1.00
Release:	11
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
Patch0:         Crypt-GOST-1.00-fix-build.patch
BuildRequires:	perl-devel

%description
GOST 28147-89 is a 64-bit symmetric block cipher with a 256-bit key developed
in the former Soviet Union. Some information on it is available at
http://vipul.net/gost/.
This module implements GOST encryption. It supports the Crypt::CBC interface.

%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p1 -b .fix-build

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%clean 

%files
%doc Changes README
%{perl_vendorlib}/*/Crypt/GOST.pm
%{perl_vendorlib}/*/auto/Crypt/GOST
%{_mandir}/*/*




