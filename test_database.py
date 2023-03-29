import database

#pytest is used to run these

def test_creation():
	db = database.Database(None, "")
	db.check_login("12345","13456")#just calling this so the thread is done
	assert(len(db.employees) == 103)
	db.save_database()

def test_login():
	db = database.Database(None,"")
	password_hash = database.password_to_hash("51-4678119","12345")
	print(db.check_login("51-4678119","12345"))#assumes database has the id and password

def test_find():
	db = database.Database(None,"")
	db.check_login("12345","12345")#just calling this so the loader thread is done
	found = db.find_employees("Bob")
	assert(len(found) == 4) #assuming only 4 people have bob in name
	found = db.find_employees(id="12-34")
	assert(len(found) == 3) #assuming only 3 people have "12-34" in id
	found = db.find_employees(title="software engineer")
	assert(len(found)==1) #assuming only 1 person has that title

def test_add_remove_():
	db = database.Database(None,"")
	db.check_login("1235","2345")#just calling this so the laoder thread is done
	db.add_employee(database.Employee("12-3456792","Jimmy","Jimanthymee",title="The Jimster"))
	db.add_employee(database.Employee("12-3456792","Jimmy","Jimanthymee",title="The Jimster"))#try adding two
	found = db.find_employees(title="Jimster")
	print(len(found))
	assert(len(found)==1)
	db.remove_employee("12-3456792")
	found = db.find_employees(title="Jimster")
	assert(len(found)==0)

#example database employees with password "12345" everyone has password "12345"
#12-3456789,Bob,Tester,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7890,3/24/2023,123-45-6789,3/24/2023,30417353-K,465794-3611,0,assitant to the manager,stapler,False,4e4577f023d1c8ab0deb91ecc1cc4f51a0cd232e0b91e60c8811e6c82da60956,bob@bob.com
#12-3456790,Bob,Tester The Second,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7890,4/25/2023,123-45-6790,4/25/2023,30417354-K,465794-3611,1,assitant to the assistant to the manager,stapler,False,adabe0c70c26f8850c41a6ddb969db8f3de122c203af1beed2953b18e8fb2776,bob2@bob.com
#12-3456791,Bob,Tester The Third,894 Glendale Plaza,Worcester,Massachusetts,1610,2,62862.15,46,16.85,123-456-7891,4/26/2023,123-45-6791,4/26/2023,30417355-K,465794-3611,1,assitant to the assitant to the assistant to the manager,stapler,False,100b16b5ee41ec5bb14087101261e0193b2db7ebbd2fc6739a41599d8654a91e,bob3@bob.com