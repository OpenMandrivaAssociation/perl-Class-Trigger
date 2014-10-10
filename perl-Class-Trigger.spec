%define upstream_name	 Class-Trigger
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Mixin to add / call inheritable triggers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(IO::Stringy)
BuildArch:	noarch

%description
Class::Trigger is a mixin class to add / call triggers (or hooks)
that get called at some points you specify.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 680829
- mass rebuild

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 461265
- update to 0.14

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 403015
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.13-3mdv2009.0
+ Revision: 256034
- rebuild

* Fri Mar 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2008.1
+ Revision: 181155
- update to new version 0.13

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.0
+ Revision: 78725
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.11-1mdv2008.0
+ Revision: 19801
- 0.11


* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.10-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- New release 0.10
- spec rewrite

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 0.09-1mdk
- Initial build.

