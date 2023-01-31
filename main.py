from libprobe.probe import Probe
from lib.check.agentalerts import check_agentalerts
from lib.check.agentjobs import check_agentjobs
from lib.check.avgtaskcount import check_avgtaskcount
from lib.check.bufferpoolusage import check_bufferpoolusage
from lib.check.cpustats import check_cpustats
from lib.check.dbinstances import check_dbinstances
from lib.check.dbperfcounters import check_dbperfcounters
from lib.check.dbtracestatus import check_dbtracestatus
from lib.check.drivelatency import check_drivelatency
from lib.check.filelatency import check_filelatency
from lib.check.hardware import check_hardware
from lib.check.heaptables import check_heaptables
from lib.check.indexchange import check_indexchange
from lib.check.indexfragmentation import check_indexfragmentation
from lib.check.indexusage import check_indexusage
from lib.check.instanceconfig import check_instanceconfig
from lib.check.instanceperfcounters import check_instanceperfcounters
from lib.check.lastbackups import check_lastbackups
from lib.check.logicalqueryreads import check_logicalqueryreads
from lib.check.logshipping import check_logshipping
from lib.check.logshippinglog import check_logshippinglog
from lib.check.memoryconsumers import check_memoryconsumers
from lib.check.memorydistribution import check_memorydistribution
from lib.check.memorydumps import check_memorydumps
from lib.check.missingindexes import check_missingindexes
from lib.check.numa import check_numa
from lib.check.oldstatistics import check_oldstatistics
from lib.check.osmemory import check_osmemory
from lib.check.pagelifeexpectancy import check_pagelifeexpectancy
from lib.check.pendingmemorygrants import check_pendingmemorygrants
from lib.check.plancache import check_plancache
from lib.check.processaddressspace import check_processaddressspace
from lib.check.recoverymodel import check_recoverymodel
from lib.check.sessions import check_sessions
from lib.check.sqlservices import check_sqlservices
from lib.check.system import check_system
from lib.check.tablesizes import check_tablesizes
from lib.check.topexecutedqueries import check_topexecutedqueries
from lib.check.topqueryio import check_topqueryio
from lib.check.topworkertimequeries import check_topworkertimequeries
from lib.check.unusedindexes import check_unusedindexes
from lib.check.volumes import check_volumes
from lib.check.waitstats import check_waitstats
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'agentalerts': check_agentalerts,
        'agentjobs': check_agentjobs,
        'avgtaskcount': check_avgtaskcount,
        'bufferpoolusage': check_bufferpoolusage,
        'cpustats': check_cpustats,
        'dbinstances': check_dbinstances,
        'dbperfcounters': check_dbperfcounters,
        'dbtracestatus': check_dbtracestatus,
        'drivelatency': check_drivelatency,
        'filelatency': check_filelatency,
        'hardware': check_hardware,
        'heaptables': check_heaptables,
        'indexchange': check_indexchange,
        'indexfragmentation': check_indexfragmentation,
        'indexusage': check_indexusage,
        'instanceconfig': check_instanceconfig,
        'instanceperfcounters': check_instanceperfcounters,
        'lastbackups': check_lastbackups,
        'logicalqueryreads': check_logicalqueryreads,
        'logshipping': check_logshipping,
        'logshippinglog': check_logshippinglog,
        'memoryconsumers': check_memoryconsumers,
        'memorydistribution': check_memorydistribution,
        'memorydumps': check_memorydumps,
        'missingindexes': check_missingindexes,
        'numa': check_numa,
        'oldstatistics': check_oldstatistics,
        'osmemory': check_osmemory,
        'pagelifeexpectancy': check_pagelifeexpectancy,
        'pendingmemorygrants': check_pendingmemorygrants,
        'plancache': check_plancache,
        'processaddressspace': check_processaddressspace,
        'recoverymodel': check_recoverymodel,
        'sessions': check_sessions,
        'sqlservices': check_sqlservices,
        'system': check_system,
        'tablesizes': check_tablesizes,
        'topexecutedqueries': check_topexecutedqueries,
        'topqueryio': check_topqueryio,
        'topworkertimequeries': check_topworkertimequeries,
        'unusedindexes': check_unusedindexes,
        'volumes': check_volumes,
        'waitstats': check_waitstats,
    }

    probe = Probe("mssql", version, checks)

    probe.start()
