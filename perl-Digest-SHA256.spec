%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA256
Summary:	Digest::SHA256 Perl module - SHA-256/384/512 hash algorithm implementation
Summary(pl):	Modu³ Perla Digest::SHA256 - implementacja algorytmu mieszaj±cego SHA-256/384/512
Name:		perl-Digest-SHA256
Version:	0.01b
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::SHA256 module allows you to use the NIST SHA 256/384/512 hash
algorithm.

%description -l pl
Modu³ Digest::SHA256 pozwala na u¿ywanie algorytmu mieszaj±cego NIST
SHA 256/384/512.

%prep
%setup -q -n %{pnam}-0.01

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Digest/SHA256.pm
%dir %{perl_sitearch}/auto/Digest/SHA256
%{perl_sitearch}/auto/Digest/SHA256/autosplit.ix
%{perl_sitearch}/auto/Digest/SHA256/SHA256.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/SHA256/SHA256.so
%{_mandir}/man3/Digest::SHA256.3pm*
