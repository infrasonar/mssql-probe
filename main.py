from libprobe.probe import Probe
from lib.check.mssql import check_mssql
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'mssql': check_mssql
    }

    probe = Probe("mssql", version, checks)

    probe.start()
