%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	SHA256
Summary:	Digest::SHA256 - SHA-256/384/512 hash algorithm implementation
Summary(pl):	Digest::SHA256 - implementacja algorytmu mieszaj±cego SHA-256/384/512
Name:		perl-Digest-SHA256
Version:	0.01b
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	08f2b87bad328275bdebf64c18bfcb31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Digest/SHA256.pm
%dir %{perl_vendorarch}/auto/Digest/SHA256
%{perl_vendorarch}/auto/Digest/SHA256/autosplit.ix
%{perl_vendorarch}/auto/Digest/SHA256/SHA256.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/SHA256/SHA256.so
%{_mandir}/man3/Digest::SHA256.3pm*
