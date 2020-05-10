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
all_entites=[]
# programCodes=[]
AdmissionCodes=[]
# data={}



def ACode(code):
    AdmissionCodes.append(code)
def last(t):
    entities=t.latest_message['entities']
    if entities:
        for entity in entities:
            if entity['entity']=='qualification':
                all_entites.append(entity['entity'])
            elif entity['entity']=="degree":
                all_entites.append(entity['entity'])
            elif entity['entity']=="course":
                all_entites.append(entity['entity'])
            elif entity['entity']=="field":
                all_entites.append(entity['entity'])



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
# all_entites=[]
# programCode=""
# def last(t):
#     entities=t.latest_message['entities']
#     if entities:
#         for entity in entities:
#             if entity['entity']=='qualification':
#                 all_entites.append(entity['entity'])
#             elif entity['entity']=="degree":
#                 all_entites.append(entity['entity'])
#         #print(all_entites)


# class ActionHelloWorldProgram(Action):
#     def name(self) -> Text:
#         return "action_hello_world_chirag"

#     def run(self, dispatcher: CollectingDispatcher,
#       tracker: Tracker,
#       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#     	dispatcher.utter_message("Hello World Chirag!")
#     	return []
        

# class ActionProgram(FormAction):
#     def name(self) -> Text:
#         return "form_programs"

#     @staticmethod
#     def required_slots(tracker:Tracker)-> List[Text]:
#         last(tracker)
#         latest_entities=tracker.latest_message['entities']
#         if latest_entities:
#             for entity in latest_entities:
#                 if entity['entity']=='qualification' or entity['entity']=='field':
#                     SlotSet('pc','qf')
#                     programCode="qf"
#                     print("program q,f")
#                     return ["qualification","field"]
#                 elif entity['entity']=='degree':
#                     programCode="d"
#                     SlotSet('pc','d')
#                     print("program degree")
#                     return ['degree']
#                 else:
#                     if all_entites:
#                         if all_entites[-1]=="degree":
#                             programCode="d"
#                             SlotSet('pc','d')
#                             print("program last entity degree")
#                             return ["degree"]
#                         else:
#                             print("program last entity q,f")
#                             programCode="qf"
#                             SlotSet('pc','qf')
#                             return ["qualification","field"]
#                     else:
#                         programCode="qf"
#                         SlotSet('pc','qf')
#                         print("program last entity q,f")
#                         return ["qualification","field"]

#         elif all_entites:
#             if all_entites[-1]=="degree":
#                 programCode="d"
#                 SlotSet('pc','d')
#                 print("program last entity degree")
#                 return ["degree"]
#             else:
#                 programCode="qf"
#                 SlotSet('pc','qf')
#                 print("program last entity q,f")
#                 return ["qualification","field"]
#         else:
#             programCode="qf"
#             SlotSet('pc','qf')
#             print("program last entity q,f")
#             return ["qualification","field"]

#     def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
#         qualificationName=""
#         degreeName=""
#         fieldName=""
#         fieldName=tracker.get_slot('field')
#         degreeName=tracker.get_slot('degree')
#         qualificationName=tracker.get_slot('qualification')
#         tracker.__set_slot('qualification','pc')
#         print("Program code: ",tracker.get_slot('pc'))
#         if degreeName or (fieldName and qualificationName):
#             print("degreeName: ",degreeName)
#             print("fieldName",fieldName)
#             print("qualificationName",qualificationName)
#             #dispatcher.utter_template("utter_available_programs_degree",tracker,LINK="https://www.charusat.ac.in/cspit/")
#         return []

#     def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
#     	return{
#     		"qualification":self.from_entity(entity="qualification",intent="inform"),
#             "field":self.from_entity(entity="field",intent="inform"),
#             "degree":self.from_entity(entity="degree",intent="inform"),
#     	}

# class ActionFeesWithCourse(FormAction):
#     def name(self) -> Text:
#         return "form_fees"

#     @staticmethod
#     def required_slots(tracker:Tracker)-> List[Text]:
#         last(tracker)
#         latest_entities=tracker.latest_message['entities']
#         if latest_entities:
#             for entity in latest_entities:

