class duplicate:
  def dic():
    name=input("Enter a String:-")
    new_name={}
    for key in name:
      new_name[key]=new_name.get(key,0)+1
    print(f"duplicates with frequency{new_name}")
  dic()
