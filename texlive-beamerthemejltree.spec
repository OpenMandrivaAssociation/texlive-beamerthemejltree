# revision 21977
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/themes/beamerthemeJLTree.sty
# catalog-date 2010-07-13 19:58:19 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-beamerthemejltree
Version:	1.1
Release:	2
Summary:	Contributed beamer theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemeJLTree.sty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemejltree.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A theme for beamer presentations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamerthemejltree/beamerthemeJLTree.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
