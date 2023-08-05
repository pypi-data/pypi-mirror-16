import itertools
import pip
import yaml

from .updater import get_last_version
from .migrator import Migrator

FILENAME = 'rqr.yaml'


class Requirements:
    def __init__(self):
        self.pkgs = {}
        self.migrator = Migrator()
        self.reload()

    def reload(self):
        try:
            with open(FILENAME, 'r') as stream:
                self.pkgs = yaml.load(stream)
                stream.close()
        except FileNotFoundError:
            self.pkgs = {}

    def migrate(self):
        # TODO: rather merge than override
        self.pkgs = self.migrator.run()
        self.save()

    def add(self, pkg, target, version):
        if target not in self.pkgs:
            self.pkgs[target] = {}
        self.pkgs[target][pkg] = version
        self.save()

    def save(self):
        with open(FILENAME, 'w') as stream:
            yaml.dump(self.pkgs, stream, default_flow_style=False)
            stream.close()

    def install(self, ipkgs, target):
        pkgs = {}
        if len(ipkgs) == 0: # no argument supplied, try to install from config
            pkgs = self.pkgs
        else:
            for pkg in ipkgs:
                pkgs[pkg] = str(get_last_version(pkg))
                if target:
                    self.add(pkg, target, pkgs[pkg])

        # flat list of all packages of all targets to install with their version
        pip_ipkgs = itertools.chain.from_iterable([pkgs[target].items() for target in pkgs])
        # join to pkg==version format for pip
        pip.main(['install'] + ['=='.join(pkg) for pkg in pip_ipkgs])
        return pkgs

    def __str__(self):
        res = []
        for target in self.pkgs:
            res.append(target + ':')
            for requirement in self.pkgs[target]:
                version = self.pkgs[target][requirement]
                res.append('  - {0}@{1}'.format(requirement, version))
        return '\n'.join(res)
