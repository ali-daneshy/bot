
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , KeyboardButton


stickers = {
    'yourwelcom' : None,
    'input_gmail_lagal' : None ,
    'input_gmail' : None,
    'profile' : None
}

admin_markups = {
    'yourwelcom' : ReplyKeyboardMarkup([    [KeyboardButton('دریافت فایل های جدید')  , KeyboardButton('ارسال لیست بلاکی') ] ,
                                            [KeyboardButton('دریافت فایل های گذشته') , KeyboardButton('پرداخت حقوق های درخواستی')] ,
                                            [KeyboardButton('ثبت جیمیل') , KeyboardButton('پروفایل')] ,
                                            [KeyboardButton('انصراف')] ])
}

markups = {
    # 'input_gmail' : InlineKeyboardMarkup([[InlineKeyboardButton()]])

    'yourwelcom' : ReplyKeyboardMarkup([[KeyboardButton('ثبت جیمیل')] , [KeyboardButton('پروفایل') , KeyboardButton('انصراف')]]),
    'input_gmail_lagal' : InlineKeyboardMarkup([[InlineKeyboardButton('ادامه' , 'next')]]),
    'profile' : InlineKeyboardMarkup([  [InlineKeyboardButton('دریافت حقوق' , 'getting_money')] , 
                                        [InlineKeyboardButton('تکمیل یا ویرایش اطلاعات' , 'completing_informations')]]),
     # url ********
    'problme' : InlineKeyboardMarkup([  [InlineKeyboardButton('گزارش عدم واریز'  ,'no_deposit'  )] ])  , # url ********
    'next_text_input_gmail' : InlineKeyboardMarkup([[InlineKeyboardButton('ادامه' , 'next_text_input_gmail')]])
}

texts = {
    'input_gmail' : 'لطفا جیمیل را وارد کنید',
    'yourwelcom' : 'به ربات ما خوش آمدید',
    'input_gmail_lagal' : 'برای وارد کردن  هر جیمیل باید نکات زیر را رعایت کنید\n\nابتدا جیمیل را می نویسید و علامت (:) را می گذارید بعد رمز جیمیل را می نویسید.\n\nمثال : \ncaspian@gmail.com:123456\nrobotman@gmail.com:123456789\n\nبرای ارسال جیمیل \nیا می توانید جیمیل هارا در هر خط یک فایل txt بنویسید یا می توانید جیمیل ها را در هر خط کامنت بگذارید و ارسال کنید \n\nحتما بعد از ارسال منتظر نتیجه باشید\n\n. ',
    'profile' :  ' کل جیمل ها : {} \nجیمیل های حساب قابل برداشت : {} \nجیمیل هایحساب  غیر قابل برداشت : {} \nدر انتظار پرداخت : {} ' ,
    'input_gmail_result' : 'تعداد جیمیل های درست = {} \nمشکل نوشتاری : \n{}\nجیمیل های بلاکی :‌\n{} \nجیمیل های تکراری :‌\n{} \n جیمیل هایی که بیشتر از یک بار وارد نوشته شده اند (ثبت نشده) :\n{}\n.',
    'input_gmail_wait' : 'لطفا منتظر بمانید...',
    'input_gmail_alarm' : 'لطفا در وارد کردن جیمیل از قواعد گفته شده استفاده کنید',
    'getting_money' : '''درخواست دریافت حقوق شما به تعداد "{}"  جیمیل ثبت شد و نتیجه به شما اعلام می شود''' ,
    'info_alert' : 'شما هنوز اطلاعات خود را کامل نکرده اید \nبرای این کار  در قسمت تکمیل اطلاعات مشخصات خود را وارد کنید.' , 
    'paying_money' : 'کاربر با نام کاربری "{}" و نام کارت "{}" و شماره کارت "{}" درخواست دریافت مبلغ حقوق به تعداد "{}"جیمیل را می دهد .' , 
    'completing_informations' : 'لطفا اطلاعات خود را به ترتیب زیر وارد کنید:\nنام\nشماره همراه\nشهر\nسن\nشماره کارت\nنام صاحب حساب\n\n' ,
    'filnall_gmail_result' : 'کاربر گرامی تعداد {} عدد از جیمیل های شما مورد قبول قرار گرفته و به حساب قابل برداشت شما ارسال شده.\nهمچنین جیمیل های غیر قابل قبول به شرح زیر هستند :\n{}' ,
    'user_protest_paying_money' : 'کاربر با نام کاربری "{}" و نام کارت "{}" و شماره کارت "{}" نسبت به درخواست دریافت مبلغ حقوق به تعداد "{}"جیمیل **اعتراض** دارد. .' 


}
