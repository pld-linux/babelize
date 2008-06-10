Summary:	Localization Project for many Linux games
Summary(pl.UTF-8):	Projekt lokalizacji dla wielu gier na Linuksa
Name:		babelize
Version:	1.1.1
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	https://babelize.org/download/babelize/%{name}-%{version}.tar.bz2
# Source0-md5:	3ec4cc76e0167849db84155169d58276
Patch0:		%{name}-dirs.patch
URL:		https://babelize.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRequires:	xdelta >= 1.1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Babelize is a project to localize games (commercial or free) that were
ported natively to Linux like that from Lokigames or
Linuxgamepublishing. The only thing you need is one original Game CD
and the patch file from Babelize.

%description -l pl.UTF-8
Babelize jest projektem, który lokalizuje gry (komercyjne i darmowe),
które posiadają natywny port dla Linuksa, jak na przykład gry z
Lokigames czy Linuxgamepublishing. Jedyną potrzebną rzeczą jest
oryginalna płyta CD z grą oraz łata z Babelize.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@${babelizedir}@$(RPM_BUILD_ROOT)%{_bindir}@' {bin/Makefile.am,share/babelize/Makefile.am}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}*.1*
