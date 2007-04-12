%define module	Class-Trigger
%define name	perl-%{module}
%define version 0.10
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Mixin to add / call inheritable triggers
License:	GPL or Artistic
Group:		Development/Perl
source:		http://search.cpan.org/dist/M/MI/MIYAGAWA/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:  perl-Class-Data-Inheritable
BuildRequires:  perl-IO-stringy
BuildRoot:	%{_tmppath}/%{name}-%{version}
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

