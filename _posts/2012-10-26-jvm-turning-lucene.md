#Lucene JVM优化
- tags: jvm, lucene, tomcat

----
####优化配置段
```bash
JAVA_OPTS="
-server -Xms3g -Xmx3g -Xmn800m  -XX:PermSize=256m -XX:MaxPermSize=256m -Xnoclassgc -XX:+DisableExplicitGC
-XX:SurvivorRatio=65536 -XX:MaxTenuringThreshold=0
-XX:+UseParNewGC
-XX:+UseConcMarkSweepGC
-XX:+CMSParallelRemarkEnabled
-XX:+UseCMSCompactAtFullCollection
-XX:CMSFullGCsBeforeCompaction=0
-XX:+UseCMSInitiatingOccupancyOnly
-XX:CMSInitiatingOccupancyFraction=55
-XX:+CMSClassUnloadingEnabled

-XX:+PrintClassHistogram
-XX:+PrintGCTimeStamps
-XX:+PrintHeapAtGC
-XX:+PrintGCApplicationStoppedTime
-XX:+PrintGCDetails
-Xloggc:'/var/log/tomcat_gc.log'
"
```
####优化效果，以下是GClog日志
```bash
36673.582: [GC [1 CMS-initial-mark: 1280228K(2326528K)] 1282461K(3145664K), 0.0020900 secs] [Times: user=0.01 sys=0.00, real=0.00 secs] 
36673.584: [CMS-concurrent-mark-start]
36673.904: [CMS-concurrent-mark: 0.320/0.320 secs] [Times: user=0.88 sys=0.00, real=0.32 secs] 
36673.904: [CMS-concurrent-preclean-start]
36673.921: [CMS-concurrent-preclean: 0.016/0.016 secs] [Times: user=0.04 sys=0.00, real=0.02 secs] 
36673.921: [CMS-concurrent-abortable-preclean-start]
36675.839: [CMS-concurrent-abortable-preclean: 0.348/1.919 secs] [Times: user=2.63 sys=0.19, real=1.92 secs] 
36675.840: [GC[YG occupancy: 461341 K (819136 K)]36675.840: [Rescan (parallel) , 0.2238640 secs]36676.064: [weak refs processing, 0.0055360 secs]36676.069: [class unloading, 0.0077180 secs]36676.077: [scrub symbol & string tables, 0.0051810 secs] [1 CMS-remark: 1282623K(2326528K)] 1743964K(3145664K), 0.2490560 secs] [Times: user=1.58 sys=0.00, real=0.25 secs] 
36676.090: [CMS-concurrent-sweep-start]
36679.691: [CMS-concurrent-sweep: 3.535/3.601 secs] [Times: user=6.61 sys=0.08, real=3.60 secs] 
36679.691: [CMS-concurrent-reset-start]
36679.698: [CMS-concurrent-reset: 0.007/0.007 secs] [Times: user=0.02 sys=0.00, real=0.01 secs] 
```

####优化所对应的项目
Apache Lucene, A flagship sub-project, provides Java-based indexing and search technology.
