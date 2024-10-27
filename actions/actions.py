# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

#class ActionResetSlots(Action):

#    def name(self) -> str:
#        return "action_reset_slots"

#    def run(self, dispatcher, tracker, domain):
#        return [SlotSet("location", None),
#                SlotSet("booking_type", None),
#                SlotSet("number_of_people", None),
#                SlotSet("expected_time", None)]
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionResetOrModifyBooking(Action):

#     def name(self) -> str:
#         return "action_reset_or_modify_booking"

#     def run(self, dispatcher, tracker, domain):
#         # Get the user's intent (assuming 'cancel' intent is captured by a slot)
#         booking_action = tracker.get_slot("booking_action")

#         if booking_action == "cancel":
#             # Reset all slots when user says 'cancel'
#             dispatcher.utter_message(text="Everything is cancelled.")
#             return [SlotSet("location", None),
#                     SlotSet("booking_type", None),
#                     SlotSet("number_of_people", None),
#                     SlotSet("expected_time", None),
#                     SlotSet("booking_action", None)]  # Reset the action slot as well
#         else:
#             # If user wants to modify, ask what they want to change
#             change_type = tracker.get_slot("change_type")

#             if change_type == "location":
#                 dispatcher.utter_message(text="Where would you like to change the location to?")
#                 # We assume user gives new location, update the location slot
#                 return [SlotSet("location", None)]  # New location would be set later in conversation

#             elif change_type == "booking_type":
#                 dispatcher.utter_message(text="What type of booking would you like to change to?")
#                 # Update the booking type slot based on user input
#                 return [SlotSet("booking_type", None)]  # New booking type will be set in the conversation

#             elif change_type == "number_of_people":
#                 dispatcher.utter_message(text="How many people do you want to book for?")
#                 # Update the number of people slot based on user input
#                 return [SlotSet("number_of_people", None)]

#             elif change_type == "expected_time":
#                 dispatcher.utter_message(text="What is the new expected time?")
#                 # Update the expected time slot
#                 return [SlotSet("expected_time", None)]

#             else:
#                 dispatcher.utter_message(text="What would you like to change? You can modify location, booking type, number of people, or expected time.")
#                 return []

# 

# import os
# import pandas as pd

# class ActionResetOrModifyBooking(Action):
#     def name(self) -> Text:
#         return "action_reset_or_modify_booking"

#     async def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:

#         # Fetch current slots
#         name = tracker.get_slot("name")
#         phone_number = tracker.get_slot("phone_number")
#         change_type = tracker.get_slot("change_type")
#         location = tracker.get_slot("location")
#         number_of_people = tracker.get_slot("number_of_people")
#         expected_time = tracker.get_slot("expected_time")
#         booking_type = tracker.get_slot("booking_type")

#         # Path to the Excel file (if file doesn't exist, it will be created)
#         file_path = "confirmed_bookings.xlsx"

#         # Check if file exists
#         if os.path.exists(file_path):
#             # Load existing Excel file
#             df = pd.read_excel(file_path)
#         else:
#             # Create a new DataFrame if file doesn't exist
#             df = pd.DataFrame(columns=["Name", "Contact", "Location", "Number of People", "Expected Time", "Booking Type"])

#         # Prepare the new row with booking details
#         new_booking = {
#             "Name": name,
#             "Contact": phone_number,
#             "Location": location,
#             "Number of People": number_of_people,
#             "Expected Time": expected_time,
#             "Booking Type": booking_type
#         }

#         # Append new row to the DataFrame
#         df = pd.concat([df, pd.DataFrame([new_booking])], ignore_index=True)

#         # Save the DataFrame back to the Excel file
#         try:
#             df.to_excel(file_path, index=False)
#         except PermissionError:
#             dispatcher.utter_message(text="Unable to save the booking due to permission error.")
#             return []

#         # Provide feedback to the user
#         dispatcher.utter_message(text=f"Your booking has been updated. Location: {location}, People: {number_of_people}, Time: {expected_time}, Type: {booking_type}.")

#         # Continue with necessary modifications
#         changes_map = {
#             "location": ("Please provide the new location.", "location"),
#             "number_of_people": ("Please provide the new number of people.", "number_of_people"),
#             "expected_time": ("Please provide the new expected time.", "expected_time")
#         }

#         if change_type in changes_map:
#             message, slot_name = changes_map[change_type]
#             dispatcher.utter_message(text=message)
#             return [SlotSet(slot_name, None)]

#         dispatcher.utter_message(text="I couldn't understand the modification. Please specify again.")
#         return []

 
import os
import pandas as pd

