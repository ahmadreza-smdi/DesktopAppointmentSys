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


/* NOZHAN */

-- 8: Prescription text for patient whose appointment number is 12345
SELECT prescription
FROM prescription
WHERE visit_number = '12345';

-- 9: Patient names and their diseases who had an appointment on 2015-05-05
SELECT p.fname, p.lname, d.disease_name, d.description
FROM diseases d JOIN appointment a USING visit_number JOIN patient p USING id
WHERE a.appointment_time = '2015-05-05';

-- 10: Special diseases of patients with blood type A
SELECT id, special_disease
FROM patient
WHERE blood_type = 'A';

-- 11: All patients with their special diseases described
SELECT p.id, p.lname, p.special_disease, d.description
FROM patient p JOIN disease d USING id
WHERE p.special_disease = d.disease_name;

-- 12: Patients with HIV and their counselations
SELECT p.id, p.lname, a.advised, a.forbidden, a.frowned_upon
FROM patient p JOIN advice a USING id
WHERE p.special_disease = 'HIV';

-- 13: Prescriptions issued in September 2016
SELECT p.id, a.visit_number, pr.prescription
FROM prescription pr JOIN patient p USING id JOIN appointment a USING visit_number
WHERE a.appointment_time BETWEEN '2016-09-01' AND '2016-09-31';

-- 14: Patients with Diabetes who've at least visited once
SELECT p.* FROM patient p
WHERE EXISTS(SELECT null
              FROM appointment a
              WHERE a.id = p.id)
      AND p.special_disease = 'Diabetes'
      
=======

/* Vahid */

--15
/*توصیه دکتر به بیمار با شماره ویزیت 110*/
SELECT advised FROM advice WHERE id='110'

--16
/*نوع بیمه‌ی بیمار 'محمد' با شماره ویزیت '17' و تاریخ مراجعه‌ی 2018/08/17*/
SELECT insurance_type FROM insurance join patient using id join appointment on id
where fname='محمد' and appointment_time='20180817'

--17
/*نوع بیمه‌ی بیمارانی که هزینه نداده‌اند*/
SELECT insurance_type FROM insurance join appointment on id
WHERE payment_roll = 'null'

--18
/*توصیه‌های دکتر به بیماران با بیماری خاص اچ‌آی‌وی*/
SELECT advised FROM advice join patient on id
WHERE special_disease = 'HIV'

--19
/*نسخه، توصیه و موارد ممنوع بیمار با شماره عضویت 45681 و شماره ویزیت 13*/
SELECT prescription and advised and forbidden FROM prescription join advise using id join patient on id
WHERE id='45681' and visit_number='13'

--20
/*شماره تماس بیمار با شماره ویزیت 93 و تاریخ مراجعه‌ی 2018/05/03*/
SELECT phone_number FROM patient join appointment on id
WHERE visit_number = '93' and appointment_time = '20180503'

--21
/*شماره عضویت بیماران با نوع بیمه تکمیلی*/
SELECT id FROM insurance WHERE insurance_type = 'تکمیلی'
