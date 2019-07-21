#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	Async-HTTP-Server
Summary:	Net::Async-HTTP-Server - serve HTTP with IO::Async
Name:		perl-Net-Async-HTTP-Server
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4b13d36f2a309cde31df7c154aa3af46
URL:		http://search.cpan.org/dist/Net-Async-HTTP-Server/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Identity
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows a program to respond asynchronously to HTTP
requests, as part of a program based on IO::Async. An object in this
class listens on a single port and invokes the on_request callback or
subclass method whenever an HTTP request is received, allowing the
program to respond to it.

For accepting HTTP connections via PSGI and Plack, see also
Plack::Handler::Net::Async::HTTP::Server.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a psgifiles $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/Async/HTTP/Server.pm
%{perl_vendorlib}/Net/Async/HTTP/Server
%{perl_vendorlib}/Plack/Handler/Net/Async/HTTP/Server.pm
%{_mandir}/man3/Net::Async::HTTP::Server*.3pm*
%{_mandir}/man3/Plack::Handler::Net::Async::HTTP::Server*.3pm*
%{_examplesdir}/%{name}-%{version}
