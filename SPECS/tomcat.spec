# To Build:
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# git clone https://github.com/xflin/skinny-tomcat-rpm.git
# cd ~/skinny-tomcat-rpm/SOURCES && wget http://www.motorlogy.com/apache/tomcat/tomcat-8/v8.0.5/bin/apache-tomcat-8.0.5.tar.gz
# ln -s ~/rpmbuild ./skinny-tomcat-rpm
# rpmbuild -bb ~/rpmbuild/SPECS/tomcat.spec

%define __jar_repack %{nil}
%define tomcat_home /opt/tomcat
%define tomcat_group tomcat
%define tomcat_user tomcat

Summary:    Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies.
Name:       tomcat
Version:    8.0.5
BuildArch:  noarch
Release:    1
License:    Apache Software License
Group:      Networking/Daemons
URL:        http://tomcat.apache.org/
Source0:    apache-tomcat-%{version}.tar.gz
Source1:    %{name}.init
Source2:    %{name}.sysconfig
Source3:    %{name}.logrotate
Requires:   jre >= 1.7
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Oracle under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be
a collaboration of the best-of-breed developers from around the world.
We invite you to participate in this open development project. To
learn more about getting involved, click here.

This package contains the base tomcat installation that depends on Oracle's Java or openjdk JPP packages.

%prep
%setup -q -n apache-tomcat-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{tomcat_home}/
cp -R * %{buildroot}/%{tomcat_home}/

# Remove all webapps
rm -rf %{buildroot}/%{tomcat_home}/webapps/ROOT/*
rm -rf %{buildroot}/%{tomcat_home}/webapps/docs
rm -rf %{buildroot}/%{tomcat_home}/webapps/examples
rm -rf %{buildroot}/%{tomcat_home}/webapps/host-manager
rm -rf %{buildroot}/%{tomcat_home}/webapps/manager

# Put logging in /var/log and link back.
rm -rf %{buildroot}/%{tomcat_home}/logs
install -d -m 755 %{buildroot}/var/log/%{name}/
cd %{buildroot}/%{tomcat_home}/
ln -s /var/log/%{name}/ logs
cd -

# Put conf in /etc/ and link back.
install -d -m 755 %{buildroot}/%{_sysconfdir}
mv %{buildroot}/%{tomcat_home}/conf %{buildroot}/%{_sysconfdir}/%{name}
cd %{buildroot}/%{tomcat_home}/
ln -s %{_sysconfdir}/%{name} conf
cd -

# Drop init script
install -d -m 755 %{buildroot}/%{_initrddir}
install    -m 755 %_sourcedir/%{name}.init %{buildroot}/%{_initrddir}/%{name}

# Drop sysconfig script
install -d -m 755 %{buildroot}/%{_sysconfdir}/sysconfig/
install    -m 644 %_sourcedir/%{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

# Drop logrotate script
install -d -m 755 %{buildroot}/%{_sysconfdir}/logrotate.d
install    -m 644 %_sourcedir/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

%clean
rm -rf %{buildroot}

%pre
getent group %{tomcat_group} >/dev/null || groupadd -r %{tomcat_group}
getent passwd %{tomcat_user} >/dev/null || /usr/sbin/useradd --comment "Tomcat Daemon User" --shell /bin/bash -M -r -g %{tomcat_group} --home %{tomcat_home} %{tomcat_user}

%files
%defattr(-,%{tomcat_user},%{tomcat_group})
%{tomcat_home}/*
/var/log/%{name}/
%defattr(-,root,root)
%{_initrddir}/%{name}
%{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*

%post
chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  service %{name} stop > /dev/null 2>&1
  chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
  service %{name} condrestart >/dev/null 2>&1
fi

%changelog
* Mon Apr 28 2014 Xiaofeng Lin <xflin>
* Thu Apr 10 2014 Brian Dwyer <bdwyertech>
* Sat Feb 15 2014 Michael McGraw-Herdeg <mherdeg@mit.edu>
- 7.0.50
* Tue Jan 7 2014 Michael McGraw-Herdeg <mherdeg@mit.edu>
- 7.0.47

* Mon Jul 1 2013 Nathan Milford <nathan@milford.io>
- 7.0.41

