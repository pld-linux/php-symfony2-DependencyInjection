%define		pearname	DependencyInjection
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 DependencyInjection Component
Name:		php-symfony2-DependencyInjection
Version:	2.3.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	a5421c960e7c087752383721f15060df
URL:		http://symfony.com/doc/current/components/dependency_injection/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Suggests:	php-symfony2-Config
Suggests:	php-symfony2-Yaml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Dependency Injection component allows you to standardize and
centralize the way objects are constructed in your application.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/DependencyInjection
%{php_pear_dir}/Symfony/Component/DependencyInjection/*.php
%{php_pear_dir}/Symfony/Component/DependencyInjection/Compiler
%{php_pear_dir}/Symfony/Component/DependencyInjection/Dumper
%{php_pear_dir}/Symfony/Component/DependencyInjection/Exception
%{php_pear_dir}/Symfony/Component/DependencyInjection/Extension
%{php_pear_dir}/Symfony/Component/DependencyInjection/LazyProxy
%{php_pear_dir}/Symfony/Component/DependencyInjection/Loader
%{php_pear_dir}/Symfony/Component/DependencyInjection/ParameterBag
