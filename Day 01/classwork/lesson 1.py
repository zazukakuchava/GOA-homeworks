#name="zaza"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
#"ზაზა" არის ცვლადისთვის მნიშვნელობა

surname="kuchava"

#print(name)
#პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name="zaza"  #ეს არის str (string) ტიპის ცვლადი 
age=11  #ეს არის int (integer) მთელი რიცხვი
heigth= 155.5 #ეს არის float ტიპის ცვლადი(ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming=True #True ან False 
is_ugly= False #snakecase(უბრალოდ წერის სტილი სტანდარტული)

is_Ugly=False # ჯავასკრიპტული camelcase


print(name + " " + surname)

#სტრინგი არის ბრჭყალებსში მოქცეული სიმბოლოები
#print(name + age)

print(type(age))
print(type(name))
print(type(surname))
print(type(heigth))
print(type(knows_programming))

print(name +  " " + str(age) )