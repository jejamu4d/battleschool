__author__ = 'spencergibb'


import abc
import os
import sys

from ansible import callbacks
from ansible import errors
from ansible.runner import Runner


class Source(object):
    """Base class for source handlers.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, options, sources):
        self.options = options
        self.sources = sources
        return

    @abc.abstractmethod
    def type(self):
        pass

    @abc.abstractmethod
    def module_args(self, source):
        """Override to do something useful.
        """

    def dest_dir(self, source):
        dest_dir = "%s/%s" % (self.options.cache_dir, source['name'])
        return dest_dir

    def module_name(self):
        return self.type()

    def run(self, inventory, sshpass, sudopass):
        playbooks = []
        if self.type() in self.sources:
            for source in self.sources[self.type()]:
                print source
                runner_cb = callbacks.CliRunnerCallbacks()
                runner_cb.options = self.options
                runner_cb.options.module_name = self.module_name()
                module_args = self.module_args(source)
                #TODO: get workstation from options
                runner = Runner(
                    pattern='workstation',
                    module_name=self.type(),
                    module_path=self.options.module_path,
                    module_args=module_args,
                    inventory=inventory,
                    callbacks=runner_cb,
                    timeout=self.options.timeout,
                    transport=self.options.connection,
                    sudo=self.options.sudo,
                    sudo_user=self.options.sudo_user,
                    sudo_pass=sudopass,
                    check=self.options.check,
                    diff=self.options.diff,
                    private_key_file=self.options.private_key_file,
                    remote_user=self.options.remote_user,
                    remote_pass=sshpass,
                    forks=self.options.forks
                )

                try:
                    results = runner.run()
                    for result in results['contacted'].values():
                        if 'failed' in result or result.get('rc', 0) != 0:
                            sys.exit(2)
                    if results['dark']:
                        sys.exit(2)
                except errors.AnsibleError, e:
                    # Generic handler for ansible specific errors
                    callbacks.display("ERROR: %s" % str(e), stderr=True, color='red')
                    sys.exit(1)

                source_playbooks = ["local.yml"]

                #add other playbooks relative to dest_dir from config.yml
                if "playbooks" in source:
                    for playbook_name in source['playbooks']:
                        if playbook_name not in source_playbooks:
                            source_playbooks.append(playbook_name)

                for playbook_name in source_playbooks:
                    playbook = "%s/%s" % (self.dest_dir(source), playbook_name)
                    if os.path.exists(playbook) and os.path.isfile(playbook):
                        playbooks.append(playbook)


                module_dir = "%s/modules" % self.dest_dir(source)
                if not os.path.exists(module_dir) or not os.path.isfile(module_dir):
                    module_dir = None

        return playbooks, module_dir
