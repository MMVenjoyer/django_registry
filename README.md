# Переделываю реестр на django
Переписываю самостоятельно реестр спортивных учреждений до базового MVP, а дальше как пойдет)
Ничего необычного, просто интерес и желание научится чему-то новому.

Функционал в данный момент (Есть только бэк на drf):
1) Регистрация кастомных пользователей по email с дальнейшей верификацией вручную
2) Каждый верифицированный пользователь может добавить, редактировать, удалять только одно учреждение связанное с ним по OneToOneField
3) Каждый верифицированный пользователь может добавить, редактировать, удалять сколько угодно студентов, связанных с ним и учреждением по ForeignKey
3) Каждый верифицированный пользователь может добавить, редактировать, удалять сколько угодно тренеров, связанных с ним и учреждением по ForeignKey