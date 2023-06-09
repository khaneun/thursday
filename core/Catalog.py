import requests
from config.Settings import *

class Catalog():

    def __init__(self):

        self.configuration = Configuration()
        self.openAPIKey = self.configuration.CONFIG['OPEN-API-KEY']

        print("Start Catalog Service with [{}]".format(self.openAPIKey))

        self.test_msg = "다음으로 주어지는 2개 데이터 베이스 테이블 스키마로 관계를 분석해줘. "\
                        +"첫번째 테이블의 DDL은 "\
                        +"Create Table Employ("\
                        +"emp_id number not null,"\
                        +"emp_name VARCHAR2(100) NOT NULL,"\
                        +"gender VARCHAR2(10) NULL,"\
                        +"age NUMBER NULL,"\
                        +"hire_date DATE NULL,"\
                        +"etc VARCHAR2(300) NULL,"\
                        +"PRIMARY KEY (emp_id) );) 입니다." \
                        + "두번째 테이블의 DDL은 " \
                        + "Create Table Person(" \
                        + "person_id number not null," \
                        + "person_name VARCHAR2(100) NOT NULL," \
                        + "gender VARCHAR2(10) NULL," \
                        + "age NUMBER NULL," \
                        + "born_date DATE NULL," \
                        + "etc VARCHAR2(300) NULL," \
                        + "PRIMARY KEY (person_id) ); 입니다."

        response = requests.post("https://api.openai.com/v1/chat/completions",
                                 headers = {"Authorization": f"Bearer {self.openAPIKey}"},
                                 json = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": self.test_msg}]},)

        try:
            message = response.json()
            buf = message["id"]
            print(message["choices"][0]["message"]["content"])
        except KeyError:
            print(response.json())
