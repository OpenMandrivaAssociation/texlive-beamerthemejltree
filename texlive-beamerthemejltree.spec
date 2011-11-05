# revision 21977
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/themes/beamerthemeJLTree.sty
# catalog-date 2010-07-13 19:58:19 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-beamerthemejltree
Version:	1.1
Release:	1
Summary:	Contributed beamer theme
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemeJLTree.sty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemejltree.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
A theme for beamer presentations.

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
%{_texmfdistdir}/tex/latex/beamerthemejltree/beamerthemeJLTree.sty
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
