connect("weblogic","weblogic123","t3://172.17.17.115:7001")
sca_deployComposite("http://172.17.17.115:7004","SOA_Composite/blob/master/MyFirstApp/deploy/",user="weblogic",password="weblogic123",overwrite=true)
