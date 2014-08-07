%define		pearname	DependencyInjection
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 DependencyInjection Component
Name:		php-symfony2-DependencyInjection
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	8657e364dcacef18b1bcf2096e7e2885
URL:		http://symfony.com/doc/2.4/components/dependency_injection/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-ProxyManagerBridge
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Dependency Injection component allows you to standardize and
centralize the way objects are constructed in your application.

%prep
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/DependencyInjection
%{php_pear_dir}/Symfony/Component/DependencyInjection/*.php
%{php_pear_dir}/Symfony/Component/DependencyInjection/Compiler
%{php_pear_dir}/Symfony/Component/DependencyInjection/Dumper
%{php_pear_dir}/Symfony/Component/DependencyInjection/Exception
%{php_pear_dir}/Symfony/Component/DependencyInjection/Extension
%{php_pear_dir}/Symfony/Component/DependencyInjection/LazyProxy
%{php_pear_dir}/Symfony/Component/DependencyInjection/Loader
%{php_pear_dir}/Symfony/Component/DependencyInjection/ParameterBag
