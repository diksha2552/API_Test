from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:disk@2552@/Company_struct'
def get_info():
    result = db.engine.execute(text("select name from details_empl"))
    names = []
    for row in result:
        names.append(row[0])
    print(names)
    return ''.join(names)

@app.route("/")
def func_get_name():
    result = get_info()
    return result




@app.route("/func_1")
def func_get_doj():
    result = db.engine.execute(text("select doj from details_empl"))
    doj = []
    for row in result:
        doj.append(row[0])
    print(doj)
    v = jsonify(doj)  # To make it a suitable response
    return v     # Return statement is needed, as list is not callable.


@app.route("/func_2")
def func_get_tree():     # ''' ... to write query with linebreaks.
    result = db.engine.execute(text('''WITH RECURSIVE childrenCTE(id_1,name, parent_id, depth ) AS (
    SELECT id_1,name, parent_id, 1
    FROM details_empl
    WHERE parent_id is Null
    UNION ALL
    SELECT details_empl.id_1,details_empl.name, details_empl.parent_id, childrenCTE.depth+1
    FROM details_empl
    JOIN childrenCTE ON(details_empl.parent_id = childrenCTE.id_1)
    )
    SELECT * FROM childrenCTE'''))
    list_of_dictionaries=[]
    for row in result:
        d ={'id_1' : row[0], 'name': row[1], 'parent_id':row[2], 'depth':row[3]}   # Creating a list of dictionaries.
        list_of_dictionaries.append(d)

    v = jsonify(list_of_dictionaries)   #Object of type 'ResultProxy' is not JSON serializable
    return v





if __name__ == '__main__':
    app.run(debug=True)
