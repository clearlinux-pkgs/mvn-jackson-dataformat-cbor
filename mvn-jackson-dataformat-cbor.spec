#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jackson-dataformat-cbor
Version  : 2.6.7
Release  : 3
URL      : https://github.com/FasterXML/jackson-dataformat-cbor/archive/jackson-dataformat-cbor-2.6.7.tar.gz
Source0  : https://github.com/FasterXML/jackson-dataformat-cbor/archive/jackson-dataformat-cbor-2.6.7.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.jar
Source2  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.pom
Source3  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.jar
Source4  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.pom
Source5  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.jar
Source6  : https://repo.maven.apache.org/maven2/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jackson-dataformat-cbor-data = %{version}-%{release}
Requires: mvn-jackson-dataformat-cbor-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
## Overview
[Jackson](/FasterXML/jackson) (Java) data format module that supports reading and writing
[CBOR](https://www.rfc-editor.org/info/rfc7049)
("Concise Binary Object Representation") encoded data.
Module extends standard Jackson streaming API (`JsonFactory`, `JsonParser`, `JsonGenerator`), and as such works seamlessly with all the higher level data abstractions (data binding, tree model, and pluggable extensions).

%package data
Summary: data components for the mvn-jackson-dataformat-cbor package.
Group: Data

%description data
data components for the mvn-jackson-dataformat-cbor package.


%package license
Summary: license components for the mvn-jackson-dataformat-cbor package.
Group: Default

%description license
license components for the mvn-jackson-dataformat-cbor package.


%prep
%setup -q -n jackson-dataformat-cbor-jackson-dataformat-cbor-2.6.7

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jackson-dataformat-cbor
cp src/main/resources/META-INF/LICENSE %{buildroot}/usr/share/package-licenses/mvn-jackson-dataformat-cbor/src_main_resources_META-INF_LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.6/jackson-dataformat-cbor-2.6.6.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.6.7/jackson-dataformat-cbor-2.6.7.pom
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.jar
/usr/share/java/.m2/repository/com/fasterxml/jackson/dataformat/jackson-dataformat-cbor/2.8.1/jackson-dataformat-cbor-2.8.1.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jackson-dataformat-cbor/src_main_resources_META-INF_LICENSE
