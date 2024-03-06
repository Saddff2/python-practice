emps = {1:{'first_name':'Tamir','last_name':'Raiss','birth_date':'11/09/11', 'email':'tamir@gmail.com'},
2:{'first_name':'Tam33ir','last_name':'Raiss','birth_date':'11/05/11', 'email':'tami234r@gmail.com'},
3:{'first_name':'Tam22ir','last_name':'Raiss','birth_date':'11/01/11', 'email':'tami1234r@gmail.com'},
4:{'first_name':'Tam55ir','last_name':'Raiss','birth_date':'11/05/11', 'email':'tami543r@gmail.com'}}



def send_mail(mail_add, name):
    print(f'to {mail_add}, hi {name} have a good day')
    
    
def send_happy(emps, month):
    for emp in emps.values():
        if emp.get('birth_date', ' / / ').split('/')[1]==month:
            send_mail(emp.get('email'),emp.get('first_name'))

send_happy(emps, '05')
