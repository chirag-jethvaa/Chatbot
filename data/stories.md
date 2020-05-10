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





## form for available programs
 * available_programs
  - form_programs
  - form{"name":"form_programs"} 
  - form{"name":null}


## form for available programs with agreement
 * available_programs
  - form_programs

  - form{"name":"form_programs"} 
  - form{"name":null}

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

## form for fees
 * fees
  - form_about_fees
  - form{"name":"form_about_fees"}
  - form{"name":null}

## form for fees happy path
 * greet
  - utter_greet
 * fees
  - form_about_fees
  - form{"name":"form_about_fees"}
  - form{"name":null}

## form for institute info
 * greet
  - utter_greet
 * about_institute
  - form_about_institute
  - form{"name":"form_about_institute"}
  - form{"name":null}
  <!-- - slot{'institute': null} -->


## form for institute info direct
 * about_institute
  - form_about_institute
  - form{"name":"form_about_institute"}
  - form{"name":null}
  <!-- - slot{'institute': null} -->


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



## about facilites path
* greet
 - utter_greet
* about_facility
 - utter_about_facilities
* goodbye
  - utter_goodbye

## about direct facilites path
* about_facility
 - utter_about_facilities