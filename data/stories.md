## happy path
* greet
  - utter_greet

## sad path 1
* greet
  - utter_greet

## sad path 2
* greet
  - utter_greet

* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye


## who_am_i
* i_am_robot
  - utter_i_am_robot


## hello_chrag
 * chirag
  - action_hello_world_chirag


## form for available programs with greet
 * greet
  - utter_greet
 * available_programs
  - form_programs
  - form{"name":"form_programs"} 
  - form{"name":null}
 * goodbye
  - utter_goodbye

## form for available programs 
 * available_programs
  - form_programs
  - form{"name":"form_programs"} 
  - form{"name":null}
 * goodbye
  - utter_goodbye


##about university happy path
 * greet
  - utter_greet
 * about_university
  - utter_about_university
 * goodbye
  - utter_goodbye

##about university direct
 * about_university
  - utter_about_university


## form for fees with course
 * fees
  - form_fees
  - form{"name":"form_fees"}
  - form{"name":null} 
 * goodbye
  - utter_goodbye

## programs with institute
* greet
 - utter_greet
* available_programs_with_institute
 - utter_available_programs_with_institute
 * goodbye
  - utter_goodbye

## out of sampark
 * out_of_scope
  - utter_out_of_scope


## form for hostels
* about_hostel
- form_about_hostels
- form{"name":"form_about_hostels"}
- form{"name":null}


## form for labs
* lab_info
- form_lab_info
- form{"name":"form_lab_info"}
- form{"name":null}


## form for admission process
* greet
- utter_greet
* admission_process
- form_about_admission
- form{"name":"form_about_admission"}
- form{"name":null}

## form for admission info direct
* admission_process
- form_about_admission
- form{"name":"form_about_admission"}
- form{"name":null}

## story for praising
* praising
- utter_thanks

## story for developer
* developer
- utter_developer

## story for bad about chatbot
* bad_about_chatbot
- utter_response_to_bad

## ask_about_events
* events
- utter_about_events

## story for commute
* commute
- form_about_locat
- form{"name":"form_about_locat"}
- form{"name":null}

## story for placement
* placement_info
- form_about_placement
- form{"name":"form_about_placement"}
- form{"name":null}

## story for why charusat
* why_charusat
- utter_why_charusat