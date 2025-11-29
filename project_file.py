class karbar:  #هدفمون از نوشتن اين کلاس گرفتن نام کاربري و رمز عبور براي بخش ثبت نام در سايته
    def __init__(self,username,password):
        self.username=username
        self.password=password

class Product: # نوشتن کلاس براي بخش محصولات 
    def __init__(self,name,price,discribtion,brand,count,code,categury):
        self.name=name
        self.price=int(price)
        self.discribtion=discribtion
        self.brand=brand
        self.count=int(count)
        self.code=code
        self.categury=categury
    def __repr__(self):
        return f'Product({self.name} - {self.price} تومان)'

    def __str__(self):
        return f'Product(نام کالا:{self.name} - قيمت کالا:{self.price} تومان - مارک کالا:{self.brand})'

    def detail(self): #اين بخشش رو براي نمايش مرتب شده جزئيات مصحول نوشتم
        print('\nاطلاعات محصول:')
        print('-' * 50)
        print(f'نام محصول   : {self.name}')
        print(f'برند        : {self.brand}')
        print(f'قیمت        : {self.price:,} تومان')
        print(f'موجودی      : {self.count} عدد')
        print(f'کد کالا     : {self.code}')
        print(f'دسته‌بندی   : {self.categury}')
        print('-' * 50)
        print('توضیحات:')
        i=0 #براي قسمت توضحات مصحول
        while i<len(self.discribtion):
            print(self.discribtion[i:i+50])
            i+=50
        print('-' * 50)


class Cart: #نوشتن يه کلاس براي بخش سبد خريد
    def __init__(self):
        self.items=[] 

    def add(self,product):
        self.items.append(product)

    def show(self):
        if not self.items:
            print('سبد خرید خالی است.')
            return
        print('       (سبد خريد)')
        i=1
        for p in self.items:
            print(i,'-',p.name,'-',p.price,'تومان') #استفاده از کلاس محصولات برا نمايش سبد خريد
            i+=1
        print('جمع کل:',self.total_price(),'تومان')
        print("-"*45)

    def remove(self,index):
        if index>=0 and index<len(self.items):
            removed=self.items.pop(index)
            print(f'محصول "{removed.name}" حذف شد.')
            print('-'*45)
        else:
            print('عدد وارد شده را چک نماييد.شماره نامعتبر!')

    def total_price(self):
        return sum(p.price for p in self.items)

    def is_empty(self): #چک کنيم که ايا سبد خريد خالي هست يا نه
        return len(self.items)==0

    def clear(self): # اين تابع هم براي خالي کردن سبد خريد بعد از پرداخت
        self.items=[]


import random
class Factore:
    def __init__(self,products):
        self.products=products
        self.number=random.randint(100000,999999)  #با استفاده از کتابخونه رندوم،يه عدد تصادفي 6 رقمي براي شماره فاکتور نشوتم
        self.date = 'تاریخ ' #به جهت صرف نمايش يه تاريخ اين استفاده شده
        self.total=sum(p.price for p in products)

    def show(self):
        print('(فاکتور)')
        print(f'شماره فاکتور:{self.number}')
        print(f' ثبت تاریخ:{self.date}')
        print('-'*45)
        i=1
        for p in self.products:
            print(i,'-',p.name,'-',p.price,'تومان')
            i+=1
        print(''*40)
        print('جمع کل:',self.total,'تومان')
        print('-'*40)
    def save_to_file(self,code_peygiri):
        with open('sefareshat.txt','a',encoding='utf-8') as f: #از متود aستافده کردم چون اگر وجود نداشت ايحاد ميکنه و چون سفارشات قبلي هست،ميتونه بهش اضافه کن.
            f.write(f'{self.number},{self.date},{self.total} تومان\n')
            for p in self.products:
                f.write(f' - {p.name} ({p.price} تومان)\n')
            f.write(f'کد پیگیری: {code_peygiri}\n')    
            f.write('-'*40+'\n')
            
def sabtenam(): #يه تابع  براي ثبت نام و اجاد يه فايل براي قارار گرفتن نام کارري و رمز مشتري ها توي اون
    username=input('نام کاربری: ')
    password=input('رمز عبور: ')
    with open('sabtenam.txt','a',encoding='utf-8') as f:
        f.write(username+','+password+'\n')
    print('ثبت نام با موفقیت انجام شد.')
    return karbar(username,password)
