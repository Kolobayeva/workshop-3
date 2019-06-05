from dao.db import OracleDb


class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getMessageData(self, text_mes=None):

        if text_mes:
            text_mes="'{0}'".format(text_mes)
        else:
            text_mes='null'

        query = "select * from table(orm_user_phone.GetMessageData({0}))".format(text_mes)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getMessageData('Java'))
    print(helper.getMessageData())
