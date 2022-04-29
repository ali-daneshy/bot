

import os 
import asyncio
import sqlite3
from email.message import Message
import time
from pyrogram import Client, filters
from validate_email_address import validate_email
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton
from Markups import markups, stickers, texts , admin_markups

admin_pv = 5068958781 # costumer
admin_pv = 5264159037 # me


api_hash = None
api_id = None

db = dict()
app = Client('bot2',api_hash ,api_id,proxy=dict(hostname="127.0.0.1",port=9150))

con = sqlite3.connect('gmail_bot_crawler.db')
cur  = con.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS 
				profile(
					id 							INT PRIMARY KEY ,
					full_name  					TEXT,
					city  						TEXT,
					age  						INT ,
					phone_number 				INT , 
					Bank_card_number 			INT , 
					Bank_card_number_name 		TEXT,
					all_gmails  				INT ,
					awaiting_payment			INT ,
					accessible_account  		INT ,
					Inaccessible_account 		INT ,
					check_infos 				TEXT
					 )''')
con.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS 
				True_gmails(
					gmail     					TEXT PRIMARY KEY ,
					password     				TEXT  ,
					id							INT ) ''')

con.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS 
				gmails(
					gmail     					TEXT PRIMARY KEY ,
					password     				TEXT  ,
					id							INT ) ''')

con.commit()


cur.execute('''CREATE TABLE IF NOT EXISTS 
				Block_gmails(
					gmail     					TEXT PRIMARY KEY ,
					password     				TEXT  ,
					id							INT ) ''')

con.commit()

async def messager(UI , status ,MM ,format=None ,  disable_web=False  , sticker = False , **kwargs  ):
	if db[UI]['status'] == 'yourwelcom':
		db[UI]['message_id'] == set()
	await app.delete_messages(UI ,MM )
	await app.delete_messages(UI ,db[UI].get('message_id') )
	
	await asyncio.sleep(0.2)
	db[UI]['status'] = status
	
	
	if sticker == True and stickers.get(status) :
		app.send_sticker(UI , stickers[status])
	elif format != None :
		[a , b , c ,d] = format
		try:
			await app.send_message(UI , texts[status].format(a , b , c ,d) , reply_markup=markups[status] , disable_web_page_preview=disable_web)
		except:
			await app.send_message(UI , texts[status].format(a , b , c ,d) , disable_web_page_preview=disable_web)
	else:
		try:
			await app.send_message(UI , texts[status], reply_markup=markups[status] , disable_web_page_preview=disable_web)
		except:
			await app.send_message(UI , texts[status], disable_web_page_preview=disable_web)












@app.on_message(filters.command('start') , group=-1)
async def starter(A:Client , B:Message):

	CI  = B.chat.id
	UI  = B.from_user.id
	# UUN = B.from_user.username
	T   = B.text
	UFN = B.from_user.first_name
	ULN = B.from_user.last_name
	MC = B.chat.id
	MM = B.message_id
	if UI == admin_pv :
		try:
			cur.executemany(' INSERT INTO  profile( full_name , id )  VALUES(?,?) ' , [(UFN+ULN , UI)] )
			con.commit()
			cur.execute(f' UPDATE profile SET all_gmails = {0} , awaiting_payment = {0} , accessible_account = {0} , Inaccessible_account = {0}  WHERE id = {UI} ')
			con.commit()
			

			db[UI]={
					'status' : 'yourwelcom',
					'block_list' :[],
					'True_list' :[],
					'block_gmail_repetitious_list' : [] ,
					'multiple_gmail_repetitious_list' : [] , 
					'old_block_gmail_repetitious_list' : [] ,
					'block_gmail_gramer_list' : [] ,
					'first_name' : UFN , 
					'last_name' : ULN , 
					'message_id' : set()}
			await app.send_message(UI , text =  texts[db[UI].get('status')] , reply_markup=admin_markups[db[UI]['status']])
		except:
			db[UI]={
					'status' : 'yourwelcom',
					'block_list' :[],
					'True_list' :[],
					'block_gmail_repetitious_list' : [] ,
					'multiple_gmail_repetitious_list' : [] , 
					'block_gmail_gramer_list' : [] ,
					'old_block_gmail_repetitious_list' : [] ,
					'first_name' : UFN , 
					'last_name' : ULN , 
					'message_id' : set()}
			await app.send_message(UI , text =  texts[db[UI].get('status')] , reply_markup=admin_markups[db[UI]['status']])
			
	else:
		try:
			cur.executemany(' INSERT INTO  profile( full_name , id )  VALUES(?,?) ' , [(UFN+ULN , UI)] )
			con.commit()
			cur.execute(f' UPDATE profile SET all_gmails = {0} , awaiting_payment = {0} , accessible_account = {0} , Inaccessible_account = {0}  WHERE id = {UI} ')
			con.commit()
			db[UI]={
					'status' : 'yourwelcom',
					'block_list' :[],
					'True_list' :[],
					'block_gmail_repetitious_list' : [] ,
					'multiple_gmail_repetitious_list' : [] , 
					'old_block_gmail_repetitious_list' : [] ,
					'block_gmail_gramer_list' : [] ,
					'first_name' : UFN , 
					'last_name' : ULN , 
					'message_id' : set()}
			await app.send_message(UI , text =  texts[db[UI].get('status')] , reply_markup=markups[db[UI]['status']])
		except:
			db[UI]={
					'status' : 'yourwelcom',
					'block_list' :[],
					'True_list' :[],
					'block_gmail_repetitious_list' : [] ,
					'multiple_gmail_repetitious_list' : [] , 
					'old_block_gmail_repetitious_list' : [] ,
					'block_gmail_gramer_list' : [] ,
					'first_name' : UFN , 
					'last_name' : ULN , 
					'message_id' : set()}
			await app.send_message(UI , text =  texts[db[UI].get('status')] , reply_markup=markups[db[UI]['status']])


@app.on_message(filters.media )
async def file(A:Client , B:Message):

	CI  = B.chat.id
	UI  = B.from_user.id
	M   = B.document
	P 	= B.photo

	UFN = B.from_user.first_name
	ULN = B.from_user.last_name
	MC 	= B.chat.id
	MM 	= B.message_id
	S 	= db[UI]['status']
	

	if S == 'input_gmail' :
		db[UI]['status'] = 'yourwelcom'

		async def progress(current, total):
			print(f"{current * 100 / total:.1f}%")
			pp = f"{current * 100 / total:.1f}%"
			if pp != '100.0%':
				await asyncio.sleep(1)	
			
		N = B.document.file_name

		await app.send_message(UI , texts['input_gmail_wait'] )
		await app.download_media(M, progress=progress)
		
		
	
				

		print('yessssss')
		
		f = os.getcwd()

		with open(f'{f}/b/downloads/{N}' , 'r') as ff :
			T = ff.read()
			os.remove(f'{f}/b/downloads/{N}') 
			
		



		
		dd = T.split('\n')
		true_count= 0

		for i in dd :

			ff = i.split(':')

			if T.count(ff[0]) > 1:
				db[UI]['multiple_gmail_repetitious_list'].append((i))

			elif (not '@gmail.com:' in i) or (ff[1] == ''):
				db[UI]['block_gmail_gramer_list'].append((i))

			else:
				cur.execute(f'''SELECT  id FROM gmails WHERE gmail = '{ff[0]}' ''' )
				ss = cur.fetchall()
				cur.execute(f'''SELECT  id FROM True_gmails WHERE gmail = '{ff[0]}' ''' )
				gg = cur.fetchall()
				cur.execute(f'''SELECT  id FROM Block_gmails WHERE gmail = '{ff[0]}' ''' )
				kk = cur.fetchall()
				print(kk)

				if ss == [] and gg == [] and kk == [] :
					isvalid=validate_email(ff[0], verify=True)
					
					if isvalid == None :
						db[UI]['block_list'].append((ff[0]))

					elif isvalid == True :
						true_count += 1
						db[UI]['True_list'].append((ff[0] ,ff[1] , UI ))
				else:

					db[UI]['block_gmail_repetitious_list'].append((ff[0])) #*******************************************************
			

		cur.executemany(f' INSERT INTO  gmails( gmail , password  , id )  VALUES(?,?,?) ' , db[UI]['True_list'])
		con.commit()
		cur.execute(f''' SELECT  Inaccessible_account , all_gmails FROM profile WHERE id = {UI}   ''')
		Y = cur.fetchall()[0]
		F = Y[0]
		L = Y[1]

		F += true_count
		L += true_count

		cur.execute(f' UPDATE profile SET  Inaccessible_account = {F} , all_gmails = {L}  WHERE id = {UI} '  )
		con.commit()
		
		

		if len(db[UI]['True_list']) != 0 :
			#getting from data base 
			#changing it
			#changing update in data base
			pass
			

		with open('gmailes.txt' , 'a') as f :
			for i in db[UI]['True_list']:
				f.write('\n')
				f.write(i[0] +':'+i[1])

		

		ss = '\n'.join(db[UI]['block_list'])
		hh = '\n'.join(db[UI]['block_gmail_repetitious_list'])
		oo = '\n'.join(db[UI]['block_gmail_gramer_list'])
		jj = '\n'.join(db[UI]['multiple_gmail_repetitious_list'])

		if oo == '' :
			oo = '___'
		if ss == '' :
			ss = '___'
		if hh == '' :
			hh = '___'
		if jj == '' :
			jj = '___'
		
		await app.send_message(UI , texts['input_gmail_result'].format(true_count ,oo, ss , hh , jj ))

		db[UI].update( [('True_list' , []) , ('block_list' , []) , ('block_gmail_repetitious_list' , []) , ('block_gmail_gramer_list' , []) , ('multiple_gmail_repetitious_list' , [])])
		
	if S[:16] == 'payment_document' :
		print('OOOOOOOOK')
		
		if B.media != 'photo':
			await app.send_message(admin_pv ,'لطفا به شکل عکس  ارسال کنید' )
		else:
			async def progress(current, total):
				print(f"{current * 100 / total:.1f}%")
				pp = f"{current * 100 / total:.1f}%"
				if pp != '100.0%':
					await asyncio.sleep(1)	

			# async def convertToBinaryData(filename):
			# 	# Convert digital data to binary format
			# 	with open(filename, 'rb') as file:
			# 		blobData = file.read()
			# 	await blobData

			f = os.getcwd()
			
			await app.download_media(P, progress=progress , file_name='dd.jpg')

			# zz = await convertToBinaryData(f'{f}/b/downloads/dd.jpg')





			await app.send_photo(S[16:],photo=f'{f}/b/downloads/dd.jpg' , caption='حقوق شما به حساب شما واریز شد' , reply_markup=InlineKeyboardMarkup([  [InlineKeyboardButton('گزارش عدم واریز'  ,'no_deposit'  )] ]) , progress=progress)

			
			cur.execute(f''' SELECT awaiting_payment , all_gmails FROM profile WHERE  id = '{S[16:]}' ''')
			ss = cur.fetchall()[0]
			
			ss[1] = ss[1] - ss[0]
			ss[0] = 0
			cur.execute(f''' UPDATE profile SET awaiting_payment = {ss[0]} , all_gmails = {ss[1]}  WHERE  id = '{S[16:]}' ''')
			con.commit()


			await app.send_message(admin_pv , 'عملیات با موفقیت انجام شد' )
			
			os.remove(f'{f}/b/downloads/dd.jpg')


	elif B.media != 'document' :
		await app.send_message(UI , 'لطفا فایل را  به  شکل txt بفرستید')


	elif S == 'sending_block_list' :
		N = B.document.file_name

		async def progress(current, total):
			print(f"{current * 100 / total:.1f}%")
			pp = f"{current * 100 / total:.1f}%"
			if pp != '100.0%':
				await asyncio.sleep(1)	
			
			

		await app.send_message(UI , texts['input_gmail_wait'] )
		await app.download_media(M, progress=progress)


		
		f = os.getcwd()

		
		with open(f'{f}/b/downloads/{N}' , 'r') as ff :
			T = ff.read()
			os.remove(f'{f}/b/downloads/{N}') 
		
		T = T.split('\n')
		BlockList = list()
		for i in T :
			ss = i.split(':')
			BlockList.append(ss[0])
			
		cur.execute(f''' SELECT * FROM gmails ''')
		gmails  = cur.fetchall()
		
		cur.execute(f''' DELETE  FROM gmails ''')
		con.commit()

		trues = []
		falses = []
		users = set()
		request = dict()
		

		for i in gmails:
			if not i[0] in BlockList :
				users.add(i[2])
				trues.append(i)
			elif i[0] in BlockList:
				users.add(i[2])
				falses.append(i)
		

		
		for i in users :
			ss = {i :  {'trues' : [] , 'falses' : [] }}
			request.update(ss)

		

		for i in trues :
			h = '''{}:{}'''.format(i[0] ,i[1] )
			request[i[2]]['trues'].append(h)

	

		for i in falses :
			h = '''{}:{}'''.format(i[0] ,i[1] )
			request[i[2]]['falses'].append(h)

		

		# print( 'ارور', falses , trues , request ,  '\n')


		# inserting to true_gmials


		cur.executemany(f''' INSERT INTO  True_gmails( gmail , password , id) VALUES(?,?,?)  ''' , trues )
		con.commit()

		cur.executemany(f''' INSERT INTO  Block_gmails( gmail , password , id) VALUES(?,?,?)  ''' , falses )
		con.commit()


		# charching thair accessible_account and decreasing thair Inaccessible_account
		# sending messages to users for thair gmails resulats
		if request == {}:
			await app.send_message( admin_pv , 'عملیات با موفقیت انجام شد')

		else :
			for i in request :
				
				s = ('\n'.join(request[i]['falses']))
				l = len(request[i]['trues'])
				b = len(request[i]['falses'])
				
				cur.execute(f''' SELECT  accessible_account , Inaccessible_account , all_gmails  FROM profile WHERE  id ='{UI}' ''')
				K = list(cur.fetchall()[0])
			
				K[2] = K[2] - b
				K[1] = K[1] - l - b
				K[0] = K[0] + l
				print(K[0],K[1])
				cur.execute(f''' UPDATE  profile SET  accessible_account = '{K[0]}' , Inaccessible_account = '{K[1]}' , all_gmails = '{K[2]}' WHERE  id ='{UI}' ''')
				con.commit()

				await app.send_message(UI ,texts['filnall_gmail_result'].format( l , s ) )
				await app.send_message( admin_pv , 'عملیات با موفقیت انجام شد')
	



@app.on_message(filters.text)
async def Messager(A:Client , B:Message):
	CI  = B.chat.id
	UI  = B.from_user.id
	T   = B.text
	UFN = B.from_user.first_name
	ULN = B.from_user.last_name
	MC = B.chat.id
	MM = B.message_id
	S = db[UI]['status']
	

	# db[UI]['message_id'].add(MM-1)
	# db[UI]['message_id'].add(MM)

	if (UI == admin_pv ) and (T in ['دریافت فایل های جدید' , 'ارسال لیست بلاکی' , 'دریافت فایل های گذشته' , 'پرداخت حقوق های درخواستی']) :

		if T == 'دریافت فایل های جدید' :
			if not os.path.exists('gmailes.txt'):
				await app.send_message(UI , 'فایل جدیدی وجود ندارد ')

			else :
				with open('gmailes.txt' , 'r+') as f:
					f = f.read()
					with open('totall.txt' , 'w') as s :
						s.write('\n')
						s.write(time.ctime())
						s.write('\n')
						s.write(f)

					async def progress(current, total):
						pp = f"{current * 100 / total:.1f}%"
						if pp != '100.0%':
							await asyncio.sleep(1)

					await app.send_document(UI , 'gmailes.txt' , progress=progress)
					
					os.remove('gmailes.txt') 

			
		elif T == 'ارسال لیست بلاکی' :
			db[UI]['status'] = 'sending_block_list'
			await app.send_message(UI , 'لطفا لیست بلاکی را با فرمت txt ارسال کنید')


		elif T == 'دریافت فایل های گذشته' :
			
			await app.send_document(admin_pv , 'totall.txt')


		elif T == 'پرداخت حقوق های درخواستی' :
			pass

	elif T == 'پروفایل':
		cur.execute(f'''SELECT all_gmails , awaiting_payment ,  accessible_account ,  Inaccessible_account FROM profile WHERE  id = '{UI}' ''' )
		ss = list(cur.fetchall()[0])
		all_gmails = ss[0]
		awaiting_payment =  ss[1]
		accessible_account = ss[2]
		Inaccessible_account = ss[3]
		await app.send_message(UI ,texts['profile'].format(all_gmails ,accessible_account ,Inaccessible_account , awaiting_payment ) , reply_markup=markups['profile'])
	
	elif T == 'انصراف' :
		db[UI]['status'] = 'yourwelcom'
		await app.send_message(UI ,'عملیات لغو شد')

	elif S == 'completing_informations':
		T = T.split('\n')
	

		if len(T) != 6 :
			await app.send_message(UI , 'لطفا مقادیر  را با ترتیب گفته شده سر هر خط وارد کنید')

		else:
			full_name =  T[0] 					
			phone_number = 	T[1]		
			city  =  T[2]			
			age  = 		T[3]			
			Bank_card_number = T[4] 		
			Bank_card_number_name 	= T[5]	
			cur.execute(f''' UPDATE profile SET full_name = '{full_name}' , phone_number = '{phone_number}'  , city = '{city}'  , age = '{age}'   , Bank_card_number = '{Bank_card_number}'  , Bank_card_number_name = '{Bank_card_number_name}' , check_infos = True   WHERE id = '{UI}' ''')
			con.commit()
			await app.send_message(UI , 'عملیات با موفقیت انجام شد' )
			db[UI]['status'] = 'yourwelcom'
		
	elif T == 'ثبت جیمیل':
		db[UI]['status'] = 'yourwelcom'
		await messager(UI , 'input_gmail_lagal' , MM )

	elif S == 'input_gmail' :
		db[UI]['status'] = ''

		await app.send_message(UI , texts['input_gmail_wait'] )
		await asyncio.sleep(0.2)
		dd = T.split('\n')
		true_count= 0

		for i in dd :

			ff = i.split(':')

			if T.count(ff[0]) > 1:
				db[UI]['multiple_gmail_repetitious_list'].append((i))

			elif (not '@gmail.com:' in i) or (ff[1] == ''):
				db[UI]['block_gmail_gramer_list'].append((i))

			else:
				cur.execute(f'''SELECT  id FROM gmails WHERE gmail = '{ff[0]}' ''' )
				ss = cur.fetchall()
				cur.execute(f'''SELECT  id FROM True_gmails WHERE gmail = '{ff[0]}' ''' )
				gg = cur.fetchall()
				cur.execute(f'''SELECT  id FROM Block_gmails WHERE gmail = '{ff[0]}' ''' )
				kk = cur.fetchall()
				print(kk)

				if ss == [] and  gg == [] and kk == [] :
					isvalid=validate_email(ff[0], verify=True)
					
					if isvalid == None :
						db[UI]['block_list'].append((ff[0]))

					elif isvalid == True :
						true_count += 1
						db[UI]['True_list'].append((ff[0] ,ff[1] , UI ))
				else:

					db[UI]['block_gmail_repetitious_list'].append((ff[0]))
					
			

		cur.executemany(f' INSERT INTO  gmails( gmail , password  , id )  VALUES(?,?,?) ' , db[UI]['True_list'])
		con.commit()
		cur.execute(f''' SELECT  Inaccessible_account , all_gmails FROM profile WHERE id = {UI}   ''')
		
		Y = cur.fetchall()[0]
		F = Y[0]
		L = Y[1]

		F += true_count
		L += true_count

		cur.execute(f' UPDATE profile SET  Inaccessible_account = {F} , all_gmails = {L}  WHERE id = {UI} '  )
		con.commit()
		
		

		if len(db[UI]['True_list']) != 0 :
			#getting from data base 
			#changing it
			#changing update in data base
			pass
			

		with open('gmailes.txt' , 'a') as f :
			for i in db[UI]['True_list']:
				f.write('\n')
				f.write(i[0] +':'+i[1])

		

		ss = '\n'.join(db[UI]['block_list'])
		hh = '\n'.join(db[UI]['block_gmail_repetitious_list'])
		oo = '\n'.join(db[UI]['block_gmail_gramer_list'])
		jj = '\n'.join(db[UI]['multiple_gmail_repetitious_list'])

		if oo == '' :
			oo = '___'
		if ss == '' :
			ss = '___'
		if hh == '' :
			hh = '___'
		if jj == '' :
			jj = '___'

		await app.send_message(UI , texts['input_gmail_result'].format(true_count ,oo, ss , hh , jj  ))

		db[UI].update( [('True_list' , []) , ('block_list' , []) , ('block_gmail_repetitious_list' , []) , ('block_gmail_gramer_list' , []) , ('multiple_gmail_repetitious_list' , [])])

	
	elif S[:12] == 'info_problme':
		
		await app.send_message( S[12:] , f'اطلاعات شما برای واریز حقوق  اشتباه است.\nلطفا آن ها را اصلاح کنید و درخواست مجدد واریز را ارسال کنید..\nتوضیحات ادمین :\n{T}' )
			
		await app.delete_messages(admin_pv ,[MM , MM-1] )	
		


		
@app.on_callback_query()
async def markup_getter(A:Client , B:Message):

	id  = B.id
	UI  = B.from_user.id
	D   = B.data
	MC  = B.message.chat.id
	MM  = B.message.message_id
	UFN = B.from_user.first_name
	ULN = B.from_user.last_name
	UUN = B.from_user.username
	MM = B.message.message_id
	S = db[UI]['status']


	if D == 'next' :
		await messager(UI , 'input_gmail' , MM )

	elif D == 'completing_informations' :
		await app.send_message(UI, texts['completing_informations'])
		db[UI]['status'] = 'completing_informations'

	elif D == 'getting_money':
		cur.execute(f''' SELECT check_infos FROM profile WHERE  id = '{UI}' AND check_infos = True ''')
		if  cur.fetchall() == []:
			
			await app.send_message(UI , texts['info_alert'])

		else:
			cur.execute(f''' SELECT Inaccessible_account , accessible_account  ,awaiting_payment ,  id , phone_number , Bank_card_number , Bank_card_number_name , full_name  FROM profile WHERE  id = '{UI}' ''')
			ss = list(cur.fetchall()[0])
			print(ss)
			
			

			if ss[2] == 0 :
				if ss[1] < 2 :
					await app.send_message(UI , 'مبلغ قابل برداشت شما  کمتر از 2 جیمیل است و نمی توانید برداشت کنید')
				else:
					ss[2] = ss[2] + ss[1]
					cur.execute(f' UPDATE profile SET  awaiting_payment = {ss[2]} , accessible_account = {0}    WHERE id = {UI} ')
					con.commit()

					await app.send_message( admin_pv , texts['paying_money'].format(ss[7] , ss[6]       ,  ss[5] ,ss[2]  )   , reply_markup= InlineKeyboardMarkup([ [InlineKeyboardButton('ارسال عکس واریز'  , f'payment_document{UI}')] , [InlineKeyboardButton('مشکل در اطلاعات' , f'info_problme{UI}' )    ] ]))
																					# name, card_number , id     , payment
					await app.send_message(UI , texts['getting_money'].format(ss[1]) , reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton('گزارش عدم واریز' , f'no_deposit{UI}')]]))

			
			else:
				ss[2] = ss[2] + ss[1]
				cur.execute(f' UPDATE profile SET  awaiting_payment = {ss[2]} , accessible_account = {0}    WHERE id = {UI} ')
				con.commit()

				await app.send_message( admin_pv , texts['paying_money'].format(ss[7] , ss[6]       ,  ss[5] ,ss[2]  )   , reply_markup= InlineKeyboardMarkup([ [InlineKeyboardButton('ارسال عکس واریز'  , f'payment_document{UI}')] , [InlineKeyboardButton('مشکل در اطلاعات' , f'info_problme{UI}' )    ] ]))
																				# name, card_number , id     , payment
				await app.send_message(UI , texts['getting_money'].format(ss[1]) , reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton('گزارش عدم واریز' , f'no_deposit{UI}')]]))



	if D[:10] == 'no_deposit' :
		print('yessssssss')
		cur.execute(f''' SELECT Inaccessible_account , accessible_account  ,awaiting_payment ,  id , phone_number , Bank_card_number , Bank_card_number_name , full_name  FROM profile WHERE  id = '{UI}' ''')
		ss = list(cur.fetchall()[0])

		await app.send_message( admin_pv , texts['user_protest_paying_money'].format(ss[7] , ss[6]       ,  ss[5] ,ss[2]  )   , reply_markup= InlineKeyboardMarkup([ [InlineKeyboardButton('ارسال عکس واریز'  , f'payment_document{UI}')] , [InlineKeyboardButton('مشکل در اطلاعات' , f'info_problme{UI}' )    ]  ]))
																				# name, card_number , id     , payment

		await app.send_message(UI , 'اعتراض شما به مدیریت ارسال شد.' )

	elif UI == admin_pv :
		if D[:12] == 'info_problme' : 
			print('yessssssss')
			db[UI]['status'] = D

			await app.send_message(admin_pv , 'لطفا درباره ی مشکل توضیح دهید.')

		elif D[:16] == 'payment_document' :
			print('yessssssss')
			db[UI]['status'] = D
			await app.send_message(admin_pv , 'عکس را ارسال کنید.')


print('Runing...')
app.run()










'''from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

print('Enter the gmailid and password')
gmailid, passWord = map(str, input().split())
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
	driver.implicitly_wait(15)

	loginBox = driver.find_element_by_xpath('//*[@id ="identifierid"]')
	loginBox.send_keys(gmailid)

	nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
	nextButton[0].click()

	passWordBox = driver.find_element_by_xpath(
		'//*[@id ="password"]/div[1]/div / div[1]/input')
	passWordBox.send_keys(passWord)

	nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
	nextButton[0].click()

	print('Login Successful...!!')
except:
	print('Login Failed')'''











'''

give me gmail in txt or message

are check the form?

is gmail syntax is valid?
is gmails are valid in google ?
is not gmails exists in data_base?


after 24 h we give money 


'''











