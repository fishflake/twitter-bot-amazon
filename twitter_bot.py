#twitter bot program
#data pulled from amazon.com top selling products

#setup libraries
from twython import Twython
import csv
import random
from random import randrange

#twitter account auth keys -redacted-
twitter = Twython("REDACTED", "REDACTED",
                  "REDACTED", "REDACTED")

#populate verb list from file 
f = open('amazon_data.csv','rU')
u = open('amazon_data.csv','rU')

csv_f = csv.reader(f)
csv_u = csv.reader(u)

product_list = []
url_list = []

for row in csv_f:
    product_list.append(row[1])

for row in csv_u:
    url_list.append(row[0])

#select random product from list
random_product_1 = randrange(0,len(product_list))
random_product_2 = randrange(0,len(product_list))

#print random product
print product_list[random_product_1]
print url_list[random_product_1]

print product_list[random_product_2]
print url_list[random_product_2]

#post two products to twitter
twitter.update_status(status=product_list[random_product_1]+ ' ' +product_list[random_product_2])
#+ '  ' + url_list[random_product_1]+ '  ' + url_list[random_product_2]

#post two products with links
#twitter.update_status(status='<a href="' + url_list[random_product_1] +' ">' + product_list[random_product_1] + '</a> or <a href="' + url_list[random_product_2] + '">' + product_list[random_product_2] + '</a>')