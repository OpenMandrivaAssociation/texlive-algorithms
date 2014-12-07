# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/algorithms
# catalog-date 2009-08-25 14:02:57 +0200
# catalog-license lgpl
# catalog-version 0.1
Name:		texlive-algorithms
Version:	0.1
Release:	9
Summary:	A suite of tools for typesetting algorithms in pseudo-code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algorithms
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Consists of two environments: algorithm and algorithmic. The
algorithm package defines a floating algorithm environment
designed to work with the algorithmic style. Within an
algorithmic environment a number of commands for typesetting
popular algorithmic constructs are available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/algorithms/algorithm.sty
%{_texmfdistdir}/tex/latex/algorithms/algorithmic.sty
%doc %{_texmfdistdir}/doc/latex/algorithms/COPYING
%doc %{_texmfdistdir}/doc/latex/algorithms/README
%doc %{_texmfdistdir}/doc/latex/algorithms/THANKS
%doc %{_texmfdistdir}/doc/latex/algorithms/algorithms.pdf
#- source
%doc %{_texmfdistdir}/source/latex/algorithms/algorithms.dtx
%doc %{_texmfdistdir}/source/latex/algorithms/algorithms.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 749161
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 717813
- texlive-algorithms
- texlive-algorithms
- texlive-algorithms
- texlive-algorithms
- texlive-algorithms

