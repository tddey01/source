#!/usr/bin/env bash
#!/bin/bash
#########################
#script:redis-cluster
#version:0.1
#name:tddey
#########################

checkDownload() {
          # redis-server
   if [ "${redis_flag}" == 'y' ]; then
        echo "Download redis-server..."
        src_url=http://download.redis.io/releases/redis-${redis_ver}.tar.gz && Download_src
        if [ "${PM}" == 'yum' ]; then
        echo "Download start-stop-daemon.c for CentOS..."
        src_url=${mirrorLink}/start-stop-daemon.c && Download_src
    fi
   fi
    }
ps aux | grep redis-server | grep -v grep  | grep -v redis-cluster
if [ X$? = "X0" ]
    then
        echo "ERROR: Host is installed redis-cluster"
    exit 101
fi

KERNEL_VERION_1=`uname -r | awk -F"-" '{print \$1}'`
if [ ${KERNEL_VERION_1} = '2.6.18' ]
    then
        OS_VERSION="RHEL5"
elif [ ${KERNEL_VERION_1} = '2.6.32' ]
    then
        OS_VERSION="RHEL6"
elif [ ${KERNEL_VERION_1} = '3.10.0' ]
    then
        OS_VERSION="RHEL7"
else
    echo "This script is not suitable for the running os version."
    exit 2
fi


install_yum () {
	echo "开始安装redis集群依赖ruby库,请稍等..."
	#解决yum update时候出现Another app is currently holding the yum lock
	rm -rf /var/run/yum.pid && rm -rf /var/lib/rpm/.rpm.lock
	rm -rf time.out
	sleep 5s
	#搭建redis集群需要的库
    yum install wget  gcc g++ gcc-c++ make ruby ruby-devel rubygems rpm-build -y
    gem install redis
}
getGetway () {
	route -n | grep UG | gawk '{print $2}'
	}
getEth () {
	route -n | grep $(getGetway) | gawk '{print $8}'
	}
getIP () {
	ifconfig $(getEth) | grep 'inet addr' | awk '{print $2}' | awk -F: '{print $2}'
    }

getver () {
	redis-cli -v | gawk '{print $2}'
}
install ()
{
	if redis-cli -v > /dev/null 2>&1
	then
		echo -e "$WHITE 当前系统已安装redis环境,版本号:$(getver)${RES}"
	else
		#jdk安装文件存在下一步安装操作
		if [ -e redis-*.tar.gz ]
		    then
			    echo -e "$WHITE 开始安装redis,请稍候...${RES}"
			    #首先删除安装目录下所有以jdk1.开头的文件夹
			    rm -rf /usr/local/redis.*
			    #然后解压tar.gz包到安装目录下
			    tar -zxvf redis-*.tar.gz -C /usr/local
			    name1=`ls /usr/local | grep redis-`
			    cd /usr/local/$name1
			    pwd
			    make && make install
			    echo -e "$WHITE redis安装完成!${RES}"
		else
			echo -e "${RED_COLOR} 安装目录下redis安装文件不存在,请上传该文件到此目录下！${RES}"
		fi
	fi
}
redisPath=/usr/local/redis-cluster
mkdieFile () {
	[ -d $redisPath ] && rm -rf $redisPath
	mkdir $redisPath
	echo -e "请选择创建redis节点数量:"
	while [ 1 = 1 ]
	do
		read NO
		    if  [[ -n "$NO" && "$NO" -gt 0 ]]
		        then
			        cd $redisPath
			        while(( ${NO} >= 1))
			            do
				            mkdir redis$NO
				            NO=$(($NO-1))
			            done
			    break
		    else
			    echo -e "输入有误,请输入正确的数字:"
		fi
	done
}
createColony () {
	#redis目录名称
	name=`ls /usr/local | grep redis-5`
	[ ! -f /usr/local/$name/redis.conf  ] && echo "redis.conf文件不存在,请检查redis是否安装成功!!" && exit 1
	[ ! -f /usr/local/$name/src/redis-trib.rb  ] && echo "redis-trib.rb文件不存在,请检查redis是否安装成功!!" && exit 1
	mkdieFile
	#拷贝redis.conf文件
	cp -rf /usr/local/$name/src/redis-trib.rb /usr/local/redis-cluster
	port=7000
	for page in `ls /usr/local/redis-cluster`
	do
		if [ -d $page ]
		then
			cp -rf /usr/local/$name/redis.conf $page
			sed -i "s/^daemonize no/daemonize yes/" $page/redis.conf
			sed -i "s/^# cluster-enabled yes/cluster-enabled yes/" $page/redis.conf
			sed -i "s/^port 6379/port $port/" $page/redis.conf
			echo $(getIP):$port >> $redisPath/prot.info
			port=$(($port+1))

		fi
	done
	echo "redis.conf文件修改成功,开始启动redis节点,请稍等..."
	startColony
	[ $? -eq 0 ] && echo "redis节点启动成功,开始创建redis集群!"
	cd  $redisPath
	install_yum
	./redis-trib.rb  create  --replicas  1  `cat  /usr/local/redis-cluster/prot.info`
	rm -rf /usr/local/redis-cluster/prot.info
	[ $? -eq 0 ] && echo "redis集群创建成功."
}

startColony () {

	for page1 in `ls /usr/local/redis-cluster`
	do
		if [ -d /usr/local/redis-cluster/$page1 ]
		then
			cd /usr/local/redis-cluster/$page1
			redis-server redis.conf
		fi
	done
}
stopColony () {
	#杀死节点进程
	killall redis-server > /dev/null
	for page1 in `ls /usr/local/redis-cluster`
	do
		if [ -d /usr/local/redis-cluster/$page1 ]
		then
			cd /usr/local/redis-cluster/$page1
			rm -rf dump.rdb
			rm -rf nodes.conf
		fi
	done

}
uninstall () {
	echo  "开始卸载redis,请稍等...."
	stopColony
	rm -rf /usr/local/bin/redis*
	name2=`ls /usr/local | grep redis-`
	rm -rf $name2
	rm -rf $redisPath
	source /etc/profile
	echo  "redis卸载成功."
}
#funcotion install(){
#
#    }

if [ "$1" = "uninstall" ]; then
	uninstall
#覆盖安装,即先卸载,后重新安装
elif [ "$1" = "replace" ]; then
	uninstall
	sleep 5
	install
	createColony
elif [ "$1" = "install" ]; then
	install
	createColony
elif [ "$1" = "stop" ]; then
	stopColony
elif [ "$1" = "start" ]; then
	startColony
fi
