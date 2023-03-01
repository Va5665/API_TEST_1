import requests
class Test_new_location():
    """Работа с новой локацией"""
    def test_create_new_location(self):
        """Создание новой локации"""
        base_url = "https://rahulshettyacademy.com" # база Url
        key = "?key=qaclick123"                      #Параметр для всех запросов                                       #
        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json"    #ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print("СТАТУС КОД: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Успешно!! Создана новая локация")
        else:
            print("Провал! Запрос ошибочный")
        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("СТАТУС КОД: " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верный")
        place_id = check_post.get("place_id")
        print("СТАТУС КОД: " + place_id)


        """Проверка создание новой локации"""
        get_resource = "/maps/api/place/get/json"

        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print("СТАТУС КОД: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!! Проверка создания новой локации прошла успешно")
        else:
            print("Провал! Запрос ошибочный")

        print(result_post.text)
        """Изменение новой локации"""



        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"

        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print("СТАТУС КОД: " + str(result_put.status_code))
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Успешно!! Изменения новой локации прошла успешно")
        else:
            print("Провал! Запрос ошибочный")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Сообщение: " + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Сообщение не верно")

        """Проверка изменения новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print("СТАТУС КОД: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Успешно!! Проверка изменения новой локации прошла успешно")
        else:
            print("Провал! Запрос ошибочный")
        check_address = result_get.json()
        check_msg_info = check_address.get("address")
        print("Сообщение: " + check_msg_info)
        assert check_msg_info == "100 Lenina street, RU"
        print("Сообщение не верно")

        """Удаление новой локации"""
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id

        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print("СТАТУС КОД: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        if result_delete.status_code == 200:
            print("Успешно!! Удаление новой локации прошла успешно")
        else:
            print("Провал! Запрос ошибочный")
        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение: " + check_status_info)
        assert check_status_info == "OK"
        print("Сообщение  верно")

        """Проверка удаления новой локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print("СТАТУС КОД: " + str(result_get.status_code))
        assert 404 == result_get.status_code
        if result_get.status_code == 404:
            print("Успешно!! Проверка удаления новой локации прошла успешно")
        else:
            print("Провал! Запрос ошибочный")
        check_msg = result_get.json()
        check_msg_info = check_msg.get("msg")
        print("Сообщение: " + check_msg_info)
        assert check_msg_info == "Get operation failed, looks like place_id  doesn't exists"
        print("Сообщение верно")
        print("Тестирование Test_new_location завершен успешно")

new_place = Test_new_location()
new_place.test_create_new_location()