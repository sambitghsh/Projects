import sqlite3
import sample
from PyQt5 import QtSql
def fetch_bat():
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute('''select name from player where roll="Bat";''')
    record=uemo.fetchall()
    demo.close()
    return (record)

def fetch_ball():
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute('''select name from player where roll="Ball";''')
    record=uemo.fetchall()
    demo.close()
    return (record)

def fetch_ar():
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute('''select name from player where roll="AR";''')
    record=uemo.fetchall()
    demo.close()
    return (record)

def fetch_wk():
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute('''select name from player where roll="WK";''')
    record=uemo.fetchall()
    demo.close()
    return (record)

def fetch_roll(item):
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute("select roll from player where name=?;",(item,))
    record=uemo.fetchone()
    demo.close()
    return (record)

def fetch_value(item):
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute("select value from player where name=?;",(item,))
    record=uemo.fetchone()
    demo.close()
    print(record)
    return (record)

def store_team(nm, l):
    name=str(nm)
    pl=l
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    if len(l)<=8:
        store="Team not formed.Total nine member must be present."
        sample.MainWindow(store)
    else:
        for i in range(len(pl)):
            val=fetch_value(pl[i])
            uemo.execute("insert into teams(name,players,value)values(?,?,?);",(name,pl[i],val[0]))
        demo.commit()

def retrieve_team(nm):
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute("select distinct(players) from teams where name=?;",(nm,))
    record=uemo.fetchall()
    demo.close()
    return (record)

def fetch_teamname():
    demo=sqlite3.connect("fantasy_cricket.db")
    uemo=demo.cursor()
    uemo.execute('''select distinct(name) from teams;''')
    record=uemo.fetchall()
    demo.close()
    return (record)
