#!/bin/bash
# Author:  Alpha Eva <kaneawk AT gmail.com>
#
# Notes: OneinStack for CentOS/RedHat 6+ Debian 7+ and Ubuntu 12+
#
# Project home page:
#       https://oneinstack.com
#       https://github.com/oneinstack/oneinstack

installDepsDebian() {
  echo "${CMSG}Removing the conflicting packages...${CEND}"
  if [[ "${apache_option}" =~ ^[1-2]$ ]]; then
    killall apache2
    pkgList="apache2 apache2-doc apache2-utils apache2.2-common apache2.2-bin apache2-mpm-prefork apache2-doc apache2-mpm-worker php5 php5-common php5-cgi php5-cli php5-mysql php5-curl php5-gd"
    for Package in ${pkgList};do
      apt-get -y purge ${Package}
    done
    dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P
  fi

  if [[ "${db_option}" =~ ^[1-9]$|^1[0-3]$ ]]; then
    pkgList="mysql-client mysql-server mysql-common mysql-server-core-5.5 mysql-client-5.5 mariadb-client mariadb-server mariadb-common"
    for Package in ${pkgList};do
      apt-get -y purge ${Package}
    done
    dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P
  fi

  echo "${CMSG}Installing dependencies packages...${CEND}"
  apt-get -y update
  apt-get -y autoremove
  apt-get -yf install
  export DEBIAN_FRONTEND=noninteractive

  # critical security updates
  grep security /etc/apt/sources.list > /tmp/security.sources.list
  apt-get -y upgrade -o Dir::Etc::SourceList=/tmp/security.sources.list

  # Install needed packages
  case "${Debian_ver}" in
    [6,7])
      pkgList="debian-keyring debian-archive-keyring build-essential gcc g++ make cmake autoconf libjpeg8 libjpeg8-dev libjpeg-dev libpng12-0 libpng12-dev libpng3 libfreetype6 libfreetype6-dev libxml2 libxml2-dev zlib1g zlib1g-dev libc6 libc6-dev libc-client2007e-dev libglib2.0-0 libglib2.0-dev bzip2 libzip-dev libbz2-1.0 libncurses5 libncurses5-dev libaio1 libaio-dev numactl libreadline-dev curl libcurl3-gnutls libcurl4-gnutls-dev libcurl4-openssl-dev e2fsprogs libkrb5-3 libkrb5-dev libltdl-dev libidn11 libidn11-dev openssl libssl-dev libtool libevent-dev bison re2c libsasl2-dev libxslt1-dev libicu-dev locales libcloog-ppl0 patch vim zip unzip tmux htop bc dc expect libexpat1-dev rsync git lsof lrzsz iptables rsyslog cron logrotate ntpdate libsqlite3-dev psmisc wget sysv-rc ca-certificates"
      ;;
    8)
      pkgList="debian-keyring debian-archive-keyring build-essential gcc g++ make cmake autoconf libjpeg8 libjpeg62-turbo-dev libjpeg-dev libpng12-0 libpng12-dev libpng3 libfreetype6 libfreetype6-dev libxml2 libxml2-dev zlib1g zlib1g-dev libc6 libc6-dev libc-client2007e-dev libglib2.0-0 libglib2.0-dev bzip2 libzip-dev libbz2-1.0 libncurses5 libncurses5-dev libaio1 libaio-dev numactl libreadline-dev curl libcurl3-gnutls libcurl4-gnutls-dev libcurl4-openssl-dev e2fsprogs libkrb5-3 libkrb5-dev libltdl-dev libidn11 libidn11-dev openssl libssl-dev libtool libevent-dev bison re2c libsasl2-dev libxslt1-dev libxslt-dev libicu-dev locales libcloog-ppl0 patch vim zip unzip tmux htop bc dc expect libexpat1-dev rsync git lsof lrzsz iptables rsyslog cron logrotate ntpdate libsqlite3-dev psmisc wget sysv-rc ca-certificates"
      ;;
    9)
      pkgList="debian-keyring debian-archive-keyring build-essential gcc g++ make cmake autoconf libjpeg62-turbo-dev libjpeg-dev libpng-dev libfreetype6 libfreetype6-dev libxml2 libxml2-dev zlib1g zlib1g-dev libc6 libc6-dev libc-client2007e-dev libglib2.0-0 libglib2.0-dev bzip2 libzip-dev libbz2-1.0 libncurses5 libncurses5-dev libaio1 libaio-dev numactl libreadline-dev curl libcurl3-gnutls libcurl4-gnutls-dev libcurl4-openssl-dev e2fsprogs libkrb5-3 libkrb5-dev libltdl-dev libidn11 libidn11-dev openssl libssl-dev libtool libevent-dev bison re2c libsasl2-dev libxslt1-dev libicu-dev locales libcloog-ppl1 patch vim zip unzip tmux htop bc dc expect libexpat1-dev rsync git lsof lrzsz iptables rsyslog cron logrotate ntpdate libsqlite3-dev psmisc wget sysv-rc ca-certificates"
      ;;
    *)
      echo "${CFAILURE}Your system Debian ${Debian_ver} are not supported!${CEND}"
      kill -9 $$
      ;;
  esac
  for Package in ${pkgList}; do
    apt-get --no-install-recommends -y install ${Package}
  done
}

