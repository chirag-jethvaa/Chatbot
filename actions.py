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
import json

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
all_entites=[]
all_entites2=[]
all_entites3=[]
programCodes=[]
placementCodes=[]
AdmissionCodes=[]
feesCodes=[]

data={}

with open('database2.json') as f:
    data=json.load(f)

coursesRoot=data['university']['courses']
def pCode(code):
    programCodes.append(code)
def plCode(code):
    placementCodes.append(code)
def fCode(code):
    feesCodes.append(code)
def ACode(code):
    AdmissionCodes.append(code)
def last(t):
    entities=t.latest_message['entities']
    if entities:
        for entity in entities:
            if entity['entity']=='qualification':
                all_entites.append(entity['entity'])
                all_entites2.append(entity['entity'])
            elif entity['entity']=="degree":
                all_entites.append(entity['entity'])
                all_entites2.append(entity['entity'])
            elif entity['entity']=='course':
                all_entites2.append(entity['entity'])
                all_entites3.append(entity['entity'])
            elif entity['entity']=='field':
                all_entites2.append(entity['entity'])
                all_entites3.append(entity['entity'])

def available_programs_qf(c,q,f):
    message=""
    for field in coursesRoot:
        if field==f:
            for institute in c[field]:
                for degree in c[field][institute]:
                    for courseName in c[field][institute][degree]:
                        courseDetails=c[field][institute][degree][courseName]
                        if courseDetails['level']==q:
                            print(courseDetails['name'])
                            message=message+courseDetails['name']+"\n"
    return message
                        
def available_programs_d(c,d):
    message=""
    for field in coursesRoot:
        for institute in c[field]:
            for degree in c[field][institute]:
                if degree==d or d in degree:
                    for courseName in c[field][institute][degree]:
                        courseDetails=c[field][institute][degree][courseName]
                        if degree=="pgd":
                            message=message+courseDetails['name']+" "+"with fees: "+courseDetails['fees']+"\n"
                        else:
                            message=message+courseDetails['name']+"\n"
    return message

def fees_qc(c,q,co):
    message=""
    for field in coursesRoot:
        for institute in c[field]:
            for degree in c[field][institute]:
                for courseName in c[field][institute][degree]:
                    if courseName==co:
                        courseDetails=c[field][institute][degree][courseName]
                        if courseDetails['level']==q:
                            message=message+courseDetails['fees']+"\n"
    return message

def fees_dc(c,d,co):
    message=""
    for field in coursesRoot:
        for institute in c[field]:
            for degree in c[field][institute]:
                if degree==d:
                    for courseName in c[field][institute][degree]:
                        if courseName==co:
                            courseDetails=c[field][institute][degree][courseName]
                            message=message+courseDetails['fees']+"\n"
    return message

def fees_d(c,d):
    message=""
    for field in coursesRoot:
        for institute in c[field]:
            for degree in c[field][institute]:
                if degree==d:
                    for courseName in c[field][institute][degree]:
                        courseDetails=c[field][institute][degree][courseName]
                        if degree=="btech":
                            message=message+institute+", "+"with fees: "+courseDetails['fees']+"\n"
                        else:
                            message=message+courseDetails['fees']+"\n"
                        break
    return message


