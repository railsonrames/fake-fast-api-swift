from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class FilterCriteria(BaseModel):
    AccountNumber: Optional[str] = None
    TransactionId: Optional[str] = None
    TransferStatus: Optional[bool] = None
    TransactionType: Optional[str] = None
    CommissionDate: Optional[datetime] = None
    CommissionState: Optional[str] = None
    OpperationStartDate: Optional[datetime] = None
    OpperationEndDate: Optional[datetime] = None

class ListItem(BaseModel):
    Uetr: str
    AccountNumber: str
    TransactionId: str
    TransactionType: str
    OpperationDate: str
    CommissionId: str
    CommissionDate: str
    TransferStatus: bool
    CommissionApplied: bool
    CommissionState: str
    DebitorCountry: str
    FeeCode: str
    CreditAmount: float
    CreditorIban: str

mock_data = [
    {
        "Uetr": "2F2E2C4D-FE1A-4D70-8E54-3B795A898342",
        "AccountNumber": "123456789",
        "TransactionId": "1bf65b80-5e29-420d-ad7b-de22cb1c7aea",
        "TransactionType": "Swift",
        "OpperationDate": "2024-04-12",
        "CommissionId": "d52afe88-e6e9-42fa-b1dc-4ac7c77131f9",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "UK",
        "FeeCode": "Swift",
        "CreditAmount": 5000.00,
        "CreditorIban": "IBAN123456789"
    },
    {
        "Uetr": "c0104328-418a-4e6a-9a74-12336f3548a4",
        "AccountNumber": "987654321",
        "TransactionId": "8831469a-c4db-4945-8785-8de5ba1f3e9d",
        "TransactionType": "Swift",
        "OpperationDate": "2024-04-10",
        "CommissionId": "8d375dbc-2deb-4d7b-8455-6be9a8d6118b",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "IT",
        "FeeCode": "Swift",
        "CreditAmount": 5000.00,
        "CreditorIban": "IBAN123456789"
    },
    {
        "Uetr": "b61a0e34-865f-4e51-b9ab-6d54694f59a7",
        "AccountNumber": "456789012",
        "TransactionId": "4ccf6754-26ef-43c2-b814-ecb80229f99e",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-04-15",
        "CommissionId": "0e80dc28-7b7c-47f2-a217-d514ea2b1506",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": False,
        "CommissionState": "Changed",
        "DebitorCountry": "FR",
        "FeeCode": "SEPA",
        "CreditAmount": 6000.00,
        "CreditorIban": "IBAN456789012"
    },
    {
        "Uetr": "92ff8c32-d915-470e-8ec7-8e9cf939aa44",
        "AccountNumber": "890123456",
        "TransactionId": "fa9169ee-58a4-47a4-889e-b4490fc78a05",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-04-18",
        "CommissionId": "69b6ee8a-16d7-42e5-a73b-4b788f7d80f4",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "DE",
        "FeeCode": "SEPA",
        "CreditAmount": 7000.00,
        "CreditorIban": "IBAN890123456"
    },    {
        "Uetr": "3d5d91b0-5ed7-4dc1-9340-72d7779f62bb",
        "AccountNumber": "234567890",
        "TransactionId": "a5eef2a1-f484-4f3b-b6e4-d1fc3eaf9e1b",
        "TransactionType": "Swift",
        "OpperationDate": "2024-04-20",
        "CommissionId": "db85018f-0f7d-4033-81e0-675605081be3",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Indebt",
        "DebitorCountry": "ES",
        "FeeCode": "Swift",
        "CreditAmount": 8000.00,
        "CreditorIban": "IBAN234567890"
    },
    {
        "Uetr": "4f056214-89b3-472e-b799-9de4de0f4334",
        "AccountNumber": "345678901",
        "TransactionId": "9e5e7277-ef63-421b-b40b-fd0b251d4f15",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-04-25",
        "CommissionId": "f932c026-34b5-497f-953a-c5dcfa0139f2",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": False,
        "CommissionState": "Chargeback",
        "DebitorCountry": "PT",
        "FeeCode": "SEPA",
        "CreditAmount": 9000.00,
        "CreditorIban": "IBAN345678901"
    },
    {
        "Uetr": "68d8691b-f2de-49a0-b481-9299dd7394cf",
        "AccountNumber": "456789012",
        "TransactionId": "76f75702-23e7-405e-b6d7-f496ecf56853",
        "TransactionType": "Swift",
        "OpperationDate": "2024-04-28",
        "CommissionId": "e7f1f80d-f3e3-49d2-9d61-d9dd5f375e42",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "IT",
        "FeeCode": "Swift",
        "CreditAmount": 10000.00,
        "CreditorIban": "IBAN456789012"
    },
    {
        "Uetr": "8c85da62-725a-47b9-9266-3c1cb352788e",
        "AccountNumber": "567890123",
        "TransactionId": "8e6ef22f-f0f5-4503-8bf0-c5f5d0d14c38",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-05-02",
        "CommissionId": "4f7b31d7-d726-407d-80ae-8b3e3b4d8bc9",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Changed",
        "DebitorCountry": "FR",
        "FeeCode": "SEPA",
        "CreditAmount": 11000.00,
        "CreditorIban": "IBAN567890123"
    },
    {
        "Uetr": "fc886b95-4f97-46d9-81e1-d4630d5a4ea4",
        "AccountNumber": "678901234",
        "TransactionId": "5b6545c1-8cb1-4750-a26a-82f167bcda1d",
        "TransactionType": "Swift",
        "OpperationDate": "2024-05-05",
        "CommissionId": "4c3d1663-515d-48d5-b227-3b13e109c180",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": False,
        "CommissionState": "Indebt",
        "DebitorCountry": "DE",
        "FeeCode": "Swift",
        "CreditAmount": 12000.00,
        "CreditorIban": "IBAN678901234"
    },
    {
        "Uetr": "b17b2e11-7b55-4813-85cf-c5ed6fc06540",
        "AccountNumber": "789012345",
        "TransactionId": "a2397e8f-3ee7-45db-bd41-81761c204dc3",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-05-08",
        "CommissionId": "e2a7d798-7e59-4e6d-b238-52d688c08f3f",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "ES",
        "FeeCode": "SEPA",
        "CreditAmount": 13000.00,
        "CreditorIban": "IBAN789012345"
    },
        {
        "Uetr": "e3cb3a4f-1ee6-4f09-89ec-df4923af2520",
        "AccountNumber": "890123456",
        "TransactionId": "8d916457-c35e-4ae8-8ebf-5cf7644a9490",
        "TransactionType": "Swift",
        "OpperationDate": "2024-05-11",
        "CommissionId": "2e90d6ae-b8e0-4f71-a279-6da5a03763f0",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Indebt",
        "DebitorCountry": "UK",
        "FeeCode": "Swift",
        "CreditAmount": 14000.00,
        "CreditorIban": "IBAN890123456"
    },
    {
        "Uetr": "d5fe76e0-dcc3-4567-8e19-3d3fda89d25b",
        "AccountNumber": "901234567",
        "TransactionId": "09f62599-6c23-4d98-a206-7a7d09160e2b",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-05-14",
        "CommissionId": "1b4893a6-b170-4a16-9aae-6e27c62e3a6d",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": False,
        "CommissionState": "Chargeback",
        "DebitorCountry": "DE",
        "FeeCode": "SEPA",
        "CreditAmount": 15000.00,
        "CreditorIban": "IBAN901234567"
    },
    {
        "Uetr": "d95e3a23-fb9b-4532-9db4-8ef6f8f8e203",
        "AccountNumber": "012345678",
        "TransactionId": "d1b0cf71-f1b2-431e-b3f8-d4aa1b45d5dc",
        "TransactionType": "Swift",
        "OpperationDate": "2024-05-17",
        "CommissionId": "e7cbe9fc-c7b8-45fb-a37a-4a53d74914d1",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "FR",
        "FeeCode": "Swift",
        "CreditAmount": 16000.00,
        "CreditorIban": "IBAN012345678"
    },
    {
        "Uetr": "d96c0726-51c6-4488-af27-2d0a68433f41",
        "AccountNumber": "123456789",
        "TransactionId": "23f4db29-0bbd-4f08-b59d-96a6eac176fd",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-05-20",
        "CommissionId": "05b69923-7836-49f2-987d-61b2ad64e3e0",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Changed",
        "DebitorCountry": "ES",
        "FeeCode": "SEPA",
        "CreditAmount": 17000.00,
        "CreditorIban": "IBAN123456789"
    },
    {
        "Uetr": "88219a90-1bb4-4ef4-9c94-ae9d8f76a170",
        "AccountNumber": "234567890",
        "TransactionId": "d5d7f5f1-3c41-48f2-8797-5e9b97e1717b",
        "TransactionType": "Swift",
        "OpperationDate": "2024-05-23",
        "CommissionId": "fbf2ec62-f487-4e13-bfeb-0107086b2642",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": False,
        "CommissionState": "Indebt",
        "DebitorCountry": "IT",
        "FeeCode": "Swift",
        "CreditAmount": 18000.00,
        "CreditorIban": "IBAN234567890"
    },
    {
        "Uetr": "a97e345d-90e0-4f7a-b81a-90c0a32fe5ae",
        "AccountNumber": "345678901",
        "TransactionId": "19d3e7cc-3c9e-4268-8c2e-dc1403a7dc71",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-05-26",
        "CommissionId": "de9b4314-dacc-42b4-b6b9-3be05895321d",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "UK",
        "FeeCode": "SEPA",
        "CreditAmount": 19000.00,
        "CreditorIban": "IBAN345678901"
    },
    {
        "Uetr": "5fd047e7-3940-44b3-9f92-fb257301971b",
        "AccountNumber": "456789012",
        "TransactionId": "c0aeb8d1-ff91-4605-a9b3-35d2999f7793",
        "TransactionType": "Swift",
        "OpperationDate": "2024-05-29",
        "CommissionId": "b6dcd3e1-e5e8-46d7-a1c0-f0a713198c36",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Chargeback",
        "DebitorCountry": "DE",
        "FeeCode": "Swift",
        "CreditAmount": 20000.00,
        "CreditorIban": "IBAN456789012"
    },
    {
        "Uetr": "2db07f26-cd3d-4593-aabc-8db6b509080f",
        "AccountNumber": "567890123",
        "TransactionId": "d1bf36f2-8d05-42c0-b340-161981eefbac",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-06-01",
        "CommissionId": "deff84e7-0a77-4432-88d6-10a4ad0ff1bc",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": False,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "FR",
        "FeeCode": "SEPA",
        "CreditAmount": 21000.00,
        "CreditorIban": "IBAN567890123"
    },
    {
        "Uetr": "f2cf0f7d-5c5c-45ac-b83b-3b6537f14dcb",
        "AccountNumber": "678901234",
        "TransactionId": "f3582f9e-1d6c-4d09-9813-84520c97e141",
        "TransactionType": "Swift",
        "OpperationDate": "2024-06-04",
        "CommissionId": "3a30c6e2-f9a3-43d2-948f-842b0de2df8c",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": False,
        "CommissionApplied": True,
        "CommissionState": "Changed",
        "DebitorCountry": "ES",
        "FeeCode": "Swift",
        "CreditAmount": 22000.00,
        "CreditorIban": "IBAN678901234"
    },
    {
        "Uetr": "d9db7f9f-4002-46f5-915f-00248c70f0ef",
        "AccountNumber": "789012345",
        "TransactionId": "d6f05085-9f38-4a6d-a9f0-d2405952ff22",
        "TransactionType": "SEPA",
        "OpperationDate": "2024-06-07",
        "CommissionId": "e5153031-fc9f-485a-b4f0-47fd55d6accc",
        "CommissionDate": "2024-04-11 08:30:00",
        "TransferStatus": True,
        "CommissionApplied": True,
        "CommissionState": "Uncollectable",
        "DebitorCountry": "IT",
        "FeeCode": "SEPA",
        "CreditAmount": 23000.00,
        "CreditorIban": "IBAN789012345"
    }
]

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.post("/filter/")
async def filter_list(filter_criteria: FilterCriteria) -> List[ListItem]:
    filtered_list = []

    for item in mock_data:
        # Check each filter criterion
        if (
            (filter_criteria.AccountNumber is None or filter_criteria.AccountNumber == "" or filter_criteria.AccountNumber == item["AccountNumber"]) and
            (filter_criteria.TransactionId is None or filter_criteria.TransactionId == "" or filter_criteria.TransactionId == item["TransactionId"]) and
            (filter_criteria.TransferStatus is None or filter_criteria.TransferStatus == "" or filter_criteria.TransferStatus == item["TransferStatus"]) and
            (filter_criteria.TransactionType is None or filter_criteria.TransactionType == "" or filter_criteria.TransactionType == item["TransactionType"]) and
            (filter_criteria.CommissionDate is None or filter_criteria.CommissionDate == "" or filter_criteria.CommissionDate == item["CommissionDate"]) and
            (filter_criteria.CommissionState is None or filter_criteria.CommissionState == "" or filter_criteria.CommissionState == item["CommissionState"]) and
            (filter_criteria.OpperationStartDate is None or filter_criteria.OpperationStartDate == "" or datetime.strptime(filter_criteria.OpperationStartDate, "%Y-%m-%d") <= datetime.strptime(item["OpperationDate"], "%Y-%m-%d")) and
            (filter_criteria.OpperationEndDate is None or filter_criteria.OpperationEndDate == "" or datetime.strptime(filter_criteria.OpperationEndDate, "%Y-%m-%d") >= datetime.strptime(item["OpperationDate"], "%Y-%m-%d"))
        ):
            filtered_list.append(ListItem(**item))

    return filtered_list