installDepsCentOS() {
  [ -e '/etc/yum.conf' ] && sed -i 's@^exclude@#exclude@' /etc/yum.conf
  # Uninstall the conflicting packages
  echo "${CMSG}Removing the conflicting packages...${CEND}"
  if [ "${CentOS_ver}" == '7' ]; then
    yum -y groupremove "Basic Web Server" "MySQL Database server" "MySQL Database client"
    systemctl mask firewalld.service
    if [ "${iptables_flag}" == 'y' ]; then
      yum -y install iptables-services
      systemctl enable iptables.service
      systemctl enable ip6tables.service
    fi
  elif [ "${CentOS_ver}" == '6' ]; then
    yum -y groupremove "FTP Server" "PostgreSQL Database client" "PostgreSQL Database server" "MySQL Database server" "MySQL Database client" "Web Server"
  elif [ "${CentOS_ver}" == '5' ]; then
    yum -y groupremove "FTP Server" "PostgreSQL Database" "MySQL Database" "Web Server"
  fi

  echo "${CMSG}Installing dependencies packages...${CEND}"
  # Install needed packages
  pkgList="deltarpm gcc gcc-c++ make cmake autoconf libjpeg libjpeg-devel libjpeg-turbo libjpeg-turbo-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel krb5-devel libc-client libc-client-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel libaio numactl numactl-libs readline-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5-devel libidn libidn-devel openssl openssl-devel libxslt-devel libicu-devel libevent-devel libtool libtool-ltdl bison gd-devel vim-enhanced pcre-devel zip unzip ntpdate sqlite-devel sysstat patch bc expect expat-devel rsync rsyslog git lsof lrzsz psmisc wget which libatomic"
  for Package in ${pkgList}; do
    yum -y install ${Package}
  done

  yum -y update bash openssl glibc

  # use gcc-4.4
  if [ -n "$(gcc --version | head -n1 | grep '4\.1\.')" ]; then
    yum -y install gcc44 gcc44-c++ libstdc++44-devel
    export CC="gcc44" CXX="g++44"
  fi
}

