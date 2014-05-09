skinny-tomcat-rpm
=================

An RPM spec file to create a "skinny" Tomcat 8 RPM.

* It removes all webapps contents and keeps only an empty ROOT.
* It depends on Oracle JRE 7+.

To Build:

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`git clone https://github.com/xflin/skinny-tomcat-rpm.git`

`cd ~/skinny-tomcat-rpm/SOURCES && wget http://www.motorlogy.com/apache/tomcat/tomcat-8/v8.0.5/bin/apache-tomcat-8.0.5.tar.gz`

`ln -s ./skinny-tomcat-rpm ~/rpmbuild`

`rpmbuild -bb ~/rpmbuild/SPECS/tomcat.spec`
