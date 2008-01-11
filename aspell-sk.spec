%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.52-0
%define languagelocal slovak
%define languageeng slovak
%define languageenglazy Slovak
%define languagecode sk
%define lc_ctype sk_SK

Summary:       Slovak files for aspell
Name:          aspell-%{languagecode}
Version:       0.52.0
Release:       %mkrel 4
Group:         System/Internationalization
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}


BuildRequires: aspell >= 0.50
BuildRequires: make
Requires:      aspell >= 0.50

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A Slovak dictionary for use with aspell, a spelling checker.


%prep
%setup -q -n %{name}-%{src_ver}

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