#                 if entity['entity']=='qualification':
#                     SlotSet('feesCode','qc')
#                     print('fees q,c latest_message')
#                     return ["qualification","course"]

#                 elif entity['entity']=='degree':
                    
#                     print('fees degree latest_message')
#                     if entity['value']=='msc' or entity['value']=='bsc':
#                         print('with sc')
#                         SlotSet('feesCode','dc')
#                         return ['degree','course']

#                     else:
#                         SlotSet('feesCode','d')
#                         return ["degree"]

#                 elif all_entites:

#                     if all_entites[-1]=="degree":
#                         print("fees with degree called last entity")
#                         if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
#                             SlotSet('feesCode','dc')
#                             return ['degree','course']

#                         else:
#                             SlotSet('feesCode','d')
#                             return ["degree"]

#                     else:
#                         SlotSet('feesCode','qc')
#                         print("fees with q,c called")
#                         return ["qualification","course"]

#                 else:
#                     SlotSet('feesCode','qc')
#                     print("fees with q,c called")
#                     return ["qualification","course"]      
#         elif all_entites:
#             if all_entites[-1]=="degree":
#                 print("fees with degree called last entity")
#                 if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
#                     feesCode="dc"
#                     SlotSet('feesCode','dc')
#                     return ['degree','course']
#                 else:
#                     feesCode="d"
#                     SlotSet('feesCode','d')
#                     return ["degree"]
#             else:
#                 SlotSet('feesCode','qc')
#                 print("fees with q,c called")
#                 return ["qualification","course"]
#         else:
#             SlotSet('feesCode','qc')
#             print("fees with q,c called")
#             return ["qualification","course"]


#     def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
#         print('FeesCode: ',tracker.get_slot('feesCode'))
#         return []

#     def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
#         #print("From entity: ",self.from_entity)
#         return{
#             "course":self.from_entity(entity="course",intent="inform"),
#             "qualification":self.from_entity(entity="qualification",intent="inform"),
#             "field":self.from_entity(entity="field",intent="inform"),
#             "degree":self.from_entity(entity="degree",intent="inform")
#         }

class Actionhostel(FormAction):
    def name(self) -> Text:
        return "form_about_hostels"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        return ["sex"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        hostelFor = tracker.get_slot('sex')
        if(hostelFor=='boy'):
            dispatcher.utter_template("utter_about_hostel",tracker)
        elif(hostelFor=='girl'):
            dispatcher.utter_template("utter_about_girlshostel",tracker)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "sex":self.from_entity(entity="sex",intent="inform"),
        }

class Actiononlab(FormAction):
    def name(self) -> Text:
        return "form_lab_info"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        if tracker.get_slot('course'):
            return ['course']
        elif tracker.get_slot('field')=="pharmacy" or tracker.get_slot('field')=="physiotherapy": 
            return ['field']
        elif tracker.get_slot('field')=="engineering":
            return ["course",'field']
        else:
            return ['field']

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        course= tracker.get_slot('course')
        field=tracker.get_slot('field')
        if(field=='pharmacy'):
            dispatcher.utter_template("utter_lab_pharma",tracker)
        elif (field == 'physiotherapy'):
            dispatcher.utter_template('utter_lab_physio', tracker)
        elif(course=="ce" or course=="it" or course=="cs"):
            dispatcher.utter_template("utter_lab_ce_it",tracker)
        elif(course=='me'):
            dispatcher.utter_template('utter_lab_mech',tracker)
        elif(course=='ci'):
            dispatcher.utter_template('utter_lab_civil',tracker)
        elif (course == 'ec'):
            dispatcher.utter_template('utter_lab_ec', tracker)
        elif (course == 'ee'):
            dispatcher.utter_template('utter_lab_electrical', tracker)

        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "course":self.from_entity(entity="course",intent="inform"),
        }

