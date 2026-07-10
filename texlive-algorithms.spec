%global tl_name algorithms
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	A suite of tools for typesetting algorithms in pseudo-code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/algorithms
License:	lgpl2.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/algorithms.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Consists of two environments: algorithm and algorithmic. The algorithm
package defines a floating algorithm environment designed to work with
the algorithmic style. Within an algorithmic environment a number of
commands for typesetting popular algorithmic constructs are available.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/algorithms
%dir %{_datadir}/texmf-dist/source/latex/algorithms
%dir %{_datadir}/texmf-dist/tex/latex/algorithms
%doc %{_datadir}/texmf-dist/doc/latex/algorithms/COPYING
%doc %{_datadir}/texmf-dist/doc/latex/algorithms/README
%doc %{_datadir}/texmf-dist/doc/latex/algorithms/THANKS
%doc %{_datadir}/texmf-dist/doc/latex/algorithms/algorithms.pdf
%doc %{_datadir}/texmf-dist/source/latex/algorithms/algorithms.dtx
%doc %{_datadir}/texmf-dist/source/latex/algorithms/algorithms.ins
%{_datadir}/texmf-dist/tex/latex/algorithms/algorithm.sty
%{_datadir}/texmf-dist/tex/latex/algorithms/algorithmic.sty
