import re 
warPath = 'https://github.com/sumitdahiya38/SOA_Composite/blob/master/MyFirstApp/deploy/sca_MyFirstApp1.jar'
connect('weblogic','weblogic123','t3://172.17.17.115:7001')

appList = re.findall('sca_MyFirstApp1',ls('/AppDeployments'))
if len(appList) > 1:
    oldestArchiveVersion = min(map(int, appList))
    undeploy('sca_MyFirstApp1', archiveVersion = oldestArchiveVersion)
 
deploy('sca_MyFirstApp1', path = warPath, retireTimeout = 0, upload = 'True')
 
exit()