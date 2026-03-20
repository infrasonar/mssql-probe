from libprobe.probe import Probe
from lib.check.agentalerts import CheckAgentAlerts
from lib.check.agentjobs import CheckAgentJobs
from lib.check.avgtaskcount import CheckAvgTaskCount
from lib.check.bufferpoolusage import CheckBufferPoolUsage
from lib.check.cpustats import CheckCpuStats
from lib.check.dbinstances import CheckDbInstances
from lib.check.dbperfcounters import CheckDbPerfCounters
from lib.check.dbtracestatus import CheckDbTraceStatus
from lib.check.drivelatency import CheckDriveLatency
from lib.check.filelatency import CheckFileLatency
from lib.check.hardware import CheckHardware
from lib.check.heaptables import CheckHeapTables
from lib.check.indexchange import CheckIndexChange
from lib.check.indexfragmentation import CheckIndexFragmentation
from lib.check.indexusage import CheckIndexUsage
from lib.check.instanceconfig import CheckInstanceConfig
from lib.check.instanceperfcounters import CheckInstancePerfCounters
from lib.check.lastbackups import CheckLastBackups
from lib.check.logicalqueryreads import CheckLogicalQueryReads
from lib.check.logshipping import CheckLogShipping
from lib.check.logshippinglog import CheckLogShippingLog
from lib.check.memoryconsumers import CheckMemoryConsumers
from lib.check.memorydistribution import CheckMemoryDistribution
from lib.check.memorydumps import CheckMemoryDumps
from lib.check.missingindexes import CheckMissingIndexes
from lib.check.numa import CheckNuma
from lib.check.oldstatistics import CheckOldStatistics
from lib.check.osmemory import CheckOsMemory
from lib.check.pagelifeexpectancy import CheckPagelifeExpectancy
from lib.check.pendingmemorygrants import CheckPendingMemoryGrants
from lib.check.plancache import CheckPlanCache
from lib.check.processaddressspace import CheckProcessAddressSpace
from lib.check.recoverymodel import CheckRecoveryModel
from lib.check.sessions import CheckSessions
from lib.check.sqlservices import CheckSqlServices
from lib.check.system import CheckSystem
from lib.check.tablesizes import CheckTableSizes
from lib.check.topexecutedqueries import CheckTopExecutedQueries
from lib.check.topqueryio import CheckTopQueryIo
from lib.check.topworkertimequeries import CheckTopWorkerTimeQueries
from lib.check.unusedindexes import CheckUnusedIndexes
from lib.check.volumes import CheckVolumes
from lib.check.waitstats import CheckWaitStats
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckAgentAlerts,
        CheckAgentJobs,
        CheckAvgTaskCount,
        CheckBufferPoolUsage,
        CheckCpuStats,
        CheckDbInstances,
        CheckDbPerfCounters,
        CheckDbTraceStatus,
        CheckDriveLatency,
        CheckFileLatency,
        CheckHardware,
        CheckHeapTables,
        CheckIndexChange,
        CheckIndexFragmentation,
        CheckIndexUsage,
        CheckInstanceConfig,
        CheckInstancePerfCounters,
        CheckLastBackups,
        CheckLogicalQueryReads,
        CheckLogShipping,
        CheckLogShippingLog,
        CheckMemoryConsumers,
        CheckMemoryDistribution,
        CheckMemoryDumps,
        CheckMissingIndexes,
        CheckNuma,
        CheckOldStatistics,
        CheckOsMemory,
        CheckPagelifeExpectancy,
        CheckPendingMemoryGrants,
        CheckPlanCache,
        CheckProcessAddressSpace,
        CheckRecoveryModel,
        CheckSessions,
        CheckSqlServices,
        CheckSystem,
        CheckTableSizes,
        CheckTopExecutedQueries,
        CheckTopQueryIo,
        CheckTopWorkerTimeQueries,
        CheckUnusedIndexes,
        CheckVolumes,
        CheckWaitStats,
    )

    probe = Probe("mssql", version, checks)

    probe.start()
