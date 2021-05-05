from flask import Flask, request, json
import mysql.connector
app = Flask(__name__)


@app.route('/')
def main():
    return "Hello World"


@app.route('/hash', methods=['POST'])
def create_db():
    try:
        nodes = request.json["id"]
        hs = request.json["hash"]
        cnx=mysql.connector.connect(user='root',password='1234',host='127.0.0.1',database='hashbase')
        cursor=cnx.cursor()
        sql = """SELECT string FROM datatable WHERE MATCH(string) AGAINST("%s")""" %nodes
        cursor.execute(sql)
        result=cursor.fetchone()
        if (result!=None):
            print("already have")
        else:
            print("new insert %s", nodes)
            insert_stmt = (
                "INSERT INTO datatable(string, sha)"
                "VALUES (%s, %s)"
            )
            data = (nodes, hs)
            cursor.execute(insert_stmt, data)
            cnx.commit()

        return json.dumps({'success': nodes}), 200

    except:
        return json.dumps({'error_type': "invalid_parameters"}), 400



if __name__ == "__main__":
    app.run()
