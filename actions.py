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
class Actionhostel(FormAction):
    def name(self) -> Text:
        return "form_about_hostels"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        return ["hostel"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        hostel = tracker.get_slot('hostel')
        if(hostel=='boys'):
            dispatcher.utter_template("utter_about_hostel",tracker)
        elif(hostel=='girls'):
            dispatcher.utter_template("utter_about_girlshostel",tracker)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "hostel":self.from_entity(entity="hostel",intent="inform"),
            "course":self.from_entity(entity="course",intent="inform"),
        }
# class Actionhostel(FormAction):
#     @staticmethod
#     hostel=tracker.get_slot('hostel')
#     if(hostel=='boys')
#     def required_fields():
#         return [FreeTextFormField("typeofhostel")]
#     def name(self):
#         return 'action_about_hostel'
#     # def validate(self,dispatcher,tracker,domain):
#     # 	if invalid:
#     # 		slots.append(SlotSet('typeofhostel',True))
#     # 	else:
#     # 		slots.append(SlotSet('typeofhostel',None))
#     # def required_slots(tracker:Tracker)-> List[Text]:
#     #     return ["typeofhostel"]
#
#     def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
#         return []
#
#
#     def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
#         return{
#             "typeofhostel":self.from_entity(entity="typeofhostel",intent="inform"),
#             "course":self.from_entity(entity="course",intent="inform"),
#         }

class Actiononlab(FormAction):
    def name(self) -> Text:
        return "form_lab_info"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        return ["course"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        lab= tracker.get_slot('course')
        if(lab=='ce' or lab=='it' or lab=='csc'):
            dispatcher.utter_template("utter_lab_ce_it",tracker)
        elif(lab=='pharmacy'):
            dispatcher.utter_template("utter_lab_pharma",tracker)
        elif(lab=='me'):
            dispatcher.utter_template('utter_lab_mech',tracker)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "hostel":self.from_entity(entity="hostel",intent="inform"),
            "course":self.from_entity(entity="course",intent="inform"),
        }