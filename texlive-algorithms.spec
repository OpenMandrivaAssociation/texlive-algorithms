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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Consists of two environments: algorithm and algorithmic. The algorithm
package defines a floating algorithm environment designed to work with
the algorithmic style. Within an algorithmic environment a number of
commands for typesetting popular algorithmic constructs are available.

