import unittest
from mock import patch
from marta import app
from marta.vehicles import Train


class InvokeSkill(unittest.TestCase):
    @patch('marta.api.get_trains')
    def test_invoke_skill_success(self, mock):
        event = {
            "version": "1.0",
            "session": {
                "new": True,
                "sessionId": "amzn1.echo-api.session.de056596-afd9-4768-b5f7-f4f2545cbed8",
                "application": {
                    "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                },
                "user": {
                    "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                }
            },
            "context": {
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                    },
                    "device": {
                        "deviceId": "amzn1.ask.device.AEDSFL673DEPCNMPSN5J54IHE3XMXD574EPPEGFXYEY2ARMWBWMYEQ7I4GBYSSE5YDLFIZ6ULNRK2EYM3KH5YNAIB5OTZSARRFC4BJOA2BQNPZWZPH7VDDKNDCYL5MSPTCF2BGGMHIAINLJ32WY7CZQ7GIMU4WQCP24RICA6CXFWDEPRXU3BM",
                        "supportedInterfaces": {}
                    },
                    "apiEndpoint": "https://api.amazonalexa.com",
                    "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjliMzZiMTMyLTk5MmMtNGE2Zi05OTg1LTI2ZjE3MzNlZDI1YiIsImV4cCI6MTUzOTkxMTQ3OCwiaWF0IjoxNTM5OTA3ODc4LCJuYmYiOjE1Mzk5MDc4NzgsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVEU0ZMNjczREVQQ05NUFNONUo1NElIRTNYTVhENTc0RVBQRUdGWFlFWTJBUk1XQldNWUVRN0k0R0JZU1NFNVlETEZJWjZVTE5SSzJFWU0zS0g1WU5BSUI1T1RaU0FSUkZDNEJKT0EyQlFOUFpXWlBIN1ZEREtORENZTDVNU1BUQ0YyQkdHTUhJQUlOTEozMldZN0NaUTdHSU1VNFdRQ1AyNFJJQ0E2Q1hGV0RFUFJYVTNCTSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHVk9CQTdGTkFVRzJMNVNPWEJIRDdGSVlQWVBQV0pNUDZDWFFTRUJZRFU1UVlRUENWUlpXSUtGVU02TkNFVU5QVElNUDZITVBQU1hJSkQzSEs0SzczWkRKNUJQQlY3NzVRU0c1UlBHSFFPVlRFN0tRR1NQRkVDQlpXTEZRWDROV09GNjJHWlJKR0FMNzJPV0RKS1RTTzZHSjVOSFYySEhCN1pUVUNLNk4zV09RQzRNRktCU1pBU0NTSUxaUVZIRE1KQkU1N1hNVDZGQ0VXUSJ9fQ.Operr0oQpTA7DhTkU4O0klTFbnzwxGL8WrrGVHMzxgx2Rc8fBWnowBh6mjNOwTvCyIUGHE1i_-KBpHE3dcE1GLFkjpWa5kYJx74DXFI1Ni7zY_zX0Q551ToQTUqw3sPRZ0Q1sVQxWVrZMhPqWjv9kfNv56S2Q_P0oSZx6kS_m8vhnxBk2YGz3PYM4Ucjemz2nl3YYW5fqM-9oNUE_VcT204bFWxAM4pN6EnIQauBik_zvl0Cp_ILpa8rE7fSjeVKEuWa0tIM0V3qImWHBf6vCn4k7-J33su-707PADNze-XfNZndmu22lpk1kI5SWreTK0eMpu9smn5hc-20bnajgQ"
                }
            },
            "request": {
                "type": "LaunchRequest",
                "requestId": "amzn1.echo-api.request.0622fd17-1438-40b3-b513-e5f30e873143",
                "timestamp": "2018-10-19T00:11:18Z",
                "locale": "en-US",
                "shouldLinkResultBeReturned": False
            }
        }
        response = app.lambda_handler(event=event, context=None)
        self.assertEquals("Welcome to Marta train tracker. Say when is the next train from Chamblee to Five Points", response['response']['outputSpeech']['text'])


