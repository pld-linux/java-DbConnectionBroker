Summary:	DbConnectionBroker - database connection pool management
Summary(pl.UTF-8):	DbConnectionBroker - zarz±dzanie pul± po³±czeñ bazodanowych
Name:		DbConnectionBroker
Version:	1.0.13
Release:	1
License:	OSS
Group:		Development/Languages/Java
Source0:	ftp://javaexchange.com/javaexchange/%{name}%{version}.tar
# Source0-md5:	9e433e92a3b613678c8f8e49d299e864
Source1:	ftp://javaexchange.com/javaexchange/%{name}.java
# Source1-md5:	215ef43a308e40a38fb12d749a601a71
URL:		http://www.javaexchange.com/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre
Obsoletes:	java-DbConnectionBroker
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DbConnectionBroker is a pure Java package for handling multiple
concurrent database connections. DbConnectionBroker creates a broker
with a very simple interface for handing out and returning database
connections from a configurable pool of connections. The Broker
creates a dynamic pool of connections and manages them for you with a
background housekeeping thread.

%description -l pl.UTF-8
DbConnectionBroker jest napisanym w Javie pakietem do obs³ugi wielu
konkurencyjnych po³±czeñ z baz± danych. DbConnectionBroker tworzy
po¶rednik z bardzo prostym interfejsem do wydawania i zwracania
po³±czeñ bazodanowych przynale¿nych do konfigurowalnej puli po³±czeñ.
Po¶rednik tworzy dynamiczn± pulê po³±czeñ i zarz±dza ni± za pomoc±
dzia³aj±cego w tle w±tku porz±dkuj±cego.

%package javadoc
Summary:	Online manual for DbConnectionBroker
Summary(pl.UTF-8):	Dokumentacja online do DbConnectionBroker
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for DbConnectionBroker.

%description -l pl.UTF-8 javadoc
Dokumentacja do DbConnectionBroker.

%prep
%setup -qc
cp %{SOURCE1} com/javaexchange/dbConnectionBroker
rm -f com/javaexchange/dbConnectionBroker/DbConnectionBroker.class

%build
%javac com/javaexchange/dbConnectionBroker/DbConnectionBroker.java
jar cvf DbConnectionBroker.jar com/javaexchange/dbConnectionBroker/DbConnectionBroker.class

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
cp -a DbConnectionBroker.jar $RPM_BUILD_ROOT%{_javadir}/DbConnectionBroker-%{version}.jar
ln -s DbConnectionBroker-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/DbConnectionBroker.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