def vorod(): #فرقش با تابع بايي توي اينه که براي لاگين کسي هست که قبلا ثبت نام کرده
    username=input('نام کاربری: ')
    password=input('رمز عبور: ')
    try:
        with open('sabtenam.txt','r',encoding='utf-8') as f:
            for line in f:
                line=line.strip()
                parts=line.split(',')
                if len(parts)==2:
                    if parts[0]==username and parts[1]==password:
                        print('ورود با موفقیت انجام شد.')
                        return karbar(username,password)
        print('نام کاربری یا رمز اشتباه است.')
    except FileNotFoundError:
        print('هیچ کاربری ثبت نشده است.')
    return None
  
menu={1:'محصولات',2:'راهنماي استفاده از سايت',3:'سبد خريد',4:'درباره ما',5:'تماس با ما',6:'سفارشات قبلي',7:'پشتيباني',8:'ورود/ثبت نام',9:'خروج از حساب کاربري',0:'خروج'}
mahsolat=[]  #يه ليست خالي درست کرديم تا محصولات رو از فايل خونده شده بريزيم اينحا 
cart=Cart() #تعريف يه مجموعه خالي براي سبد خريد
karbar_vared_shode=None #براي اينکه بررسي کنيم کسي وارد حساب کاربري شده يا نه.
peygham_khoroji=None    #اولش براي پيام خروج به مشکل خوردم.براي همين مجبور شدم يه متغير حديد براش تعريف کنم
code_takhfif={'OFF10':10,'OFF20':20,'OFF30':30}  #تعغريف يه ديکشنري براي کد تخفيف
with open('mahsolat.csv','r',encoding='utf-8') as f:
    for line in f:
        parts=line.split(',')
        if len(parts)==7:
            y=Product(parts[0],parts[1],parts[2],parts[3],parts[4],parts[5],parts[6])
            mahsolat.append(y)