installDepsUbuntu() {
  # Uninstall the conflicting software
  echo "${CMSG}Removing the conflicting packages...${CEND}"
  if [[ "${apache_option}" =~ ^[1-2]$ ]]; then
    killall apache2
    pkgList="apache2 apache2-doc apache2-utils apache2.2-common apache2.2-bin apache2-mpm-prefork apache2-doc apache2-mpm-worker php5 php5-common php5-cgi php5-cli php5-mysql php5-curl php5-gd"
    for Package in ${pkgList};do
      apt-get -y purge ${Package}
    done
    dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P
  fi

  if [[ "${db_option}" =~ ^[1-9]$|^1[0-3]$ ]]; then
    pkgList="mysql-client mysql-server mysql-common mysql-server-core-5.5 mysql-client-5.5 mariadb-client mariadb-server mariadb-common"
    for Package in ${pkgList};do
      apt-get -y purge ${Package}
    done
    dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P
  fi

  echo "${CMSG}Installing dependencies packages...${CEND}"
  apt-get -y update
  apt-get -y autoremove
  apt-get -yf install
  export DEBIAN_FRONTEND=noninteractive

  # critical security updates
  grep security /etc/apt/sources.list > /tmp/security.sources.list
  apt-get -y upgrade -o Dir::Etc::SourceList=/tmp/security.sources.list

  # Install needed packages
  pkgList="debian-keyring debian-archive-keyring build-essential gcc g++ make cmake autoconf libjpeg8 libjpeg8-dev libpng12-0 libpng12-dev libpng3 libfreetype6 libfreetype6-dev libxml2 libxml2-dev zlib1g zlib1g-dev libc6 libc6-dev libc-client2007e-dev libglib2.0-0 libglib2.0-dev bzip2 libzip-dev libbz2-1.0 libncurses5 libncurses5-dev libaio1 libaio-dev numactl libreadline-dev curl libcurl3-gnutls libcurl4-gnutls-dev libcurl4-openssl-dev e2fsprogs libkrb5-3 libkrb5-dev libltdl-dev libidn11 libidn11-dev openssl libssl-dev libtool libevent-dev re2c libsasl2-dev libxslt1-dev libicu-dev libsqlite3-dev patch vim zip unzip tmux htop bc dc expect libexpat1-dev iptables rsyslog rsync git lsof lrzsz ntpdate psmisc wget sysv-rc"
  export DEBIAN_FRONTEND=noninteractive
  for Package in ${pkgList}; do
    apt-get --no-install-recommends -y install ${Package}
  done

  if [[ "${Ubuntu_ver}" =~ ^14$|^15$ ]]; then
    apt-get -y install libcloog-ppl1
    apt-get -y remove bison
    ln -sf /usr/include/freetype2 /usr/include/freetype2/freetype
  elif [ "${Ubuntu_ver}" == "13" ]; then
    apt-get -y install bison libcloog-ppl1
  elif [ "${Ubuntu_ver}" == "12" ]; then
    apt-get -y install bison libcloog-ppl0
  else
    apt-get -y install bison libcloog-ppl1
  fi
}

installDepsBySrc() {
  pushd ${oneinstack_dir}/src > /dev/null
  if [ "${OS}" == 'Ubuntu' ]; then
    if [[ "${Ubuntu_ver}" =~ ^14$|^15$ ]]; then
      # Install bison on ubt 14.x 15.x
      tar xzf bison-${bison_ver}.tar.gz
      pushd bison-${bison_ver} > /dev/null
      ./configure
      make -j ${THREAD} && make install
      popd > /dev/null
      rm -rf bison-${bison_ver}
    fi
  elif [ "${OS}" == 'CentOS' ]; then
    # Install tmux
    if ! command -v tmux >/dev/null 2>&1; then
      # Install libevent first
      tar xzf libevent-${libevent_ver}.tar.gz
      pushd libevent-${libevent_ver} > /dev/null
      ./configure
      make -j ${THREAD} && make install
      popd > /dev/null
      rm -rf libevent-${libevent_ver}

      tar xzf tmux-${tmux_ver}.tar.gz
      pushd tmux-${tmux_ver} > /dev/null
      CFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib" ./configure
      make -j ${THREAD} && make install
      unset LDFLAGS
      popd > /dev/null
      rm -rf tmux-${tmux_ver}

      if [ "${OS_BIT}" == "64" ]; then
        ln -s /usr/local/lib/libevent-2.0.so.5 /usr/lib64/libevent-2.0.so.5
      else
        ln -s /usr/local/lib/libevent-2.0.so.5 /usr/lib/libevent-2.0.so.5
      fi
    fi

    # install htop
    if ! command -v htop >/dev/null 2>&1; then
      tar xzf htop-${htop_ver}.tar.gz
      pushd htop-${htop_ver} > /dev/null
      ./configure
      make -j ${THREAD} && make install
      popd > /dev/null
      rm -rf htop-${htop_ver}
    fi

    # upgrade autoconf for CentOS6
    [ "${CentOS_ver}" == '6' ] && rpm -Uvh autoconf-2.69-12.2.noarch.rpm
  else
    echo "No need to install software from source packages."
  fi

  if command -v lsof >/dev/null 2>&1; then
    echo 'already initialize' > ~/.oneinstack
  else
    echo "${CFAILURE}${PM} config error parsing file failed${CEND}"
    kill -9 $$
  fi

  popd > /dev/null
}
