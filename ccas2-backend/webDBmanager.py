import pymysql
import logging
import sqlite3
import datetime
class mysqlUtils():
    
    # def __init__(self,confobj):
    def __init__(self):
        self.host = ""
        self.port = ""
        self.username = ""
        self.password = ""
        self.dbname = ""
        self.charsets = "UTF8"

        self.base_header = "INSERT INTO {}.".format(self.dbname)
        try:
            self.con = pymysql.Connect(
            host=self.host,
            port = int(self.port),
            user=self.username,
            passwd = self.password,
            db=self.dbname,
            charset=self.charsets,
            cursorclass=pymysql.cursors.DictCursor  # return the query results in dict format not the tuple format.
            )
            #获得数据库的游标
            self.cursor = self.con.cursor() #开启事务
            logging.info("Get cursor successfully")
        except Exception as e :
            logging.info("Can not connect databse {}\nReason:{}".format(self.dbname,e))

    def close(self):
        if  self.con:
            self.con.commit()
            self.con.close()
            logging.info("Close database {} successfully".format(self.dbname))
        else:
            logging.info("DataBase doesn't connect,close connectiong error;please check the db config.")

    def fetchOne(self):
        data = self.cursor.fetchone()
        return(data)

    def fetchAll(self):
        data  = self.cursor.fetchall()
        return(data)

    def excute(self,sql,data = None):
        try:
            if data is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql,data)
            self.commit()
            return(self.cursor.rowcount)
        except Exception as e :
            print(f"Can not excute sql '{sql}' \nwith data {data}\nbecause:{str(e)}")
            self.rollback()
            return False
        

    def commit(self):
        self.con.commit()

   
    def rollback(self):
        self.con.rollback()
        logging.info("RollBack Transaction")


class webMysqlUtil(): # inherient from mysqlUtils class

    def __init__(self):
        self.host = "192.168.164.83"
        self.port = "33067"
        self.username = "zhengxc"
        self.password = "canceranno"
        self.dbname = "cancerkdb"
        self.charsets = "UTF8"

        self.base_header = "INSERT INTO {}.".format(self.dbname)
        try:
            self.con = pymysql.Connect(
            host=self.host,
            port = int(self.port),
            user=self.username,
            passwd = self.password,
            db=self.dbname,
            charset=self.charsets,
            cursorclass=pymysql.cursors.DictCursor  # return the query results in dict format not the tuple format.
            )
            #获得数据库的游标
            self.cursor = self.con.cursor() #开启事务
            logging.info("Get cursor successfully")
        except Exception as e :
            logging.info("Can not connect databse {}\nReason:{}".format(self.dbname,e))

    def close(self):
        if  self.con:
            self.con.commit()
            self.con.close()
            logging.info("Close database {} successfully".format(self.dbname))
        else:
            logging.info("DataBase doesn't connect,close connectiong error;please check the db config.")

    def fetchOne(self):
        data = self.cursor.fetchone()
        return(data)

    def fetchAll(self):
        data  = self.cursor.fetchall()
        return(data)

    def excute(self,sql,data = None):
        try:
            if data is None:
                self.cursor.execute(sql)
            else:
                self.cursor.execute(sql,data)
            self.commit()
            return(self.cursor.rowcount)
        except Exception as e :
            print(f"Can not excute sql '{sql}' \nwith data {data}\nbecause:{str(e)}")
            self.rollback()
            return False
        

    def commit(self):
        self.con.commit()

   
    def rollback(self):
        self.con.rollback()
        logging.info("RollBack Transaction")

    def get_one_jobinfo_by_job_id(self,jobid):
        sql = "select * from jobs where jobid = (%s)"
        self.excute(sql,jobid)
        res = self.fetchOne()
        return res

    def insertOneJob(self,
            jobid,
            status,
            refver,
            workdir,
            start_time,
            snvindeltype,
            has_exp,
            has_cnv,
            has_meth,
            email=None,
            title=None,
            end_time=None,
            exptype=None,
            cnvtype=None,
            methtype=None,
            has_send_jobid=0,
            has_send_finished=0,
            ):
        sql = """
        insert into jobs (
            jobid,
            status,
            title,
            refver,
            workdir,
            start_time,
            end_time,
            email,
            snvindeltype,
            exptype,
            cnvtype,
            methtype,
            has_exp,
            has_cnv,
            has_meth,
            has_send_jobid,
            has_send_finished
        ) values (
            (%s),(%s),(%s),(%s),(%s),
            (%s),(%s),(%s),(%s),(%s),
            (%s),(%s),(%s),(%s),(%s),
            (%s),(%s)
        )
        """
        self.excute(sql,(            
            jobid,
            status,
            title,
            refver,
            workdir,
            start_time,
            end_time,
            email,
            snvindeltype,
            exptype,
            cnvtype,
            methtype,
            has_exp,
            has_cnv,
            has_meth,
            has_send_jobid,
            has_send_finished
            )
            )
        self.commit()

    def updateJobStatus(self,jobid,status):
        sql= """
        update jobs
        set status = (%s)
        where jobid = (%s)
        """
        self.excute(sql,(str(status),jobid))

    def updateJobEndtime(self,jobid,endtime):
        sql= """
        update jobs
        set end_time = (%s)
        where jobid = (%s)
        """
        self.excute(sql,(endtime,jobid))

    def updateJobEmailSendJoid(self,jobid,has_send_jobid):
        sql= """
        update jobs
        set has_send_jobid = (%s)
        where jobid = (%s)
        """
        self.excute(sql,(has_send_jobid,jobid))

    def updateJobEmailSendFinished(self,jobid,has_send_finished):
        sql= """
        update jobs
        set has_send_finished = (%s)
        where jobid = (%s)
        """
        self.excute(sql,(has_send_finished,jobid))

    def checkJobStatus(self,jobid):
        sql = """
        select jobs.`status` from jobs WHERE  1=1 and jobid = (%s) ;
        """
        self.excute(sql,(jobid,))
        return self.fetchOne()
