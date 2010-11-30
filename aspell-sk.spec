%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 2.01-2
%define languagelocal slovak
%define languageeng slovak
%define languageenglazy Slovak
%define languagecode sk
%define lc_ctype sk_SK

Summary:       Slovak files for aspell
Name:          aspell-%{languagecode}
Version:       2.01.2
Release:       %mkrel 4
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell6-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A Slovak dictionary for use with aspell, a spelling checker.


%prep
%setup -q -n aspell6-sk-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

#cp doc/README README.sk
chmod 644 README* Copyright doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/*
%{_libdir}/aspell-*/*


