from pyfcm import FCMNotification

push_service = FCMNotification("AAAA9la-Ong:APA91bF3qZvgXmOAcXpDj4x0-f9wxPfg4L2gHA-mJwkEqsWuJTiychra2ACrYs5154vUN6iBY_luYmKXi7ooZYbJnfmFpymdlziyJ2uJpyHjpfvbhZlRvfgvysmcYF5ULmuuyJbiL8rw")
# proxy_dict = {
#           "http"  : "http://127.0.0.1",
#           "https" : "http://127.0.0.1",
#         }
# push_service = FCMNotification(api_key=" AAAA9la-Ong:APA91bF3qZvgXmOAcXpDj4x0-f9wxPfg4L2gHA-mJwkEqsWuJTiychra2ACrYs5154vUN6iBY_luYmKXi7ooZYbJnfmFpymdlziyJ2uJpyHjpfvbhZlRvfgvysmcYF5ULmuuyJbiL8rw ", proxy_dict=proxy_dict)
re = "dqIExZi19Sg1a_XaeO8dUQ:APA91bHrVTu-Z5Z_CiiYbBOEjRfmK9R-eZUyA6uJH8SucrsGlQxNOAklY-uUtjTAlOvznanE58eoDHdv-W0Wo0fhYRKfDcYrUIHMZrujwSjA2Wft-GpiQemLNzDqd8ucQ4U_Zoo-TqxM"
re2 = "f2_dqdyvnGrd-4JfnfoYSc:APA91bGfNRmxZeKx-qsHB7n5LFR9A_x0935XUr4mN_EE1pNuTgKQCt0Cu-8V6Y3xxQLpJCYSIYfUNylHfdwCzwyIlZ3nEy7zdjLcLm4bhaQgnCZoIjRgrPYyYdb6GIIVG3v8cLTa99Tf"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=re2,message_title=message_title, message_body=message_body)
print(result)