class sqlite3Utils():
    
    def __init__(self,dbpath):
        # 创建log日志数据库
        """
        create table if not exists batchs ( BATCHID	 text not null PRIMARY KEY , INIT_TIME_STAMP text not null, CURR_TIME_STAMP	 text not null, BATCHID_DIR	 text not null, STATUS	 integer not null default 0, IDLIST	 text , ACCN	 text not null, FTP_DIR	 text not null, PROCESS_DIR	 text not null, START_GWHID	 text , END_GWHID text , START_WGSID text , END_WGSID text);
        """
        def dict_factory(cursor, row): 
            d = {} 
            for idx, col in enumerate(cursor.description): 
                d[col[0]] = row[idx] 
            return d     
        self.con = sqlite3.connect(dbpath)
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()

    def execute_fetchOne(self,sql,params=None):

        try:
            if params is not None:
                self.cur.execute(sql,params)
                results = self.cur.fetchone()
            else:
                self.cur.execute(sql)
                results = self.cur.fetchone()
            return([True,results])
        except Exception as e:
            print(f"FetchOne has errors:\n{str(e)}")
            self.con.rollback()
            return([False,str(e)])  

    def execute_fetchAll(self,sql,params=None):
        try:
            if params is None:
                self.cur.execute(sql)
                results = self.cur.fetchall()
            else:
                self.cur.execute(sql,params)
                results = self.cur.fetchall()
            return([True,results])
        except Exception as e:
            print(f"FetchAll has errors:\n{str(e)}")
            self.con.rollback()
            return([False,str(e)])            

    def getOneGeneDetail(self,GeneID):
        sql = "select * from gene WHERE geneid = ?;"
        return self.execute_fetchOne(sql,(GeneID,))



if __name__ == "__main__":
    testdbutils = webMysqlUtil()
    testdbutils.insertOneJob(
        jobid="cc",
        status="ok",
        refver="hg19",
        workdir="aa",
        start_time=datetime.datetime.now(),
        snvindeltype="vcf",
        has_exp=0,
        has_cnv=0,
        has_meth=0,
        email="aa",
        end_time=datetime.datetime.now(),
        exptype="gene",
        cnvtype="region",
        methtype="gene",
        title="asdfa",
        has_send_jobid=1,
        has_send_finished=0
    )
    testdbutils.updateJobStatus("notfound","aa")
    testdbutils.updateJobEndtime("aa",datetime.datetime.now())
    testdbutils.updateJobEmailSendFinished("aa",1)
    testdbutils.updateJobEmailSendJoid("aa",1)
