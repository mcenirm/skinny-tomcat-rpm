#!/bin/bash

Usage () {
  cat <<EOF
Usage: $0 ...somewhere.../apache-tomcat-8.0.xx.tar.gz
Adds symlinks under rpmbuild _topdir
EOF
}

case $# in
  1) _dist=${1} ;;
  *) Usage >&2 ; exit 1 ;;
esac

_topdir=$( rpm --eval '%{_topdir}' )
if ! [ -d "${_topdir}" ] ; then
  echo >&2 'Missing rpmbuild _topdir. Did you run rpmdev-setuptree?'
  exit 2
fi

_here=$( cd $( dirname "$0" ) && /bin/pwd )
_there=$( cd $( dirname "${_dist}" ) && /bin/pwd )/${_dist##*/}

ln -v -s "${_there}" "${_here}/SOURCES/tomcat."{init,logrotate,sysconfig} "${_topdir}/SOURCES/"
ln -v -s "${_here}/SPECS/tomcat.spec" "${_topdir}/SPECS/"

