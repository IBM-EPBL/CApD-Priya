import ibm_db

conn= ibm_db.connect("DATABASE=XXXXX;HOSTNAME=XXXXXX;PORT=XXXXX;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=XXXXX;PWD=XXXXXX",'','')

sql= "SELECT * FROM COURSE"
stmt= ibm_db.exec_immediate(conn,sql)
dictionary= ibm_db.fetch_assoc(stmt)
print(dictionary)
