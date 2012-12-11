%define real_name Crypt-GOST

Summary:	Crypt-GOST module for perl 
Name:		perl-%{real_name}
Version:	1.00
Release:	8
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GOST 28147-89 is a 64-bit symmetric block cipher with a 256-bit key developed
in the former Soviet Union. Some information on it is available at
http://vipul.net/gost/.
This module implements GOST encryption. It supports the Crypt::CBC interface.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*/Crypt/GOST.pm
%{perl_vendorlib}/*/auto/Crypt/GOST
%{_mandir}/*/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.00-8
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.00-7
+ Revision: 680852
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.00-6mdv2011.0
+ Revision: 555713
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2010.0
+ Revision: 430358
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2009.0
+ Revision: 256265
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.00-2mdv2008.1
+ Revision: 152033
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.00-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

