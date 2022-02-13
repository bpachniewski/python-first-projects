import random
import string

#Password generator: weak , strong

#Domain
password_len = 8
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits
domain = lowercase + uppercase + punctuation + digits


weak_password = "".join(random.sample(lowercase, password_len))

#redundancy removed -> random_chars_domain = random.sample(domain, password_len)
strong_password = "".join(random.sample(domain, password_len))


print(f"Your weak password: {weak_password}", type(weak_password))
print(f"Your strong password: {strong_password}", type(strong_password))

