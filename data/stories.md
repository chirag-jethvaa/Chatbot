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

## form for available programs
 * available_programs
  - form_programs
  - form{"name":"form_programs"} 
  - form{"name":null}

## form for hostels
 * about_hostel
  - form_about_hostels
  - form{"name":"form_about_hostels"} 
  - form{"name":null}
  - action_restart
  
## form for labs
 *lab_info
  - form_lab_info
  - form{"name":"form_lab_info"} 
  - form{"name":null}
  - action_restart
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

## out of sampark
 * out_of_scope
  - utter_out_of_scope
  
## abt internet info
* internet_info
   - utter_internet_info
  
## abt food
*food_availability
   - utter_food

## form for fees
* fees
  - form_about_fees
  - form{"name":"form_about_fees"}
  - form{"name":null}
  - action_restart

## form for fees happy path
 * greet
  - utter_greet
 * fees
  - form_about_fees
  - form{"name":"form_about_fees"}
  - form{"name":null}
  - action_restart
  
## form for placement
 *placement_info
  - form_about_placement
  - form{"name":"form_about_placement"} 
  - form{"name":null}
  - action_restart
  
## form for recruiter_company
 *placement_company_info
    - utter_placement_compaines_details