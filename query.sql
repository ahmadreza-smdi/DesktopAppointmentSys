--1:name of the patient that have o blood type and  their insurance_type is khadamat darmani

select fname,lname from patient join insurance using id where insurance_type =="khadamat darmani"


--2:address of the patient where have b+ blood type and their special_disease was HIV

select address from patient where blood_type =='b+' and special_disease == 'HIV'


--3:name of the patient that have an appointment on 2018/01/20 and dont have insurance

select fname,lname from patient join appointment using id join insurance on id
where appointment_time.date =='20180120' and insurance_id = null


--4:prescription of the patient that their payment_roll was cash and have parkinson disease

select prescription from prescription join appointment on id join patient using id where
payment_roll = 'cash' and special_disease = 'parkinson'

--5:forbidden stuff for the patient with 911 id number

select forbidden from advice join patient using id

/* 6:categorize the patient with id  that have diabet and their insurance_type is tamin ejtemaee
and their blood_type is ab    */

select id from patient join insurance on id where special_disease = 'diabet' and blood_type = 'ab'
and insurance_type = 'tamin ejtemaee' group by id


--7:insurance type of the patient that have cancer

select insurance_type from patient join insurance on id where special_disease = 'cancer'
