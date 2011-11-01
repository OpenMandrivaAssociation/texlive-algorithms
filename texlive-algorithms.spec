Name:		texlive-algorithms
Version:	0.1
Release:	1
Summary:	A suite of tools for typesetting algorithms in pseudo-code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/algorithms
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Consists of two environments: algorithm and algorithmic. The
algorithm package defines a floating algorithm environment
designed to work with the algorithmic style. Within an
algorithmic environment a number of commands for typesetting
popular algorithmic constructs are available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
