MODULE_PARAMS="pkg_name=com.oracle.jdk7u25"
MODULE_PARAMS="$MODULE_PARAMS pkg_version=1.1x"
MODULE_PARAMS="$MODULE_PARAMS url=https://edelivery.oracle.com/otn-pub/java/jdk/7u25-b15/jdk-7u25-macosx-x64.dmg"
MODULE_PARAMS="$MODULE_PARAMS curl_opts='--cookie gpw_e24=http%3A%2F%2Fwww.oracle.com'"
#MODULE_PARAMS="$MODULE_PARAMS dest=jdk7.dmg"
#MODULE_PARAMS="$MODULE_PARAMS force=yes"
MODULE_PARAMS="$MODULE_PARAMS archive_type=dmg"
MODULE_PARAMS="$MODULE_PARAMS archive_path='JDK 7 Update 25.pkg'"
#echo $MODULE_PARAMS
$ANSIBLE_SRC_PATH/hacking/test-module -m share/library/mac_pkg -a "$MODULE_PARAMS"
