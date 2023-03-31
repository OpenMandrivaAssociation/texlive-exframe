Name:		texlive-exframe
Version:	53911
Release:	2
Summary:	Framework for exercise problems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exframe
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exframe.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exframe.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exframe.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX2e package provides a general purpose framework to
describe and typeset exercises and exam questions along with
their solutions. The package features mechanisms to hide or
postpone solutions, to assign and handle points, to collect
problems on exercise sheets, to store and use metadata, and to
implement a consistent numbering. It also provides a very
flexible interface for configuring and customising the
formatting, layout, and representation of the exercise content.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/exframe
%{_texmfdistdir}/tex/latex/exframe
%doc %{_texmfdistdir}/doc/latex/exframe

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
