# Using regular expression to extract usernames
import re  

text= "The new registrations are potter709@gmail.com , elixir101@gmail.com. If you find any disruptions, kindly contact granger111@gamil.com or severus77@gamil.com "
# \S matches any non-whitespace character 
# @ for as in the Email 
# + for Repeats a character one or more times 
usernames= re.findall('(\S+)@', text)     
print("usernames :", usernames) 