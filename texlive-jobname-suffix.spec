%global tl_name jobname-suffix
%global tl_revision 64797

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Compile differently based on the filename
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jobname-suffix
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jobname-suffix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jobname-suffix.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows to compile a document differently depending on the
portion of the document's file name (internally, the \jobname) that
comes after the first "-" character. This allows one to have one source
file and multiple links to this source file that each compile
differently.

