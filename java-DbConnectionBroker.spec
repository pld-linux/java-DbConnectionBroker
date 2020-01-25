%define		srcname		DbConnectionBroker
Summary:	%{srcname} - database connection pool management
Summary(pl.UTF-8):	%{srcname} - zarządzanie pulą połączeń bazodanowych
Name:		java-%{srcname}
Version:	1.0.13
Release:	5
License:	OSS
Group:		Development/Languages/Java
Source0:	ftp://javaexchange.com/javaexchange/%{srcname}%{version}.tar
# Source0-md5:	9e433e92a3b613678c8f8e49d299e864
Source1:	ftp://javaexchange.com/javaexchange/%{srcname}.java
# Source1-md5:	215ef43a308e40a38fb12d749a601a71
URL:		http://www.javaexchange.com/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Requires:	jre
Provides:	DbConnectionBroker
Obsoletes:	DbConnectionBroker
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DbConnectionBroker is a pure Java package for handling multiple
concurrent database connections. DbConnectionBroker creates a broker
with a very simple interface for handing out and returning database
connections from a configurable pool of connections. The Broker
creates a dynamic pool of connections and manages them for you with a
background housekeeping thread.

%description -l pl.UTF-8
DbConnectionBroker jest napisanym w Javie pakietem do obsługi wielu
konkurencyjnych połączeń z bazą danych. DbConnectionBroker tworzy
pośrednik z bardzo prostym interfejsem do wydawania i zwracania
połączeń bazodanowych przynależnych do konfigurowalnej puli połączeń.
Pośrednik tworzy dynamiczną pulę połączeń i zarządza nią za pomocą
działającego w tle wątku porządkującego.

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%package demo
Summary:	Demo for %{srcname}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{srcname}
Group:		Documentation
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{srcname}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{srcname}.

%prep
%setup -qc
cp %{SOURCE1} com/javaexchange/%{srcname}
rm -f com/javaexchange/%{srcname}/%{srcname}.class

%build
%javac com/javaexchange/%{srcname}/%{srcname}.java
%jar cvf %{srcname}.jar com/javaexchange/%{srcname}/%{srcname}.class

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{srcname}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{srcname}-%{version}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{srcname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -sf %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{srcname}-%{version}
