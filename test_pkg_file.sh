MODULE_PARAMS="state=present"
MODULE_PARAMS="$MODULE_PARAMS pkg_name=com.oracle.jdk7u25"
MODULE_PARAMS="$MODULE_PARAMS pkg_version=1.1"
MODULE_PARAMS="$MODULE_PARAMS archive_type=dmg"
MODULE_PARAMS="$MODULE_PARAMS src=/tmp/jdk7.dmg"
MODULE_PARAMS="$MODULE_PARAMS archive_path='JDK 7 Update 25.pkg'"
#echo $MODULE_PARAMS
~/workspace/32degrees/ansible/hacking/test-module -m share/library/mac_pkg -a "$MODULE_PARAMS"
