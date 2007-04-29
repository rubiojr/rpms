# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Expect-Simple

Summary: Wrapper around the Expect module
Name: perl-Expect-Simple
Version: 0.02
Release: 1
License: GPL
Group: Development/Libraries
URL: http://search.cpan.org/dist/Expect-Simple/

Source: http://www.cpan.org/modules/by-module/Expect/Expect-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Expect)

%description
Expect::Simple is a wrapper around the Expect module which should
suffice for simple applications. It hides most of the Expect
machinery; the Expect object is available for tweaking if need be.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Expect/

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