class ActionHelloWorldProgram(Action):
    def name(self) -> Text:
        return "action_hello_world_chirag"

    def run(self, dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    	dispatcher.utter_message("Hello World Chirag!")
    	return []
        

class ActionProgram(FormAction):
    def name(self) -> Text:
        return "form_programs"

    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        last(tracker)
        latest_entities=tracker.latest_message['entities']
        if latest_entities:
            for entity in latest_entities:
                if entity['entity']=='qualification' or entity['entity']=='field':
                    pCode('qf')
                    #print("program q,f")
                    return ["qualification","field"]
                elif entity['entity']=='degree':
                    pCode('d')
                    #print("program degree")
                    return ['degree']
                else:
                    if all_entites:
                        if all_entites[-1]=="degree":
                            pCode('d')
                            #print("program last entity degree")
                            return ["degree"]
                        else:
                            #print("program last entity q,f")
                            pCode('qf')

                            return ["qualification","field"]
                    else:
                        pCode('qf')
                        #print("program last entity q,f")
                        return ["qualification","field"]

        elif all_entites:
            if all_entites[-1]=="degree":
                pCode('d')
                #print("program last entity degree")
                return ["degree"]
            else:
                pCode('qf')
                #print("program last entity q,f")
                return ["qualification","field"]
        else:
            pCode('qf')
            #print("program last entity q,f")
            return ["qualification","field"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        print("programCode: ",programCodes[-1])
        if programCodes[-1]=='qf':
            if tracker.get_slot('field')=="commerce":
                m=""
                m=available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"computer applications")
                m=m+available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"management")
                dispatcher.utter_message(m)
            elif tracker.get_slot('field')=="medical":
                m=""
                m=available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"nursing")
                m=m+available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"physio")
                m=m+available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"pharmacy")
                m=m+available_programs_qf(coursesRoot,tracker.get_slot('qualification'),"paramedical sciences")
                dispatcher.utter_message(m)
            else:
                m=""
                m=available_programs_qf(coursesRoot,tracker.get_slot('qualification'),tracker.get_slot('field'))
                dispatcher.utter_message(m)
        elif programCodes[-1]=='d':
            m=""
            m=available_programs_d(coursesRoot,tracker.get_slot('degree'))
            dispatcher.utter_message(m)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
    	return{
    		"qualification":self.from_entity(entity="qualification",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform"),
            "degree":self.from_entity(entity="degree",intent="inform"),
    	}

class ActionFeesWithCourse(FormAction):
    def name(self) -> Text:
        return "form_fees"

    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        last(tracker)
        latest_entities=tracker.latest_message['entities']

        if latest_entities:
            for entity in latest_entities:
                if entity['entity']=='qualification':
                    fCode('qc')
                    #print('fees q,c latest_message')
                    return ["qualification","course"]

                elif entity['entity']=='degree':
                    
                    #print('fees degree latest_message')
                    if entity['value']=='msc' or entity['value']=='bsc':
                        #print('with sc')
                        fCode('dc')
                        return ['degree','course']

                    else:
                        fCode('d')
                        return ["degree"]

                elif all_entites:

                    if all_entites[-1]=="degree":
                        #print("fees with degree called last entity")
                        if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
                            fCode('dc')
                            return ['degree','course']

                        else:
                            fCode('d')
                            return ["degree"]
                    else:
                        fCode('qc')
                        #print("fees with q,c called")
                        return ["qualification","course"]
                else:
                    fCode('qc')
                    #print("fees with q,c called")
                    return ["qualification","course"]      
        elif all_entites:
            if all_entites[-1]=="degree":
                #print("fees with degree called last entity")
                if tracker.get_slot(all_entites[-1])=='bsc' or tracker.get_slot(all_entites[-1])=='msc':
                    fCode('dc')
                    return ['degree','course']
                else:
                    fCode('d')
                    return ["degree"]
            else:
                fCode('qc')
                #print("fees with q,c called")
                return ["qualification","course"]
        else:
            fCode('qc')
            #print("fees with q,c called")
            return ["qualification","course"]


    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        #print("FeesCodes:",feesCodes)
        if feesCodes[-1]=='qc':
            m=""
            m=fees_qc(coursesRoot,tracker.get_slot('qualification'),tracker.get_slot('course'))
            dispatcher.utter_message(m)
        elif feesCodes[-1]=='dc':
            m=""
            m=fees_dc(coursesRoot,tracker.get_slot('degree'),tracker.get_slot('course'))
            dispatcher.utter_message(m)
        elif feesCodes[-1]=='d':
            m=""
            m=fees_d(coursesRoot,tracker.get_slot('degree'))
            dispatcher.utter_message(m)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        #print("From entity: ",self.from_entity)
        return{
            "course":self.from_entity(entity="course",intent="inform"),
            "qualification":self.from_entity(entity="qualification",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform"),
            "degree":self.from_entity(entity="degree",intent="inform")
        }

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
            print('c')
            return ['course']
        elif tracker.get_slot('field')=="engineering":
            print('engg')
            return ["course",'field']
        elif tracker.get_slot('field')=="pharmacy" or tracker.get_slot('field')=="physiotherapy": 
            print('ph or pharmacy')
            return ['field']
        else:
            print('else')
            return ['field']

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        course= tracker.get_slot('course')
        field=tracker.get_slot('field')
        if(field=='pharmacy'):
            dispatcher.utter_template("utter_lab_pharma",tracker)
        elif (field == 'physiotherapy'):
            dispatcher.utter_template('utter_lab_physio', tracker)
        elif(course=="ce" or course=="it" or course=="cs" or course=="cse"):
            dispatcher.utter_template("utter_lab_ce_it",tracker)
        elif(course=='me'):
            dispatcher.utter_template('utter_lab_mech',tracker)
        elif(course=='cl'):
            dispatcher.utter_template('utter_lab_civil',tracker)
        elif (course == 'ec'):
            dispatcher.utter_template('utter_lab_ec', tracker)
        elif (course == 'ee'):
            dispatcher.utter_template('utter_lab_electrical', tracker)
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "course":self.from_entity(entity="course",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform")
        }

class ActionAdmission(FormAction):
    def name(self) -> Text:
        return "form_about_admission"
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
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


                elif all_entites2:

                    if all_entites2[-1]=="degree":
                        #print("fees with degree called last entity")
                        if tracker.get_slot(all_entites2[-1])=='bsc' or tracker.get_slot(all_entites2[-1])=='msc':
                            ACode('dc')
                            return ['degree','course']

                        else:
                            ACode('d')
                            return ["degree"]
                    elif(all_entites2[-1]=="qualification"):
                        if(tracker.get_slot('course')):
                            ACode('qc')
                            return ["qualification","course"]
                        elif(tracker.get_slot('field')):
                            ACode('qf')
                            return ["qualification","field"]
                        else:
                            ACode('qf')
                            return ["qualification","field"]
                    elif(all_entites2[-1]=="field"):
                        ACode('qf')
                        #print("fees with q,c called")
                        return ["qualification","field"]
                    elif(all_entites2[-1]=="course"):
                        ACode('qc')
                        #print("fees with q,c called")
                        return ["qualification","course"]
                    
                else:
                    ACode('d')
                    #print("fees with q,c called")
                    return ["degree"]      
        elif all_entites2:
            if all_entites2[-1]=="degree":
                #print("fees with degree called last entity")
                if tracker.get_slot(all_entites2[-1])=='bsc' or tracker.get_slot(all_entites2[-1])=='msc':
                    ACode('dc')
                    return ['degree','course']
                else:
                    ACode('d')
                    return ["degree"]
            elif(all_entites2[-1]=="course"):
                ACode('qc')
                #print("fees with q,c called")
                return ["qualification","course"]
            elif(all_entites2[-1]=="field"):
                ACode('qf')
                return ["qualification","field"]
            elif(all_entites2[-1]=="qualification"):
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
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "qualification":self.from_entity(entity="qualification",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform"),
            "degree":self.from_entity(entity="degree",intent="inform"),

        }
class Actioncommute(FormAction):
    def name(self) -> Text:
        return "form_about_locat"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ['location']

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[Dict]:
        loc = tracker.get_slot("location")
        if loc == 'ahmedabad':
            dispatcher.utter_template("utter_about_Abd", tracker)
        elif loc == 'vadodara':
            dispatcher.utter_template("utter_about_Vad", tracker)
        elif loc == 'vvnagar':
            dispatcher.utter_template("utter_about_Vv", tracker)
        elif loc == 'anand':
            dispatcher.utter_template("utter_about_And", tracker)
        elif loc == 'nadiad':
            dispatcher.utter_template("utter_about_Nad", tracker)
        else:
            dispatcher.utter_template("utter_about_unk_loc", tracker)
        return []

    def slot_mapping(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "location": self.from_entity(entity="location", intent="inform")
        }

class ActionPlacement(FormAction):
    def name(self) -> Text:
        return "form_about_placement"

    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        last(tracker)
        latest_entities=tracker.latest_message['entities']
        if latest_entities:
            for entity in latest_entities:
                if entity['entity']=='course':
                    plCode('c')
                    return ['course']
                if entity['entity']=='field':
                    if tracker.get_slot('field')=="engineering":
                        plCode('cf')
                        return ["field","course"]
                    else:
                        plCode('f')
                        return ["field"]
                else:
                    if all_entites3:
                        if all_entites3[-1]=="field":
                            if tracker.get_slot('field')=="engineering":
                                plCode('cf')
                                return ["field","course"]
                            else:
                                plCode('f')
                                return ["field"]
                        else:
                            plCode('f')
                            return ["field"]
                    else:
                        plCode('f')
                        return ["field"]

        if all_entites3:
            if all_entites3[-1]=="field":
                if tracker.get_slot('field')=="engineering":
                    plCode('cf')
                    return ["field","course"]
                else:
                    plCode('f')
                    return ["field"]
            else:
                plCode('f')
                return ["field"]
        else:
            plCode('f')
            return ["field"]

    def submit(self,dispatcher:CollectingDispatcher,tracker:Tracker,domain: Dict[Text, Any],)-> List[Dict]:
        print("placementCode: ",placementCodes[-1])
        field = tracker.get_slot('field')
        course = tracker.get_slot('course')
        if (field == "computer applications"):
            dispatcher.utter_template('utter_placement_statistics_cmpica', tracker)
        elif (field == "applied sciences"):
            dispatcher.utter_template('utter_placement_statistics_pdpias', tracker)
        elif(field=="management"):
            dispatcher.utter_template('utter_placement_statistics_i2im',tracker)
        elif placementCodes[-1]=='c':
            if (course == "ce" or course == "it" or course == "cs"):
                dispatcher.utter_template("utter_placement_statistics_CE", tracker)
            elif (course == 'me'):
                dispatcher.utter_template('utter_placement_statistics_ME', tracker)
            elif (course == 'cl'):
                dispatcher.utter_template('utter_placement_statistics_Civil', tracker)
            elif (course == 'ec'):
                dispatcher.utter_template('utter_placement_statistics_EC', tracker)
            elif (course == 'ee'):
                dispatcher.utter_template('utter_placement_statistics_Electrical', tracker)
            else:
                dispatcher.utter_message("Sorry we don't have any information about this. Please contact ")
        else:
            dispatcher.utter_message("Sorry we don't have any information about this. Please contact ")
        return []

    def slot_mapping(self)->Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "course":self.from_entity(entity="course",intent="inform"),
            "field":self.from_entity(entity="field",intent="inform")
        }