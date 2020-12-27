# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFindFlights(Action):

    def name(self) -> Text:
        return "action_find_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['indent'].get('name')
        source  = ""
        destination = ""
        for e in tracker.latest_message['entities']:
            if e['entity'] == 'source':
                source = e['value']
            if e['entity'] == 'destination':
                destination = e['value']

        print(f"Source {source}, Destination {destination} for intent {intent}")

        dispatcher.utter_message(text=f"Following flights are available from {source} to {destination} \n Flight A \n Flight B")

        return []

class ActionFindTrains(Action):

    def name(self) -> Text:
        return "action_find_trains"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['indent'].get('name')
        source  = ""
        destination = ""
        for e in tracker.latest_message['entities']:
            if e['entity'] == 'source':
                source = e['value']
            if e['entity'] == 'destination':
                destination = e['value']

        print(f"Source {source}, Destination {destination} for intent {intent}")

        dispatcher.utter_message(text=f"Following trains are available from {source} to {destination} \n Train A \n Train B")

        return []

class ActionFindIntinerary(Action):

    def name(self) -> Text:
        return "action_find_flights"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"Here is a list of your upcomming trips : \n ... \n ...")

        return []