while True:
    if peygham_khoroji!=None:
        print(peygham_khoroji)
        peygham_khoroji=None
    elif karbar_vared_shode!=None:
        print(f' کاربر وارد شده: {karbar_vared_shode.username}')
    else:
        print(' هنوز وارد حساب کاربری نشده‌اید.')


    print('           (منوی اصلی)')
    print('-'*45)
    for key,value in menu.items():   #حلفه روي کليد و ارزش هاي ديکشنري براي دريافت منوي اصلي
        print(str(key)+'-'+value)
    print('-'*45)

    choice=input('لطفا گزينه مورد نظر را انتخاب کنيد: ')
    if not choice:
        print('ورودی نادرست!')
        continue
    try:
        x=int(choice)
    except ValueError:
        print('ورودی نادرست!')
        continue
    

    if x not in menu:
        print('لطفا فقط بين اعدا 0 تا 9 يک گزينه را اتخاب کنيدد!')
        continue
    
    if x==1:                          #اين بخش براي نوشتن شرايط اتخب گزينه محصولات هست
        print('-'*45)
        print('           (دسته‌بندی محصولات)')
        while True:
            categurys=[]     #ساختن يه ليست خالي براي ايجاد دسته بندي
            for p in mahsolat:
                c=p.categury
                if c not in categurys:
                    categurys.append(c)

            if len(categurys)==0:
                print('هیچ دسته‌بندی‌ای پیدا نشد.')
                input('برای بازگشت Enter را بزنید...')
                break

            print('-'*45)
            j=1
            for cat in categurys:
                print(j,'-',cat)
                j+=1
            print('-'*45)

            y=input('براي بازگشت به منو اصلي کليد q را بزنيد: ')
            if y=='q':
                break
            if not y.isdigit():
                print('ورودی نادرست!')
                continue

            n=int(y)
            if n<1 or n>len(categurys):  #شرط براي چگ کردن شماره وارد شده دسته بندي
                print('عدد نامعتبر!')
                continue

            selected_cat=categurys[n-1]
            products_in_cat=[]  #يه ليست خالي براي ريختن محصولات اون دسته اي که انتخاب ميشن.
            for p in mahsolat:
                if p.categury==selected_cat:
                    products_in_cat.append(p)

            if len(products_in_cat)==0:
                print('هیچ محصولی در این دسته نیست.')
                continue

            while True:
                print('-'*104)
                print(f'| {"ردیف":^6} | {"نام محصول":^30} | {"قیمت (تومان)":^18} | {"برند":^20} | {"موجودی":^10} |')
                print('-'*104)

                i = 1
                for p in products_in_cat:
                    print(f'| {i:^6} | {p.name:<30} | {p.price:^18,} | {p.brand:^20} | {p.count:^10} |')
                    i += 1

                print('-'*104)

                sel=input('براي بازگشت به منو قبلي،کليد q را بزنيد: ')
            
                if sel=='q':
                    break
                
                if not sel.isdigit():
                    print('ورودی نادرست!')
                    continue

                num=int(sel)
                if num<1 or num>len(products_in_cat):
                    print('عدد نامعتبر!')
                    continue

                selected_product = products_in_cat[num-1] #اين بخش براي محصولات انتخاب شده و اضافه کردن به سبد خريد هستش
                selected_product.detail()

                while True:
                    print('1- افزودن به سبد خرید')
                    print('2- بازگشت به لیست محصولات')
                    choice=input('انتخاب شما: ')
                    if choice=='1':
                        if karbar_vared_shode==None:
                            print('برای افزودن به سبد خرید باید وارد حساب کاربری شوید.')
                        else:
                            cart.add(selected_product)
                            print('محصول با موفقیت به سبد خرید اضافه شد.')                        
                            break                    
                    elif choice=='2':
                        break
                    else:
                        print('ورودی نامعتبر!')

        continue

    if x==2:                              #اين بخش براي استفاده راهنماي استفاده از سايت هست
        try:
            with open('user_guide.txt','r',encoding='utf-8') as f:  #باز کردن قايل notepad
                text=f.read()
                print(text)
        except FileNotFoundError:
            print('فایل user_guide.txt یافت نشد!')
        except:
            print('خطا در خواندن فایل راهنما.')    
        
        while True:
            back=input('برای بازگشت به منوی اصلی کلید q را بزنید: ')
            if back=='q':
                break
        continue


    if x==3:                             #اين بخش براي تعريف شرايط سبد خريد هست
        while True:
            print('-'*45)
            print('          (سبد خريد)')
            print('1- مشاهده سبد خرید')
            print('2- حذف محصول')
            print('3- صدور فاکتور')
            print('4- پرداخت فاکتور')
            print('5- بازگشت')
            choice=input('لطفا گزينه مورد نظرتون رو وارد کنيد.: ')
            if choice=='1':
                if len(cart.items)==0:
                    print('سبد خرید شما خالی است.')
                else:
                    print('-'*100)
                    print(f'| {"ردیف":^6} | {"نام محصول":^30} | {"قیمت واحد":^18} | {"تعداد":^8} | {"قیمت کل":^20} |')
                    print('-'*100)

                    total=0
                    i=1
                    for p in cart.items:
                        gheymat_kol=p.price
                        total+=gheymat_kol
                        print(f'| {i:^6} | {p.name:<30} | {p.price:^15,} | {"1":^8} | {gheymat_kol:^20,} |')
                        i+=1

                    print('-'*100)
                    print(f'{"جمع کل سبد خرید":<70} : {total:,} تومان')
 
            elif choice=='2':
                cart.show()
                if cart.is_empty(): 
                    continue
                remove=input('شماره محصولی که میخوای حذف کنی: ')  #علت اينکه از int استافه نکردم اينه که ممکنه برنامه خطا بده..
                if remove.isdigit():  #پس اينجا اوومدم با اين متد چگ کردم که حتما رشته گرفته شده من عدد صحيح باشه 
                    cart.remove(int(remove)-1)
                else:
                    print('ورودی نامعتبر!')
            elif choice=='3':
                if cart.is_empty():
                    print('سبد خرید خالی است.')
                    continue
                fct=Factore(cart.items)
                fct.show()
            elif choice=='4':
                if cart.is_empty():
                    print('سبد خرید خالی است.')
                    continue

                fct = Factore(cart.items)
                fct.show()
                print('-'*104)
                print(f'| {"ردیف":^6} | {"نام محصول":^30} | {"قیمت واحد":^15} | {"تعداد":^8} | {"قیمت کل":^20} |')
                print('-'*104)

                i=1
                total_price=0
                for p in cart.items:
                    gheymat_kol=p.price
                    total_price+=gheymat_kol
                    print(f'| {i:^6} | {p.name:<30} | {p.price:^15,} | {"1":^8} | {gheymat_kol:^20,} |')
                    i+=1

                print('-'*104)

                while True:
                    code=input('اگر کد تخفیف دارید وارد کنید، در غیر اینصورت Enter بزنید: ')
                    code=code.strip().upper() #با توجه به اينکه مهم نيست کد تخفيف رو بزرگ يا وچيک وارد ميکنه،بعدش خومون با upper بزرگش ميکنيم
                    if code=='':
                        break
                    if code in code_takhfif: #ين بخش براي محاسبه قيمت با از اعمال کد تخفي
                        darsad=code_takhfif[code]
                        takhfif=(fct.total*darsad)//100
                        fct.total -= takhfif
                        print(f'کد تخفیف اعمال شد. مبلغ {takhfif} تومان از فاکتور شما کم شد.')
                        break
                    else:
                        if code!='':
                            print('کد تخفیف نامعتبر است.')
                            tekrar=input(':اگر ميخواي دوباره امتحان کني y رو بزن و در صورت ادامه،n رو بزن')
                            if tekrar!='y': #نامساوي گذاشتم تا هر چيزي غير از y گذاشت بره مرحله بعدي
                                break
                
                print('        روش پرداخت:')
                print('1- پرداخت با کارت بانکی')
                print('2- پرداخت در محل')
                print('3- انصراف')
                z=input('انتخاب روش پرداخت: ')  # همون گزینۀ روش پرداخت خودت

                if z=='1' or z=='2':
                    address=input('لطفاً آدرس دقیق محل دریافت را وارد کنید: ')
                    print('-'*45)

                    hazine_ersal=0
                    tozihat_ersal=''

                    if 'تهران' in address:
                        print('        روش‌های ارسال:')
                        print('1-  ارسال با پيک (هزينه: 30000 تومان)')
                        print('2- ارسال با پست (هزينه: 20000 تومان)')
                        ersal=input('انتخاب روش ارسال: ')
                        if ersal=='1':
                            hazine_ersal=30000
                            tozihat_ersal='ارسال با پیک - تهران - کمتر از 24 ساعت'
                        elif ersal=='2':
                            hazine_ersal=20000
                            tozihat_ersal='ارسال با پست - تهران/سایر شهرها - 2 تا 4 روز کاری'
                        else:
                            print(' ورودي نامعتبر')
                            continue
                    else:
                        hazine_ersal=20000
                        tozihat_ersal='ارسال با پست - خارج از تهران - 2 تا 4 روز کاری'

                    mablagh_nahayi=fct.total+hazine_ersal
                    print('-'*45)
                    print(f' اطلاعات ارسال:{tozihat_ersal}')
                    print(f' هزينه ارسال:{hazine_ersal} تومان')
                    print(f'قیمت نهایی قابل پرداخت:{mablagh_nahayi} تومان')
                    print('-'*45)

                    taeed=input('برای اتصال به درگاه پرداخت عدد 1 و برای انصراف عدد 0 را وارد کنید: ')
                    if taeed=='1':
                        print('در حال اتصال به درگاه پرداخت...')
                        fct.total=mablagh_nahayi
                        code_peygiri=str(random.randint(1000000000,9999999999))
                        if karbar_vared_shode==None:# اينجا بررسي ميکنيم که کاربر وارد حساب شده يا نه
                            print('برای ثبت سفارش باید وارد حساب کاربری شوید.')
                        else:
                            nam_file=f'orders_{karbar_vared_shode.username}.txt' #اپه وارد حساب شده بود،به اسم خودش يه قايل درست ميکنيم.
                            with open(nam_file,'a',encoding='utf-8') as f:
                                f.write(f'{fct.number},{fct.date},{fct.total} تومان\n')
                                for p in fct.products:
                                    f.write(f' - {p.name} ({p.price} تومان)\n')
                                f.write(f'کد پیگیری: {code_peygiri}\n')    
                                f.write('-'*40+'\n')

                        cart.clear()
                        print(' پرداخت با موفقیت انجام شد.')
                        print('کد پيگيري شما:',code_peygiri)
                    elif taeed=='0':
                        print('پرداخت لغو شد. بازگشت به سبد خرید.')
                    else:
                        print('ورودی نامعتبر! بازگشت به سبد خرید.')
                    

            elif choice=='5':
                break
            else:
                print('گزینه نامعتبر!')
        continue
    if x==4:                                 #اين بخش براي نوشتن شرايط درباره ما هست.
        print('       (درباره ما)')
        print('فروشگاه ماجراجویان کوهستان، ارائه‌دهنده بهترین تجهیزات کوهنوردی و طبیعت‌گردی است.')
        print('از کفش و کوله گرفته تا چادر و ابزار ایمنی، همراه مطمئن ماجراجویان در مسیرهای سخت.')
        print('تجربه خریدی آسان، امن و تخصصی را با ما داشته باشید.')
        print('-'*45)
        while True:
            back=input('برای بازگشت به منوی اصلی کلید q را بزنید: ')
            if back=='q':
                break
        continue 
        
    if x==5:                                   #اين بخش براي نوشتن شرايط تماس با ما هست.
        print('(تماس با ما)')
        print('برای پشتیبانی و سوالات:')
        print(' تلفن: 021-22264466')
        print('ایمیل: support@mountaingear.com')
        print(' آدرس:تهران،ميدان منيريه،پلاک 1539')
        print(' ساعات پاسخگويي و مراجعه حضوري:همه روزه از ساعت 9 صبح تا 8 شب')
        print('-'*45)
        while True:
            back=input('برای بازگشت به منوی اصلی کلید q را بزنید: ')
            if back=='q':
                break
        continue

    if x==6:                                 # اين بخش براي نمايش سفارشات قبلي هست
        print('        (سفارشات قبلی شما)')
        print('-'*45)
        if karbar_vared_shode==None:  #اينجا چک ميکنم کاربر وارد شده يا نه
            print('برای مشاهده سفارشات باید وارد حساب کاربری شوید.')
        else:
            nam_file=f'orders_{karbar_vared_shode.username}.txt' #اگه وارد شده بود يه فايل هست که به اسم خودش سفارشاتش داخل هست از قبل
            try:
                with open(nam_file,'r',encoding='utf-8') as f:
                    lines=f.read()
                    print(lines)
            except FileNotFoundError:
                print('شما هنوز سفارشی ثبت نکرده‌اید.')
                
        while True:
            back=input('برای بازگشت به منوی اصلی کلید q را بزنید: ')
            if back=='q':
                break
        continue
    if x==7:                                 # اين بخش براي پشتيباني و ثبت تیکت هست
        print('        (ارسال تیکت پشتیبانی)')
        print('-'*45)
        if karbar_vared_shode==None: #اپه کاربر وارد شده بود به صورت خودکار اسمش مياد ولي اگه وارد نشده بود دستي ميتونه وارد کنه
            name=input('نام شما: ')
        else:
            name=karbar_vared_shode.username

        subject=input('موضوع پیام: ')
        message=input('متن پیام: ')

        try:
            with open('tickets.txt','a',encoding='utf-8') as f:
                f.write(f'نام: {name}\n')
                f.write(f'موضوع: {subject}\n')
                f.write(f'پیام: {message}\n')
                f.write('-'*40+'\n') 
            print('تیکت شما با موفقیت ثبت شد. تیم پشتیبانی در اسرع وقت پاسخ خواهد داد.')
        except:
            print(' خطا در ثبت تیکت! لطفاً بعداً دوباره تلاش کنید.')

        while True:
            back=input('برای بازگشت به منوی اصلی کلید q را بزنید: ')
            if back=='q':
                break
        continue


    if x==8:                               #اين بخش براي ورود يا ثبت نام کاربره
        print('       (ورود/ثبت‌نام)')
        print('1- ورود')
        print('2- ثبت نام')
        y=input('انتخاب شما: ')
        if y=='1':
            karbar_vared_shode=vorod()
        elif y=='2':
            karbar_vared_shode=sabtenam()
        else:
            print('ورودی نامعتبر!')
        continue
    
    if x==9:                              #اين بخش براي خروج از حساب کاربري هستش
        if karbar_vared_shode!=None:
            peygham_khoroji=f'خروج از حساب کاربری {karbar_vared_shode.username} انجام شد.'
            karbar_vared_shode=None
        else:
            peygham_khoroji='شما هنوز وارد حساب کاربری نشده‌اید.'
        continue

      
    if x==0:                                #اين شرط براي خروج از برنامه
        print('خروج از برنامه!')
        break