class Actioninstitute(FormAction):
    def name(self) -> Text:
        return "form_about_institute"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        
        return ["institute"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        ins = tracker.get_slot('institute')
        if(ins=='depstar'):
            dispatcher.utter_template("utter_about_depstar",tracker)
        elif(ins=='rpcp'):
            dispatcher.utter_template("utter_about_rpcp",tracker)
        elif(ins=='arip'):
            dispatcher.utter_template("utter_about_arip",tracker)
        elif(ins=='mtin'):
            dispatcher.utter_template("utter_about_mtin",tracker)
        elif(ins=='cips'):      
            dispatcher.utter_template("utter_about_cips",tracker)
        elif(ins=='pdpias'):
            dispatcher.utter_template("utter_about_pdpias",tracker)
        elif(ins=='cmpica'):
            dispatcher.utter_template("utter_about_cmpica",tracker)
        elif(ins=='i2im'):
            dispatcher.utter_template("utter_about_i2im",tracker)
        elif(ins=='Chandubhai S Patel Institute of Technology'):
            dispatcher.utter_template("utter_about_cspit",tracker)

    


        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "institute":self.from_entity(entity="institute",intent=["inform","about_institute"]),
            # "course":self.from_entity(entity="course",intent="inform"),
        }


class ActionAdmission(FormAction):
    def name(self) -> Text:
        return "form_about_admission"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        # if tracker.get_slot('course') or tracker.get_slot('qualification'):
        #     return ['course','qualification']
        # elif tracker.get_slot('field') or tracker.get_slot('qualification'): 
        #     return ['field','qualification']
        # elif tracker.get_slot('degree'):
        #     return ['degree']
        # else:
        #     return ['degree']
        last(tracker)
        latest_entities=tracker.latest_message['entities']
        if latest_entities:
            for entity in latest_entities:

                if entity['entity']=='qualification':
                    
                    # print('fees q,c latest_message')
                    if(tracker.get_slot('course')):
                        ACode('qc')
                        return ["qualification","course"]
                    elif(tracker.get_slot('field')):
                        ACode('qf')
                        return ["qualification","field"]
                    else:
                        ACode('qf')
                        return ["qualification","field"]
                elif entity['entity']=='degree':
                    
                    #print('fees degree latest_message')
                    if entity['value']=='msc' or entity['value']=='bsc':
                        #print('with sc')
                        ACode('dc')
                        return ['degree','course']

                    else:
                        ACode('d')
                        return ["degree"]
                elif entity['entity']=='field':
                    ACode('qf')
                    # print('fees q,c latest_message')
                    
                    return ["qualification","field"]
                
                elif entity['entity']=='course':
                    ACode('qc')
                    # print('fees q,c latest_message')
                    
                    return ["qualification","course"]


                elif all_entites:

                    if all_entites[-1]=="degree":
                        #print("fees with degree called last entity")
                        if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
                            ACode('dc')
                            return ['degree','course']

                        else:
                            ACode('d')
                            return ["degree"]
                    elif(all_entites[-1]=="qualification"):
                        if(tracker.get_slot('course')):
                            ACode('qc')
                            return ["qualification","course"]
                        elif(tracker.get_slot('field')):
                            ACode('qf')
                            return ["qualification","field"]
                        else:
                            ACode('qf')
                            return ["qualification","field"]
                    elif(all_entites[-1]=="field"):
                        ACode('qf')
                        #print("fees with q,c called")
                        return ["qualification","field"]
                    elif(all_entites[-1]=="course"):
                        ACode('qc')
                        #print("fees with q,c called")
                        return ["qualification","course"]
                    
                else:
                    ACode('d')
                    #print("fees with q,c called")
                    return ["degree"]      
        elif all_entites:
            if all_entites[-1]=="degree":
                #print("fees with degree called last entity")
                if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
                    ACode('dc')
                    return ['degree','course']
                else:
                    ACode('d')
                    return ["degree"]
            elif(all_entites[-1]=="course"):
                ACode('qc')
                #print("fees with q,c called")
                return ["qualification","course"]
            elif(all_entites[-1]=="field"):
                ACode('qf')
                return ["qualification","field"]
            elif(all_entites[-1]=="qualification"):
                if(tracker.get_slot('course')):
                    ACode('qc')
                    return ["qualification","course"]
                elif(tracker.get_slot('field')):
                    ACode('qf')
                    return ["qualification","field"]
                else:
                    ACode('qf')
                    return ["qualification","field"]
        else:
            ACode('d')
            #print("fees with q,c called")
            return ["degree"]


    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        if(AdmissionCodes[-1]=='qf'):
            field=tracker.get_slot('field')
            qualification=tracker.get_slot('qualification')
            if(field=='pharmacy' and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_pharmacy_undergraduate',tracker)
            elif((field=='physiotherapy' and qualification=='undergraduate') or (field=='nursing' and qualification=='undergraduate')):
                dispatcher.utter_template('utter_adm_nursing/physio_undergraduate',tracker)
            elif(field=='engineering' and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_engineering_undergraduate',tracker)
            elif(field=='management' and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_bba_undergraduate',tracker)
            elif(field=='computer applications' and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_computeraplication_undergraduate',tracker)
            else:
                dispatcher.utter_template('utter_other_field', tracker)

        elif(AdmissionCodes[-1]=='qc'):
            course=tracker.get_slot('course')
            qualification=tracker.get_slot('qualification')
            if((course=="ce" or course=="it" or course=="cs" or course=='me' or course=='ci' or course=='ee' or course=='ec') and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_engineering_undergraduate',tracker)
            elif(course=='GNM' and qualification=='undergraduate'):
                dispatcher.utter_template('utter_adm_nursing/physio_undergraduate', tracker)
            else:
                dispatcher.utter_template('utter_other_field', tracker)

        elif(AdmissionCodes[-1]=='dc'):
            course=tracker.get_slot('course')
            degree=tracker.get_slot('degree')
            if (degree=='bsc' and course=='it'):
                dispatcher.utter_template('utter_adm_bscit_undergraduate', tracker)
            else:
                dispatcher.utter_template('utter_other_field', tracker)

        elif(AdmissionCodes[-1]=='d'):
            degree=tracker.get_slot('degree')
            if(degree=='bpharm'):
                dispatcher.utter_template('utter_adm_pharmacy_undergraduate',tracker)
            elif(degree=='btech'):
                dispatcher.utter_template('utter_adm_engineering_undergraduate',tracker)
            elif(degree=='bpt'):
                dispatcher.utter_template('utter_adm_nursing/physio_undergraduate', tracker)
            elif(degree=='bba'):
                dispatcher.utter_template('utter_adm_bba_undergraduate', tracker)
            elif(degree=='bca'):
                dispatcher.utter_template('utter_adm_computeraplication_undergraduate', tracker)
            else:
                dispatcher.utter_template('utter_other_field', tracker)
            


        # if((field=='pharmacy' and qualification=='undergraduate') or degree=='bpharm'):
        #     dispatcher.utter_template('utter_adm_pharmacy_undergraduate',tracker)
        # elif((field=='physiotherapy' and qualification=='undergraduate') or degree=='bpt' or course=='GNM' or (field=='nursing' and qualification=='undergraduate') ):
        #     dispatcher.utter_template('utter_adm_nursing/physio_undergraduate', tracker)
        # elif(((course=="ce" or course=="it" or course=="cs" or course=='me' or course=='ci' or course=='ee' or course=='ec') and qualification=='undergraduate') or degree=='btech' or (field=='engineering' and qualification=='undergraduate')):
        #     dispatcher.utter_template('utter_adm_engineering_undergraduate',tracker)
        # elif(degree=='bba' or (field=='management' and  qualification=='undergraduate')):
        #     dispatcher.utter_template('utter_adm_bba_undergraduate',tracker)
        # elif(degree=='bca' or (field=='computer applications' and qualification=='undergraduate')):
        #     dispatcher.utter_template('utter_adm_computeraplication_undergraduate',tracker)
        # elif (degree=='bsc' and course=='it'):
        #     dispatcher.utter_template('utter_adm_bscit_undergraduate', tracker)
        # else:
        #     dispatcher.utter_template('utter_other_field', tracker)

        return []

    

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "course":self.from_entity(entity="course",intent="inform"),
            "qualification":self.from_entity(entity="qualification",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform"),
            "degree":self.from_entity(entity="degree",intent="inform"),

        }