import os
import chromadb
import json
from data_format import parse_flight_details
import chromadb.utils.embedding_functions as embedding_functions


client = chromadb.PersistentClient(path= os.path.join(os.getcwd()))


json_str = '''{
    "user": {
        "id": 227,
        "flights": [
            {
                "ticket_id": 3183,
                "pnr": "HZAVJJ",
                "class": "ECONOMY",
                "source": "Cape Town International Airport (CPT)",
                "destination": "Indira Gandhi International Airport (DEL)",
                "departure_date": "2024-07-11T14:35:00.000Z",
                "arrival_date": "2024-07-12T08:10:00.000Z",
                "layover_duration": "55m",
                "segments": [
                    {
                        "flight_number": "ET846",
                        "departure": {
                            "airport": "Cape Town International Airport",
                            "iata": "CPT",
                            "date": "2024-07-11T14:35:00.000Z"
                        },
                        "arrival": {
                            "airport": "Addis Ababa Bole International Airport",
                            "iata": "ADD",
                            "date": "2024-07-11T22:00:00.000Z"
                        },
                        "passengers": [
                            {
                                "first_name": "surendra",
                                "last_name": "singh",
                                "seat_number": "21a",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            },
                            {
                                "first_name": "narinder",
                                "last_name": "kaur",
                                "seat_number": "21b",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            },
                            {
                                "first_name": "samik",
                                "last_name": "singh",
                                "seat_number": "21c",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            }
                        ]
                    },
                    {
                        "flight_number": "ET686",
                        "departure": {
                            "airport": "Addis Ababa Bole International Airport",
                            "iata": "ADD",
                            "date": "2024-07-11T22:55:00.000Z"
                        },
                        "arrival": {
                            "airport": "Indira Gandhi International Airport",
                            "iata": "DEL",
                            "date": "2024-07-12T08:10:00.000Z"
                        },
                        "passengers": [
                            {
                                "first_name": "surendra",
                                "last_name": "singh",
                                "seat_number": "21a",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            },
                            {
                                "first_name": "narinder",
                                "last_name": "kaur",
                                "seat_number": "21b",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            },
                            {
                                "first_name": "samik",
                                "last_name": "singh",
                                "seat_number": "21c",
                                "cabin_baggage": "7kg",
                                "check_in_baggage": "23kg"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}'''

def add_to_ragdb(json_str , passenger_name):

    google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key="AIzaSyBQzhUKcMqLJdFKn1ZDmR_LDXCTbBcLFiE")
    passenger_data , Onestring = parse_flight_details(json.loads(json_str))
    collection =  client.create_collection(name = passenger_name)

    index_list = [str(ele) for ele in range(0 , len(passenger_data))]

    collection.add(
        documents = passenger_data,
        ids = index_list
    )

 

def rag_query(query , user_name):

    collection = client.get_collection(name = user_name)
    results = collection.query(
    query_texts=[query], # Chroma will embed this for you
    n_results=2 # how many results to return
    )
    return results['documents'][0][0] + '''\n 
    ============================================================================================================================
    
    here is summarized version of all data :
    
    User ID: 227 - This is the unique identifier associated with the user in the system. It is used to track the user's account and all associated travel records, including ticket purchases and preferences.
Ticket ID: 3183 - This ID uniquely identifies the specific ticket purchased by the user. It is critical for tracking reservations, managing ticket history, and coordinating flight modifications or cancellations.
PNR: HZAVJJ - Passenger Name Record (PNR) is a unique code used by airlines to store passenger details and booking information. It is used for managing flight bookings, ticket validation, and identifying passenger-specific details across flights.
Class: ECONOMY - This denotes the class of service the passenger has selected, such as Economy or Business. It impacts seating arrangements, baggage allowances, and in-flight service levels available to the passenger.
Source: Cape Town International Airport (CPT) - This is the departure airport for the flight journey, indicating the airport from which the user's travel begins.
Destination: Indira Gandhi International Airport (DEL) - This is the arrival airport for the final destination of the flight journey, where the user’s travel ends.
Departure Date: 2024-07-11 14:35 UTC - This is the date and time when the flight is scheduled to leave the departure airport.
Arrival Date: 2024-07-12 08:10 UTC - This is the date and time when the flight is scheduled to arrive at the destination airport.
Layover Duration: 55m - This represents the total layover time between flight segments, typically at connecting airports. Important for passengers to plan for rest, meals, or any other necessities between flights.
Flight Number: ET846 - This is the unique identifier assigned to each specific flight. It allows airlines, airports, and travelers to reference the particular aircraft and route for this segment.
Segment Departure Airport: Cape Town International Airport (CPT) - This indicates the specific airport where the flight segment begins.
Segment Departure Date: 2024-07-11 14:35 UTC - The date and time when the flight departs from the segment's departure airport.
Segment Arrival Airport: Addis Ababa Bole International Airport (ADD) - This represents the destination airport where the flight segment concludes.
Segment Arrival Date: 2024-07-11 22:00 UTC - The date and time when the flight segment arrives at the destination airport.
	Passenger Details:
		Passenger Name: Surendra Singh - This is the full name of the passenger as it appears on their flight ticket.
		Seat Number: 21A - This indicates the specific seat assigned to the passenger on this segment of the flight.
		Cabin Baggage Allowance: 7kg - This is the weight limit of carry-on baggage that the passenger can bring into the cabin.
		Check-in Baggage Allowance: 23kg - This is the weight limit of luggage that the passenger is permitted to check into the cargo hold.


    
    '''







