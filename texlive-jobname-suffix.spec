Name:		texlive-jobname-suffix
Version:	64797
Release:	1
Summary:	Compile differently based on the filename
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jobname-suffix
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jobname-suffix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jobname-suffix.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to compile a document differently depending
on the portion of the document's file name (internally, the
\jobname) that comes after the first "-" character. This allows
one to have one source file and multiple links to this source
file that each compile differently.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jobname-suffix
%doc %{_texmfdistdir}/doc/latex/jobname-suffix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
