import os

class Cgroups(object):

    BASEDIR = '/sys/fs/cgroup'

    def __init__(self, group):
        self.group = group
        self.assigned = {}

    def get_cgroup_dir(self, resource):
        resource_dir = os.path.join(Cgroups.BASEDIR, self.group)
        cgroup_dir = os.path.join(resource_dir, cgroup_dir)
        return cgroup_dir

    def get_task_file_path(self, resource):
        cgroup_dir = self.get_cgroup_dir(resource)
        tasks_file_path = os.path.join(cgroup_dir, 'tasks')
        return tasks_file_path

    def assigned(self, resource):
        tasks_file_path = self.get_tasks_file_path(resource)
        with open(tasks_file_path, 'r') as f:
            for line in tasks_file:
                line = line.strip()
                if line == str(os.getpid()):
                    return True
        return False

    def set(self, resource, attribute, value):

        if not os.path.exists(cgroup_dir):
            os.makedirs(cgroup_dir)

        with open(tasks_file_path, 'a') as tasks_file:
            tasks_file.write(str(os.getpid()))
            tasks_file.write('\n')
