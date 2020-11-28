import sqlite3

conn = sqlite3.connect('hospital_sqlite.db')
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS doctor (
	name VARCHAR(20),
	department VARCHAR(40),
	professional_title VARCHAR(40),
	intro VARCHAR(120),
	expert_in VARCHAR(120)
);''')

# Insert a row of data
c.execute("""INSERT INTO doctor VALUES('老刘', '儿科','主治医师', 'ee', 'eeee');""")
c.execute("""INSERT INTO doctor VALUES('老王', '妇科','住院医师', 'ff', 'ffff');""")
c.execute("""INSERT INTO doctor VALUES('小王', '呼吸内科','住院医师', 'gg', 'gggg');""")
c.execute("""INSERT INTO doctor VALUES('小狗', '口腔科','住院医师', 'hh', 'hhhh');""")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()