# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet
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
#         dispatcher.utter_message("Hello World!")
#
#         return []
class ActionHelloWorldProgram(Action):
    def name(self) -> Text:
        return "action_hello_world_chirag"

    def run(self, dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	print(tracker)
    	dispatcher.utter_message("Hello World Chirag!")
    	return []

class ActionCommute(Action):
    def name(self) -> Text:
    	return "action_ways_to_commute_to_charusat"

    def run(self, dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	#print("Message is: ",tracker.latest_message['entities'])
    	dispatcher.utter_message("Yes, obviously you can commute from !")
    	return []

class ActionProgram(FormAction):

    #SlotSet("institute", None)

    def name(self) -> Text:
        return "form_programs"

    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
    	return ["institute"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:

    	dispatcher.utter_template("utter_available_programs_submit",tracker)

    	return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
    	return{
    		"institute":self.from_entity(entity="institute",intent="inform"),
    	}

class ActionFees(FormAction):
    def name(self) -> Text:
        return "form_about_fees"

    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
    	return ["course","institute"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        
    	dispatcher.utter_template("utter_about_fees_submit",tracker)
    	
    	return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
    	return{
    		"institute":self.from_entity(entity="institute",intent="inform"),
    		"course":self.from_entity(entity="course",intent="inform"),
    	}