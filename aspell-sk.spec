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
Release:       %mkrel 5
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.01.2-5mdv2011.0
+ Revision: 662867
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.01.2-4mdv2011.0
+ Revision: 603460
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.01.2-3mdv2010.1
+ Revision: 518961
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 2.01.2-2mdv2010.0
+ Revision: 413103
- rebuild

* Tue Apr 14 2009 Antoine Ginies <aginies@mandriva.com> 2.01.2-1mdv2009.1
+ Revision: 366868
- update very old release (1 year old)

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 2.00.0-3mdv2009.1
+ Revision: 350114
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 2.00.0-2mdv2009.0
+ Revision: 220444
- rebuild

* Mon Mar 31 2008 Anssi Hannula <anssi@mandriva.org> 2.00.0-1mdv2008.1
+ Revision: 191181
- new version

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.52.0-5mdv2008.1
+ Revision: 182649
- provide enchant-dictionary

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.52.0-3mdv2007.0
+ Revision: 123363
- Import aspell-sk

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.52.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.52.0-2mdk
- rebuild for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.52.0-1mdk
- updated to 0.52.0

