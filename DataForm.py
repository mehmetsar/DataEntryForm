from tkinter import *
import psycopg2




root = Tk()
root.title('Codemy. com- Postgres Cloud App')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry ("500x550")

def query() :
# Configure and connect to Postgres
    conn = psycope2.connect(
    host='ec2-54-228-218-84.eu-west-1.compute.amazonaws.com'
    database="d859ssgdssb8t6"
    user="nfcincpwrptzfx"
    password="afa50cf93ccb3c851e4bc315ed33463c1a921319e716debb065844d50233415f"
    port="5432",
    )

    c = conn.cursor()
    c.execute (''' CREATE TABLE IF NOT EXIST content
    (id INTEGER,
    content TEXT)
    
    ''')
    conn.commit()
    conn.close()

def submit():

    conn = psycope2.connect(
    host='ec2-54-228-218-84.eu-west-1.compute.amazonaws.com'
    database="d859ssgdssb8t6"
    user="nfcincpwrptzfx"
    password="afa50cf93ccb3c851e4bc315ed33463c1a921319e716debb065844d50233415f"
    port="5432",
    )

    c = conn.cursor()
    c.execute(''' INSERT INTO content (id, content)
    VALUES (%s, %s)''' , (f_name.get(), l_name.get()))
    conn.commit()
    conn.close()

    update()

def update():

    conn = psycope2.connect(
    host='ec2-54-228-218-84.eu-west-1.compute.amazonaws.com'
    database="d859ssgdssb8t6"
    user="nfcincpwrptzfx"
    password="afa50cf93ccb3c851e4bc315ed33463c1a921319e716debb065844d50233415f"
    port="5432",
    )

    c = conn.cursor()
    c.execute("SELECT * FROM content")
    records = c.fetchall()
    output = ''

    for record in records:
        output_label.config(text = f'{output'\n{record[0]} {record[1]}')
        output =output_label['text']   

    conn.close()
# Create The GUI For The App
my_frame = LabelFrame (root, text="Postgres Example")
my_frame.pack(pady=20)
f_label = Label(my_frame, text="id")
f_label.grid(row=0, column=0, pady=10, padx=10)
f_name = Entry(my_frame, font= ("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)
l_label = Label(my_frame, text= "content:")
l_label.grid(row=1, column=0, pady=10, padx=10)
l_name = Entry(my_frame, font= ("Helvetica, 18"))
l_name.grid(row=1, column=1, pady=10, padx=10)
submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)
update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)
output_label = Label(root, text = '')
output_label.pack(pady=50)

root.mainloop()