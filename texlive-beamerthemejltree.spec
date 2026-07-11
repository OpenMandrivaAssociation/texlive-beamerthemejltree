%global tl_name beamerthemejltree
%global tl_revision 21977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Contributed beamer theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemeJLTree.sty
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemejltree.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A theme for beamer presentations.

