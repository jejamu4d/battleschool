MODULE_PARAMS="pkg_type=script"
MODULE_PARAMS="$MODULE_PARAMS script_exe=ruby"
MODULE_PARAMS="$MODULE_PARAMS script_creates=/usr/local/bin/brew"
MODULE_PARAMS="$MODULE_PARAMS url=https://raw.github.com/mxcl/homebrew/go"
#echo $MODULE_PARAMS
~/workspace/32degrees/ansible/hacking/test-module -m share/library/mac_pkg -a "$MODULE_PARAMS"
