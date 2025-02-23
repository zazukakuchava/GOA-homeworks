#name="zaza"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
#"ზაზა" არის ცვლადისთვის მნიშვნელობა

surname="kuchava"

#print("name")
# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name="zaza"# ეს არის str(string) ტიპის ცვლადი
age=11 # ეს არის int(integer) მთელი რიცხვი
height=155,5 # ეს არის floar ტიპის ცვლადი(ათწილადი)
#boolean (bool) ტიპის ცვლადი

knows_programming=True #True ან False
is_ugly=False #snakecase (უბრალოდ წერის სტილი სტანდარტული)

is_Ugly=False # ჯავასკრიპტული camelcase

#სტრინგი არის ბრჭყალებში მოქცეული სიმბოლოები
print(name+surname )

print(type(name))
print(type(surname))
print(type(age))
print(type(height))
print(type(knows_programming))

print(name+surname+str(age))