#!/bin/bash
src=/home/user/www                           # 需要同步的源路径
des=/var/www                            # 目标服务器上 rsync --daemon 发布的名称，rsync --daemon这里就不做介绍了，网上搜一下，比较简单。
inotifywait_path=/home/user
rsync_path=/usr/bin
chmod 777 ${inotifywait_path}/inotifywait
chmod 777 ${rsync_path}/rsync
${inotifywait_path}/inotifywait -mrq --format  '%Xe %w%f' -e open,modify,create,delete,close_write,move ${des}/ | while read file         # 把监控到有发生更改的"文件路径列表"循环
do
        INO_EVENT=$(echo $file | awk '{print $1}')      # 把inotify输出切割 把事件类型部分赋值给INO_EVENT
        INO_FILE=$(echo $file | awk '{print $2}')       # 把inotify输出切割 把文件路径部分赋值给INO_FILE
	if [[ $INO_EVENT =~ 'CREATE' ]] || [[ $INO_EVENT =~ 'MODIFY' ]] || [[ $INO_EVENT =~ 'CLOSE_WRITE' ]] || [[ $INO_EVENT =~ 'MOVED_TO' ]]||[[ $INO_EVENT =~ 'DELETE' ]] || [[ $INO_EVENT =~ 'MOVED_FROM' ]];then #||[[ $INO_EVENT =~ 'ATTRIB' ]]||[[ $INO_EVENT =~ 'OPEN' ]]
        	echo "-------------------------------$(date)------------------------------------"
        	echo "inotify:"$file
		if [[ -a $INO_FILE ]]; then
			dir_des=$(dirname $INO_FILE)
			if [ $dir_des = $des ]; then
				dir_src=$src
			else
				dir_src=$src/${dir_des:${#des}+1}
			fi
			echo "rsync target:"$dir_src
			echo "${rsync_path}/rsync -avzc --delete  ${dir_src}/ ${dir_des}/"
        		${rsync_path}/rsync -avzc --delete  ${dir_src}/ ${dir_des}/
		fi
	fi
done
