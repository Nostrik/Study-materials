import os
import requests


class ParserApiHotels:
    headers = {
        'x-rapidapi-host': "hotels4.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('RAPIDAPI-KEY-2')
    }
    url = 'https://hotels4.p.rapidapi.com/'

    def locations_search(self, query, locale="ru_RU"):  # пригодится
        """
        Search for related locations and suggestions
        Найдите похожие места и предложения
        :param query: REQUIRED Name of countries, cities, districts, places, etc…
        :param locale: OPTIONAL The language code
        :return:
        """
        url = "https://hotels4.p.rapidapi.com/locations/v2/search"
        querystring = {"query": query, "locale": locale, "currency": "USD"}
        response = requests.request("GET", url, headers=self.headers, params=querystring, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_meta_data(self):
        """
        Get locale meta data
        Получить метаданные локали
        """
        url = "https://hotels4.p.rapidapi.com/get-meta-data"

        response = requests.request("GET", url, headers=self.headers, timeout=10)
        print(response.text)

    def properties_list(self, landmarkids, destinationId, pageNumber='1', pageSize='25', checkIn='2020-01-08',
                        checkOut='2020-01-15', sortOrder='PRICE', locale='ru_RU', currency='RUB'):
        """
        List properties with options and filters
        Список свойств с параметрами и фильтрами
        :param landmarks field
        :param destinationId: REQUIRED The value of destinationId returned in locations/search endpoint
        :param pageNumber: REQUIRED The page number in which data is display
        :param pageSize: REQUIRED Total items returned in every requests (max 25)
        :param checkIn: REQUIRED The check-in date at hotel, formated as yyyy-MM-dd
        :param checkOut: REQUIRED The check-out date at hotel, formated as yyyy-MM-dd
        :param adults1: REQUIRED The number of adults in first room
        :param sortOrder: OPTIONAL One of the following is allowed
        :param locale: OPTIONAL The language code, get all supported languag
        :param currency: OPTIONAL The currency code
        :return:
        """
        global response_with
        url = "https://hotels4.p.rapidapi.com/properties/list"
        querystring = {"destinationId": destinationId, "pageNumber": pageNumber, "pageSize": pageSize,
                       "checkIn": checkIn, "checkOut": checkOut, "adults1": "1", "sortOrder": sortOrder,
                       "locale": locale, "currency": currency}
        querystring_with_landmarks = {"destinationId": destinationId, "pageNumber": pageNumber, "pageSize": pageSize,
                                      "checkIn": checkIn, "checkOut": checkOut, "adults1": "1", "sortOrder": sortOrder,
                                      "locale": locale, "currency": currency, "landmarkIds": "City center"}
        if landmarkids != 'City center':
            response_with = requests.request("GET", url, headers=self.headers, params=querystring, timeout=10)
        elif landmarkids == 'City center':
            response_with = requests.request("GET", url, headers=self.headers, params=querystring_with_landmarks,
                                             timeout=10)
        if response_with.status_code == 200:
            return response_with.json()
        else:
            return response_with.status_code

    def properties_get_details(self, find_id="424023", checkIn="2020-01-08", checkOut="2020-01-15", adults1="1",
                               currency="USD", locale="en_US"):  # пригодится

        """
        Get all available information of a property
        Получите всю доступную информацию о недвижимости
        :param find_id: REQUIRED The value of id field that returned in properties/list endpoint
        :param checkIn: OPTIONAL The check-in date at hotel
        :param checkOut: OPTIONAL The check-out date at hotel
        :param adults1: OPTIONAL The number of adults in the first room
        :param currency: OPTIONAL The currency code
        :param locale: OPTIONAL The language code
        :return:
        """
        url = "https://hotels4.p.rapidapi.com/properties/get-details"
        querystring = {"id": find_id, "checkIn": checkIn, "checkOut": checkOut, "adults1": adults1,
                       "currency": currency, "locale": locale}

        response = requests.request("GET", url, headers=self.headers, params=querystring, timeout=10)
        return response.json()

    def properties_get_hotel_photos(self, find_id='1178275040'):  # пригодится
        """
        Get all available photos of property
        Получите все доступные фотографии недвижимости
        :param find_id: REQUIRED The value of id field that received from
        :return:
        """
        url = "https://hotels4.p.rapidapi.com/properties/get-hotel-photos"
        querystring = {"id": find_id}

        response = requests.request("GET", url, headers=self.headers, params=querystring, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
