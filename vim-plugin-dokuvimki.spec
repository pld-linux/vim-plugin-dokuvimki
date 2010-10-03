# TODO
# - how to express dep for vim with python?
%define		plugin	dokuvimki
Summary:	Vim plugin: NAME
Name:		vim-plugin-%{plugin}
Version:	20100806
Release:	0.1
License:	GPL v2
Group:		Applications/Editors/Vim
Source0:	http://cloud.github.com/downloads/chimeric/dokuvimki/dokuvimki.tgz
# Source0-md5:	7d6ace736da52213b76dd64725ff6a32
URL:		http://www.chimeric.de/projects/dokuwiki/dokuvimki
Requires:	vim-rt >= 4:7.2.170
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
DokuVimKi is a Vim plugin which allows you to edit wiki:DokuWiki pages
of DokuWikis XML-RPC interface.

It also does syntax highlighting for DokuWiki syntax.

%prep
%setup -qc
rm COPYING

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a . $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_vimdatadir}/doc/*.txt
%{_vimdatadir}/plugin/*.vim
%{_vimdatadir}/syntax/*.vim