import os
import pandas as pd
from typing import Text, Dict, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionResetOrModifyBooking(Action):
    def name(self) -> Text:
        return "action_reset_or_modify_booking"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Fetch current slots
        name = tracker.get_slot("name")
        phone_number = tracker.get_slot("phone_number")
        change_type = tracker.get_slot("change_type")
        location = tracker.get_slot("location")
        people = tracker.get_slot("people")
        time = tracker.get_slot("time")
        booking = tracker.get_slot("booking")

        # Debugging - Check if slots are correctly populated
        dispatcher.utter_message(text=f"Name: {name}, Phone Number: {phone_number}")

        # Path to the Excel file (if file doesn't exist, it will be created)
        file_path = "confirmed_bookings.xlsx"

        # Load or create the DataFrame
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["Name", "Contact", "Location", "Number of People", "Expected Time", "Booking Type"])

        # Debugging - Display loaded data
        dispatcher.utter_message(text=f"Excel Data: {df.to_dict()}")

        # Check if name and phone_number slots are not None
        if name is None or phone_number is None:
            dispatcher.utter_message(text="Booking could not be processed. Name or phone number is missing.")
            return []

        # Try to find an existing booking to modify
        mask = (df["Name"].str.strip().str.lower() == name.strip().lower()) & (df["Contact"].astype(str).str.strip() == phone_number.strip())

        if df[mask].empty:
            # No existing booking found; add a new booking
            dispatcher.utter_message(text="No existing booking found, creating a new booking.")

            # Prepare the new row with booking details
            new_booking = {
                "Name": name,
                "Contact": phone_number,
                "Location": location,
                "Number of People": people,
                "Expected Time": time,
                "Booking Type": booking
            }

            # Append the new booking
            df = pd.concat([df, pd.DataFrame([new_booking])], ignore_index=True)

        else:
            # Modify the existing booking based on the change_type
            if change_type == "location":
                df.loc[mask, "Location"] = location
                dispatcher.utter_message(text=f"Location updated to {location}.")
            elif change_type == "people":
                df.loc[mask, "Number of People"] = people
                dispatcher.utter_message(text=f"Number of people updated to {people}.")
            elif change_type == "time":
                df.loc[mask, "Expected Time"] = time
                dispatcher.utter_message(text=f"Expected time updated to {time}.")
            elif change_type == "booking":
                df.loc[mask, "Booking Type"] = booking
                dispatcher.utter_message(text=f"Booking type updated to {booking}.")
            else:
                dispatcher.utter_message(text="Unknown modification request.")
                return []

        # Save the updated or new booking back to the Excel file
        try:
            df.to_excel(file_path, index=False)
        except PermissionError:
            dispatcher.utter_message(text="Unable to save the booking due to a permission error. Please ensure the file is closed and try again.")
            return []

        # Provide a summary of the updated booking
        dispatcher.utter_message(text=f"Your booking has been updated: Location: {location}, People: {people}, Time: {time}, Type: {booking}.")

        # Reset the slot if a specific change was made
        if change_type in ["location", "people", "time"]:
            return [SlotSet(change_type, None)]

        return[]


class ActionSaveBooking(Action):
    def name(self) -> Text:
        return "action_save_booking"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Fetch slots
        name = tracker.get_slot("name")
        phone_number = tracker.get_slot("phone_number")
        location = tracker.get_slot("location")
        people = tracker.get_slot("people")
        time = tracker.get_slot("time")
        booking = tracker.get_slot("booking")

        # Debug message to confirm slot data
        dispatcher.utter_message(text=f"Debug - Name: {name}, Phone Number: {phone_number}")

        # Check if essential slots are provided
        if not name or not phone_number:
            dispatcher.utter_message(text="Booking could not be saved. Please provide both name and phone number.")
            return []

        # Clean up phone number formatting
        phone_number = ''.join(filter(str.isdigit, phone_number))

        # File path
        file_path = "confirmed_bookings.xlsx"

        # Load or create DataFrame
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
        else:
            df = pd.DataFrame(columns=["Name", "Contact", "Location", "Number of People", "Expected Time", "Booking Type"])

        # Check if booking already exists
        mask = (df["Name"].str.strip().str.lower() == name.strip().lower()) & (df["Contact"].astype(str).str.strip() == phone_number.strip())
        if not df[mask].empty:
            dispatcher.utter_message(text="Booking already exists with the provided details. No new booking was created.")
            return []

        # New booking entry
        new_booking = {
            "Name": name,
            "Contact": phone_number,
            "Location": location,
            "Number of People": people,
            "Expected Time": time,
            "Booking Type": booking
        }

        # Append booking to DataFrame and save
        df = pd.concat([df, pd.DataFrame([new_booking])], ignore_index=True)
        try:
            df.to_excel(file_path, index=False)
            dispatcher.utter_message(text="Your booking has been successfully saved.")
        except PermissionError:
            dispatcher.utter_message(text="Unable to save the booking due to a file permission error.")
            return []

        return []

