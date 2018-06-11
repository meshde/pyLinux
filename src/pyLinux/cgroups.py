import os
from pyLinux import utils

class Cgroup(object):

    BASEDIR = '/sys/fs/cgroup'

    def __init__(self, group):
        self.group = group
        self.resources = {}
        assert utils.is_root()

    def __create_resource_entry(self, resource):
        entry = {}

        resource_dir = os.path.join(Cgroup.BASEDIR, resource)
        cgroup_dir = os.path.join(resource_dir, self.group)
        if not os.path.exists(cgroup_dir):
            os.makedirs(cgroup_dir)
        tasks_file_path = os.path.join(cgroup_dir, 'tasks')

        entry['cgroup_dir'] = cgroup_dir
        entry['tasks_file_path'] = tasks_file_path
        self.resources[resource] = entry
        return

    def get_cgroup_dir(self, resource):
        if resource in self.resources:
            return self.resources[resource]['cgroup_dir']

        resource_dir = os.path.join(Cgroup.BASEDIR, self.group)
        cgroup_dir = os.path.join(resource_dir, cgroup_dir)
        return cgroup_dir

    def get_tasks_file_path(self, resource):
        if resource not in self.resources:
            self.__create_resource_entry(resource)
        tasks_file_path = self.resources[resource]['tasks_file_path']
        return tasks_file_path

    def __assigned(self, tasks_file_path):
        with open(tasks_file_path, 'r') as tasks_file:
            for line in tasks_file:
                line = line.strip()
                if line == str(os.getpid()):
                    return True
        return False

    def assigned(self, resource):
        tasks_file_path = self.get_tasks_file_path(resource)
        return self.__assigned(tasks_file_path)

    def assign(self, resource):
        tasks_file_path = self.get_tasks_file_path(resource)
        if not self.__assigned(tasks_file_path):
            with open(tasks_file_path, 'a') as tasks_file:
                tasks_file.write(str(os.getpid()))
                tasks_file.write('\n')
        return

    def set(self, resource, attribute, value):
        self.assign(resource)
        cgroup_dir = self.get_cgroup_dir(resource)
        attribute_path = os.path.join(cgroup_dir, attribute)
        with open(attribute_path, 'w') as f:
            f.write(str(value))
        return
