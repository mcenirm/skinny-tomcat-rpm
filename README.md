skinny-tomcat-rpm
=================

An RPM spec file to create a "skinny" Tomcat 8 RPM.

* It removes all webapps: docs, examples, manager, host-manager.
* It removes ROOT webapp contents and keeps only an empty ROOT directory.
* It removes logging configurations for console, manager, and host-manager.
* It depends on Oracle JRE 7+.

To Build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`git clone https://github.com/xflin/skinny-tomcat-rpm.git`

`ln -s ./skinny-tomcat-rpm ~/rpmbuild`

`cd ~/rpmbuild/SOURCES && wget http://www.motorlogy.com/apache/tomcat/tomcat-8/v8.0.5/bin/apache-tomcat-8.0.5.tar.gz`

`rpmbuild -bb ~/rpmbuild/SPECS/tomcat.spec`
