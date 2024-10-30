from datetime import datetime

def parse_flight_details(json_data):
    user_id = json_data["user"]["id"]
    flight_info = []
    
    # Add a description for the user ID
    flight_info.append(f"User ID: {user_id} - This is the unique identifier associated with the user in the system. "
                       f"It is used to track the user's account and all associated travel records, including ticket purchases and preferences.")
    
    # Loop through flights
    for flight in json_data["user"]["flights"]:
        ticket_id = flight["ticket_id"]
        pnr = flight["pnr"]
        flight_class = flight["class"]
        source = flight["source"]
        destination = flight["destination"]
        departure_date = datetime.fromisoformat(flight["departure_date"].replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M UTC')
        arrival_date = datetime.fromisoformat(flight["arrival_date"].replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M UTC')
        layover_duration = flight["layover_duration"]
        
        # Add descriptions for the primary flight information
        flight_info.append(f"Ticket ID: {ticket_id} - This ID uniquely identifies the specific ticket purchased by the user. "
                           f"It is critical for tracking reservations, managing ticket history, and coordinating flight modifications or cancellations.")
        flight_info.append(f"PNR: {pnr} - Passenger Name Record (PNR) is a unique code used by airlines to store passenger details and booking information. "
                           f"It is used for managing flight bookings, ticket validation, and identifying passenger-specific details across flights.")
        flight_info.append(f"Class: {flight_class} - This denotes the class of service the passenger has selected, such as Economy or Business. "
                           f"It impacts seating arrangements, baggage allowances, and in-flight service levels available to the passenger.")
        flight_info.append(f"Source: {source} - This is the departure airport for the flight journey, indicating the airport from which the user's travel begins.")
        flight_info.append(f"Destination: {destination} - This is the arrival airport for the final destination of the flight journey, where the user’s travel ends.")
        flight_info.append(f"Departure Date: {departure_date} - This is the date and time when the flight is scheduled to leave the departure airport.")
        flight_info.append(f"Arrival Date: {arrival_date} - This is the date and time when the flight is scheduled to arrive at the destination airport.")
        flight_info.append(f"Layover Duration: {layover_duration} - This represents the total layover time between flight segments, typically at connecting airports. "
                           f"Important for passengers to plan for rest, meals, or any other necessities between flights.")
        
        # Loop through each flight segment
        for segment in flight["segments"]:
            flight_number = segment["flight_number"]
            segment_departure = datetime.fromisoformat(segment["departure"]["date"].replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M UTC')
            segment_arrival = datetime.fromisoformat(segment["arrival"]["date"].replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M UTC')
            departure_airport = segment["departure"]["airport"]
            departure_iata = segment["departure"]["iata"]
            arrival_airport = segment["arrival"]["airport"]
            arrival_iata = segment["arrival"]["iata"]
            
            # Descriptions for each segment detail
            flight_info.append(f"Flight Number: {flight_number} - This is the unique identifier assigned to each specific flight. "
                               f"It allows airlines, airports, and travelers to reference the particular aircraft and route for this segment.")
            flight_info.append(f"Segment Departure Airport: {departure_airport} ({departure_iata}) - This indicates the specific airport where the flight segment begins.")
            flight_info.append(f"Segment Departure Date: {segment_departure} - The date and time when the flight departs from the segment's departure airport.")
            flight_info.append(f"Segment Arrival Airport: {arrival_airport} ({arrival_iata}) - This represents the destination airport where the flight segment concludes.")
            flight_info.append(f"Segment Arrival Date: {segment_arrival} - The date and time when the flight segment arrives at the destination airport.")
            
            # List passengers with detailed descriptions
            passenger_info = []
            for passenger in segment["passengers"]:
                first_name = passenger["first_name"]
                last_name = passenger["last_name"]
                seat_number = passenger["seat_number"]
                cabin_baggage = passenger["cabin_baggage"]
                check_in_baggage = passenger["check_in_baggage"]
                
                # Detailed description for each passenger
                passenger_info.append(f"Passenger Name: {first_name} {last_name} - This is the full name of the passenger as it appears on their flight ticket.")
                passenger_info.append(f"Seat Number: {seat_number} - This indicates the specific seat assigned to the passenger on this segment of the flight.")
                passenger_info.append(f"Cabin Baggage Allowance: {cabin_baggage} - This is the weight limit of carry-on baggage that the passenger can bring into the cabin.")
                passenger_info.append(f"Check-in Baggage Allowance: {check_in_baggage} - This is the weight limit of luggage that the passenger is permitted to check into the cargo hold.")
            
            # Add passenger info to the flight segment
            flight_info.append("\tPassenger Details:\n\t\t" + "\n\t\t".join(passenger_info))

            total_data = ('\n').join(flight_info)
    
    return flight_info , total_data

# Example usage
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
# Run the function and print the result