class GetTrainArrivalByDestinationSuccess(unittest.TestCase):
    @patch('marta.api.get_trains')
    def test_get_train_arrival_success(self, mock):
        mock.return_value = create_mock_train_response()
        event = {
            "version": "1.0",
            "session": {
                "new": False,
                "sessionId": "amzn1.echo-api.session.f1837415-b25a-4b3c-9ee3-4e4957a02550",
                "application": {
                    "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                },
                "user": {
                    "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                }
            },
            "context": {
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                    },
                    "device": {
                        "deviceId": "amzn1.ask.device.AEDSFL673DEPCNMPSN5J54IHE3XMXD574EPPEGFXYEY2ARMWBWMYEQ7I4GBYSSE5YDLFIZ6ULNRK2EYM3KH5YNAIB5OTZSARRFC4BJOA2BQNPZWZPH7VDDKNDCYL5MSPTCF2BGGMHIAINLJ32WY7CZQ7GIMU4WQCP24RICA6CXFWDEPRXU3BM",
                        "supportedInterfaces": {}
                    },
                    "apiEndpoint": "https://api.amazonalexa.com",
                    "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjliMzZiMTMyLTk5MmMtNGE2Zi05OTg1LTI2ZjE3MzNlZDI1YiIsImV4cCI6MTUzODUzNTc5NiwiaWF0IjoxNTM4NTMyMTk2LCJuYmYiOjE1Mzg1MzIxOTYsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVEU0ZMNjczREVQQ05NUFNONUo1NElIRTNYTVhENTc0RVBQRUdGWFlFWTJBUk1XQldNWUVRN0k0R0JZU1NFNVlETEZJWjZVTE5SSzJFWU0zS0g1WU5BSUI1T1RaU0FSUkZDNEJKT0EyQlFOUFpXWlBIN1ZEREtORENZTDVNU1BUQ0YyQkdHTUhJQUlOTEozMldZN0NaUTdHSU1VNFdRQ1AyNFJJQ0E2Q1hGV0RFUFJYVTNCTSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHVk9CQTdGTkFVRzJMNVNPWEJIRDdGSVlQWVBQV0pNUDZDWFFTRUJZRFU1UVlRUENWUlpXSUtGVU02TkNFVU5QVElNUDZITVBQU1hJSkQzSEs0SzczWkRKNUJQQlY3NzVRU0c1UlBHSFFPVlRFN0tRR1NQRkVDQlpXTEZRWDROV09GNjJHWlJKR0FMNzJPV0RKS1RTTzZHSjVOSFYySEhCN1pUVUNLNk4zV09RQzRNRktCU1pBU0NTSUxaUVZIRE1KQkU1N1hNVDZGQ0VXUSJ9fQ.efcmQ0DewNIs9d9Pkv2k9AB7jvaGZUrm1y1BCfvg5kHF2heydtHtQbSCN831GTsXrJxh9iY_C6iBQD6mCoUtYLKrLKz9PVG4ZlgU2YI1LFUdY4V4XFFu6Mf5MmxkYBsb-I2PLRS20mFLeHg2MGYJ8egBwJ8E6hJLUXw_5a81PwBdGrqln2UWro_44EqEDlOsMFKn2hUTqfasFT-8zxXa0frHCNVPWECHu2o55d4j2IPQTL0AA1AxgEwQkyuBJrtE0w3r28d69iuLykI-_hyL1sqUdZ4tslX4z3y3OshgGyEubKuUhKd37zQzoF6tgReeg_STHr6oLwPcDb10Cueg1Q"
                }
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.51285d8d-a014-43b6-8120-c97b962c9453",
                "timestamp": "2018-10-03T02:03:16Z",
                "locale": "en-US",
                "intent": {
                    "name": "GetTrainArrivalByDestinationIntent",
                    "confirmationStatus": "NONE",
                    "slots": {
                        "destination_station": {
                            "name": "destination_station",
                            "value": "5 points",
                            "resolutions": {
                                "resolutionsPerAuthority": [
                                    {
                                        "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b.LIST_OF_MARTA_STATIONS",
                                        "status": {
                                            "code": "ER_SUCCESS_MATCH"
                                        },
                                        "values": [
                                            {
                                                "value": {
                                                    "name": "Five Points Station",
                                                    "id": "ac61bde2e2de91cde069e6a9e6ba9955"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            "confirmationStatus": "NONE"
                        },
                        "departure_station": {
                            "name": "departure_station",
                            "value": "chamblee",
                            "resolutions": {
                                "resolutionsPerAuthority": [
                                    {
                                        "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b.LIST_OF_MARTA_STATIONS",
                                        "status": {
                                            "code": "ER_SUCCESS_MATCH"
                                        },
                                        "values": [
                                            {
                                                "value": {
                                                    "name": "Chamblee Station",
                                                    "id": "162ce708438b2a112a16946e45bc5890"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            "confirmationStatus": "NONE"
                        }
                    }
                }
            }
        }
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "The next train from Chamblee Station to Five Points Station arrives at 11:42:02",
            response['outputSpeech']['text'])
        self.assertTrue(response['shouldEndSession'])

    @patch('marta.api.get_trains')
    def test_get_train_arrival_failure(self, mock):
        mock.return_value = '10'
        event = {
            "version": "1.0",
            "session": {
                "new": False,
                "sessionId": "amzn1.echo-api.session.8f9829e3-311c-453c-8b69-93699022dfc7",
                "application": {
                    "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                },
                "user": {
                    "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                }
            },
            "context": {
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b"
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AGVOBA7FNAUG2L5SOXBHD7FIYPYPPWJMP6CXQSEBYDU5QYQPCVRZWIKFUM6NCEUNPTIMP6HMPPSXIJD3HK4K73ZDJ5BPBV775QSG5RPGHQOVTE7KQGSPFECBZWLFQX4NWOF62GZRJGAL72OWDJKTSO6GJ5NHV2HHB7ZTUCK6N3WOQC4MFKBSZASCSILZQVHDMJBE57XMT6FCEWQ"
                    },
                    "device": {
                        "deviceId": "amzn1.ask.device.AEDSFL673DEPCNMPSN5J54IHE3XMXD574EPPEGFXYEY2ARMWBWMYEQ7I4GBYSSE5YDLFIZ6ULNRK2EYM3KH5YNAIB5OTZSARRFC4BJOA2BQNPZWZPH7VDDKNDCYL5MSPTCF2BGGMHIAINLJ32WY7CZQ7GIMU4WQCP24RICA6CXFWDEPRXU3BM",
                        "supportedInterfaces": {}
                    },
                    "apiEndpoint": "https://api.amazonalexa.com",
                    "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjliMzZiMTMyLTk5MmMtNGE2Zi05OTg1LTI2ZjE3MzNlZDI1YiIsImV4cCI6MTUzOTU2NDY3NCwiaWF0IjoxNTM5NTYxMDc0LCJuYmYiOjE1Mzk1NjEwNzQsInByaXZhdGVDbGFpbXMiOnsiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVEU0ZMNjczREVQQ05NUFNONUo1NElIRTNYTVhENTc0RVBQRUdGWFlFWTJBUk1XQldNWUVRN0k0R0JZU1NFNVlETEZJWjZVTE5SSzJFWU0zS0g1WU5BSUI1T1RaU0FSUkZDNEJKT0EyQlFOUFpXWlBIN1ZEREtORENZTDVNU1BUQ0YyQkdHTUhJQUlOTEozMldZN0NaUTdHSU1VNFdRQ1AyNFJJQ0E2Q1hGV0RFUFJYVTNCTSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHVk9CQTdGTkFVRzJMNVNPWEJIRDdGSVlQWVBQV0pNUDZDWFFTRUJZRFU1UVlRUENWUlpXSUtGVU02TkNFVU5QVElNUDZITVBQU1hJSkQzSEs0SzczWkRKNUJQQlY3NzVRU0c1UlBHSFFPVlRFN0tRR1NQRkVDQlpXTEZRWDROV09GNjJHWlJKR0FMNzJPV0RKS1RTTzZHSjVOSFYySEhCN1pUVUNLNk4zV09RQzRNRktCU1pBU0NTSUxaUVZIRE1KQkU1N1hNVDZGQ0VXUSJ9fQ.b0R3kkabsS_VHH8dW6eFwGYlIyZ9qmI2C7fbh6cbsXg1FJF6d3T46q88FlsmvQhKXGZQB7KCavWiX7WjTOQ6nQ1NcfO3r0XELSn90d0AE24mc2iDEpApFBOFYO9tXZeODA6GuvQGify7uQxDTa-SqaWU0u4yezmeUaAd1rwgT7AW9eAa6kUotCQyfCTn2Ug14AtYoDJEQy3_NO1snzSDMyUilU3S0FjEinXPz_25awDZ4gHVq1eDUACrDnpha8FmF7wj04wrGoizShMIWohEKdcD4W_E7LDZwsJpyfj2l4KRq_ci4MRPyfoONdgVtCt4XALYdWXpqdhYzxNA3LiDfQ"
                }
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.1a2d5e60-5d08-4783-9869-cc0dc2a18b6a",
                "timestamp": "2018-10-14T23:51:14Z",
                "locale": "en-US",
                "intent": {
                    "name": "GetTrainArrivalByDestinationIntent",
                    "confirmationStatus": "NONE",
                    "slots": {
                        "destination_station": {
                            "name": "destination_station",
                            "value": "5",
                            "resolutions": {
                                "resolutionsPerAuthority": [
                                    {
                                        "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b.LIST_OF_MARTA_STATIONS",
                                        "status": {
                                            "code": "ER_SUCCESS_MATCH"
                                        },
                                        "values": [
                                            {
                                                "value": {
                                                    "name": "Five Points Station",
                                                    "id": "ac61bde2e2de91cde069e6a9e6ba9955"
                                                }
                                            }
                                        ]
                                    }
                                ]
                            },
                            "confirmationStatus": "NONE",
                            "source": "USER"
                        },
                        "departure_station": {
                            "name": "departure_station",
                            "value": "taking Marta from cham",
                            "resolutions": {
                                "resolutionsPerAuthority": [
                                    {
                                        "authority": "amzn1.er-authority.echo-sdk.amzn1.ask.skill.9b36b132-992c-4a6f-9985-26f1733ed25b.LIST_OF_MARTA_STATIONS",
                                        "status": {
                                            "code": "ER_SUCCESS_NO_MATCH"
                                        }
                                    }
                                ]
                            },
                            "confirmationStatus": "NONE",
                            "source": "USER"
                        }
                    }
                }
            }
        }
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "Sorry, I didn't understand that. Ask when is the next train from Chamblee to Five Points",
            response['outputSpeech']['text'])
        self.assertFalse(response['shouldEndSession'])


def create_mock_train_response():
    trains = []
    train = Train
    train.next_arrival = '11:42:02'
    train.station = 'CHAMBLEE STATION'
    train.destination = 'AIRPORT STATION'
    train.direction = 'SOUTHBOUND'
    train.last_updated = '11:42:02'
    train.line = 'gold'
    train.train_id = '1'
    train.waiting_seconds = '2'
    train.waiting_time = '11:42:02'

    trains.append(train)
    return trains


if __name__ == '__main__':
    unittest.main()

