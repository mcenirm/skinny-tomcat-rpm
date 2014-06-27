skinny-tomcat-rpm
=================

An RPM spec file to create a "skinny" Tomcat 8 RPM. This is a very opinionated
Tomcat RPM meant to be used in so-called "production" deployments.

* It removes all webapps: docs, examples, manager, host-manager, and ROOT.
* It removes logging configurations for console, manager, and host-manager.
* It depends on Oracle JRE 7+ (not JDK, not even OpenJDK).
* It moves installation base (from /opt/tomcat) to /usr/lib/tomcat.
* It places webapps, temp, and work under /var/lib/tomcat (with links from /usr/lib/tomcat).

Prebuild RPM
------------

[tomcat-8.0.9-1.noarch.rpm](tomcat-8.0.9-1.noarch.rpm)

To Build
--------

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`git clone https://github.com/xflin/skinny-tomcat-rpm.git`

`ln -s ./skinny-tomcat-rpm ~/rpmbuild`

`cd ~/rpmbuild/SOURCES && wget http://www.motorlogy.com/apache/tomcat/tomcat-8/v8.0.9/bin/apache-tomcat-8.0.9.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/tomcat.spec`
