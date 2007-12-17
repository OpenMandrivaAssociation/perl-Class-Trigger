%define module	Class-Trigger
%define name	perl-%{module}
%define version 0.12
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Mixin to add / call inheritable triggers
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(IO::Stringy)
BuildArch:	noarch

%description
Class::Trigger is a mixin class to add / call triggers (or hooks)
that get called at some points you specify.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*

