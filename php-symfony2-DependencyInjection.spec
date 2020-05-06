%define		package	DependencyInjection
%define		php_min_version 5.3.9
Summary:	Symfony2 DependencyInjection Component
Name:		php-symfony2-DependencyInjection
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	4abb0f37f8159cc686621c08871008bb
URL:		https://symfony.com/doc/2.8/components/dependency_injection.htmlindex.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-ProxyManagerBridge
Suggests:	php-symfony2-Yaml
Conflicts:	php-symfony2-ExpressionLanguage < 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Dependency Injection component allows you to standardize and
centralize the way objects are constructed in your application.

%prep
%setup -q -n dependency-injection-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/DependencyInjection
%{php_data_dir}/Symfony/Component/DependencyInjection/*.php
%{php_data_dir}/Symfony/Component/DependencyInjection/Compiler
%{php_data_dir}/Symfony/Component/DependencyInjection/Dumper
%{php_data_dir}/Symfony/Component/DependencyInjection/Exception
%{php_data_dir}/Symfony/Component/DependencyInjection/Extension
%{php_data_dir}/Symfony/Component/DependencyInjection/LazyProxy
%{php_data_dir}/Symfony/Component/DependencyInjection/Loader
%{php_data_dir}/Symfony/Component/DependencyInjection/ParameterBag
