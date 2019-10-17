# Desarrollado por:     Jorge Miguel Anaya Leon     C.C 1094859633
# Año:                  2019
# Proyecto:             SoftDataFusion

import os.path
import pandas
import datetime
import time
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from tkinter.font import nametofont
import urllib.request
import xport

NHANES_DATA = [[
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods",
    "Dietary Interview - Total Nutrient Intakes",
    "Dietary Interview Technical Support File - Food Code Format File",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 30-Day - File 1, Supplement Counts",
    "Dietary Supplement Use 30-Day - File 2, Participant's Use of Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DRXIFF.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DRXTOT.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DRXFMT.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSQFILE1.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSQFILE2.XPT"]
    ], 
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Balance",
    "Bioelectrical Impedance Analysis",
    "Blood Pressure",
    "Body Measures",
    "Cardiovascular Fitness",
    "Dual-Energy X-ray Absorptiometry - Whole Body",
    "Lower Extremity Disease - Ankle Brachial Blood Pressure Index",
    "Lower Extremity Disease - Peripheral Neuropathy",
    "Muscle Strength",
    "Oral Health - Dentition",
    "Oral Health - Periodontal",
    "Oral Health - Recommendation of Care",
    "Shared Exclusion Questions",
    "Tuberculosis",
    "Vision"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/AUX1.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/AUXAR.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/AUXTYM.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BAX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BIX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BPX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CVX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/Dxa/Dxa.aspx",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LEXABPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LEXPN.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/MSX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OHXDENT.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OHXPERIO.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OHXREF.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SEQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/TB.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/VIX.XPT"]
    ], 
    [
    ["Aflatoxin B1-lysine - Serum (Surplus)",
    "Albumin & Creatinine - Urine",
    "Anti-Mullerian Hormone (AMH) & Inhibin-B (Surplus)",
    "Autoantibodies - Immunofluorescence & Immunoprecipitation Analyses (Surplus)",
    "Cadmium, Lead, Mercury, Cotinine & Nutritional Biochemistries",
    "Chlamydia & Gonorrhea - Urine",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total & HDL",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "C-Reactive Protein (CRP)",
    "Cryptosporidum & Toxoplasma",
    "Cystatin C - Serum (Surplus)",
    "Cytomegalovirus Antibodies - Serum (Surplus)",
    "Cytomegalovirus Genotypes - Urine (Surplus)",
    "Cytomegalovirus IgG Antibodies - Serum (Surplus)",
    "Cytomegalovirus shedding - Urine (Surplus)",
    "Dioxins, Furans, & Coplanar PCBs",
    "Fasting Questionnaire",
    "Folic Acid - Unmetabolized (Surplus)",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody & Surface Antigen; Hepatitis C: Confirmed Antibody & RNA (HCV-RNA); Hepatitis D Antibody",
    "Herpes Simplex Virus Type-1 & Type-2",
    "Herpes Simplex Virus Type-1 (Surplus)",
    "HIV Antibody Test, CD4+ T Lymphocytes & CD8+ T Cells",
    "Latex",
    "Lead - Dust",
    "Measles, Rubella, & Varicella",
    "Mercury - Hair",
    "Metals - Urine",
    "Monoclonal gammopathy of undetermined significance (MGUS) (Surplus)",
    "Mumps Antibody - Serum (Surplus)",
    "Norovirus antibody - Serum",
    "Perfluoroaokyl Chemicals - Serum (Surplus)",
    "Pesticides - Current Use - Urine (Formerly Priority Pesticides, Non-persistent Pesticide Metabolites)",
    "Phthalates, Phytoestrogens & PAHs - Urine PHPYPA Urinary Phthalates",
    "Plasma Fasting Glucose, Serum C-peptide & Insulin",
    "Pregnancy Test - Urine",
    "Sex Steroid Hormone - Men (Surplus)",
    "Standard Biochemistry Profile & Hormones",
    "Telomere Mean and Standard Deviation (Surplus)",
    "Thyroid - Stimulating Hormone & Thyroxine (TSH & T4)",
    "Trans Fatty Acids",
    "Transferrin Receptor - Pregnant Women (Surplus)",
    "Varicella-Zoster Virus Antibody (Surplus)",
    "Volatile Organic Compounds - Blood & Water",
    "Volatile Organic Compounds (VOC) - Personal Exposure Badge"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSAFB_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB16.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSAMH_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSANA_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB06.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB05.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB13AM.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB13.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB25.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB11.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB17.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCYST_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCMV_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCMVG_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCMV_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSUCSH_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB28POC.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PH.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSFOL_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB10.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/L02HPA_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/L02HBS.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB02.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB09.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSHSV1_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB03.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB07.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB20.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB19.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB22.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB06HM.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSOL_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSMUMP_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSNORO_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSPFC_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB26PP.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PHPYPA.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB10AM.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/UC.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCHL_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB18.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/TELO_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB18T4.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/TFA_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSTFR_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSVARI_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB04.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/LAB21.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Analgesic Pain Relievers",
    "Audiometry",
    "Balance",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Cognitive Functioning",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Kidney Conditions",
    "Medical Conditions",
    "Mental Health - Depression",
    "Mental Health - Generalized Anxiety Disorder",
    "Mental Health - Panic Disorder",
    "Miscellaneous Pain",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Activity - Individual Activities",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Smoking - Adult Recent Tobacco Use & Youth Cigarette/Tobacco Use",
    "Smoking - Cigarette/Tobacco Use - Adult",
    "Smoking - Household Smokers",
    "Social Support",
    "Tuberculosis",
    "Vision",
    "Weight History"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/ACQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/ALQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_ANA.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/AUQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BAQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BPQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CDQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CFQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/HSQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DIQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DBQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DUQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/ECQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/FSQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/HIQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/HUQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/HOQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/IMQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/KIQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/MCQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CIQMDEP.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CIQGAD.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/CIQPANIC.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/MPQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OCQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OHQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/OSQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PUQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PAQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PAQIAF.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/PFQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_RX.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RHQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RDQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SXQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SMQMEC.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SMQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SMQFAM.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/TBQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/VIQ.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/WHQ.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DEMO_B.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods",
    "Dietary Interview - Total Nutrient Intakes",
    "Dietary Interview Technical Support File - Food Code Format File",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 30-Day - File 1, Supplement Counts",
    "Dietary Supplement Use 30-Day - File 2, Participant's Use of Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DRXIFF_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DRXTOT_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DRXFMT_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DSQ1_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DSQ2_B.XPT"]
    ],
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Balance",
    "Bioelectrical Impedance Analysis",
    "Blood Pressure",
    "Body Measures",
    "Cardiovascular Fitness",
    "Dual-Energy X-ray Absorptiometry - Whole Body",
    "Dual-Energy X-ray Absorptiometry - Whole Body, Second Exam",
    "Lower Extremity Disease - Ankle Brachial Blood Pressure Index",
    "Lower Extremity Disease - Peripheral Neuropathy",
    "Muscle Strength",
    "Oral Health - Dentition",
    "Oral Health - Periodontal/Lower",
    "Oral Health - Periodontal/Upper",
    "Oral Health - Recommendation of Care",
    "Vision"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/AUX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/AUXAR_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/AUXTYM_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BAX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BIX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BPX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BMX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CVX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/Dxa/Dxa.aspx",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DXX_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/LEXAB_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/LEXPN_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/MSX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OHXDEN_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OHXPRL_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OHXPRU_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OHXREF_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/VIX_B.XPT"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Anti-Mullerian Hormone (AMH) & Inhibin-B (Surplus)",
    "Autoantibodies - Immunofluorescence & Immunoprecipitation Analyses (Surplus)",
    "Bacterial vaginosis (BV) & Trichomonas vaginalis",
    "Brominated Flame Retardants (BFRs) - Pooled Samples (Surplus)",
    "Cadmium, Lead, Mercury, Cotinine & Nutritional Biochemistries",
    "Cadmium, Lead, Total Mercury, Ferritin, Serum Folate, RBC Folate, Vitamin B12, Homocysteine, Methylmalonic acid, Cotinine - Blood, Second Exam",
    "Chlamydia & Gonorrhea - Urine",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total & HDL",
    "Cholesterol - Total, HDL, LDL & Triglycerides, Second Exam",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Complete Blood Count with 5-part Differential - Whole Blood, Second Exam",
    "C-Reactive Protein & Others, Second Exam",
    "C-Reactive protein (CRP), Fibrinogen, Bone Alkaline Phosphatase & Urinary N-telopeptides",
    "Creatinine & Albumin - Urine, Second Exam",
    "Cystatin C (Surplus)",
    "Cytomegalovirus Antibodies - Serum (Surplus)",
    "Cytomegalovirus Genotypes - Urine (Surplus)",
    "Cytomegalovirus IgG Antibodies - Serum (Surplus)",
    "Cytomegalovirus shedding - Urine (Surplus)",
    "Dioxins, Furans, & Coplanar PCBs",
    "Erythrocyte Protoporphyrin",
    "Erythrocyte Protoporphyrin",
    "Fasting Questionnaire",
    "Glycohemoglobin",
    "Glycohemoglobin, Plasma Glucose, Serum C-peptide, & Insulin, Second Exam",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody & Surface Antigen; Hepatitis C: Confirmed Antibody & RNA (HCV-RNA); Hepatitis D Antibody",
    "Herpes Simplex Virus Type-1 & Type-2",
    "Herpes Simplex Virus Type-1 (Surplus)",
    "HIV Antibody Test, CD4+ T Lymphocytes & CD8+ T Cells",
    "Iodine - Urine",
    "Iron, Total Iron Binding Capacity (TIBC), & Transferrin Saturation",
    "Lead - Dust",
    "Measles, Rubella, & Varicella",
    "Measles, Rubella, & Varicella, Second Exam",
    "Metals - Urine",
    "Methicillin - Resistant Staphylococcus aureus (MRSA)",
    "Monoclonal gammopathy of undetermined significance (MGUS) (Surplus)",
    "Mumps Antibody - Serum (Surplus)",
    "Non-dioxin-like Polychlorinated Biphenyls - Pooled Samples (Surplus Sera)",
    "Perchlorate, Nitrate & Thiocyanate - Urine (Surplus)",
    "Pesticides - Current Use - Urine (Formerly Priority Pesticides, Non-persistent Pesticide Metabolites)",
    "Pesticides - Organochlorine Metabolites - Serum - Pooled Samples (Surplus)",
    "Phthalates, Phytoestrogens & PAHs - Urine",
    "Plasma Fasting Glucose, Serum C-peptide & Insulin",
    "Polyfluoroalkyl Chemicals - Pooled Samples (Surplus)",
    "Pregnancy Test - Urine",
    "Prostate specific antigen (PSA)",
    "Prostate-specific Antigen (PSA), Second Exam",
    "Sex Steroid Hormone - Men (Surplus)",
    "Standard Biochemistry Profile",
    "Standard Biochemistry Profile, Follicle Stimulating Hormone & Luteinizing Hormone, Second Exam",
    "Syphilis-IgG, Syphilis Rapid Plasma Reagin (RPR) & Treponema pallidum Particle Agglutination (TP-PA)",
    "Telomere Mean and Standard Deviation (Surplus)",
    "Thyroid - Stimulating Hormone & Thyroxine (TSH & T4)",
    "Thyroid Profile (Surplus)",
    "Toxoplasma (IgG), Toxoplasma (IgM),Toxoplasma (Dye),Toxoplasma Differential Agglutination, & Toxoplasma (Avidity)",
    "Transferrin Receptor - Pregnant Women (Surplus)",
    "Varicella-Zoster Virus Antibody (Surplus)",
    "Vitamin A, Vitamin E & Carotenoids",
    "Vitamin A, Vitamin E, & Carotenoids, Second Exam",
    "Vitamin D",
    "Volatile Organic Compounds - Blood & Water"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L16_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSAMH_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSANA_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L34_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSBFR_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L06_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L06_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L05_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L13AM_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L13_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L13_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L25_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L25_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L11_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L11_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L16_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSCYST_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSCMV_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCMVG_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSCMV_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSUCSH_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L28POC_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L39_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L39_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PH_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L10_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L10_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L02HPA_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L02HBS_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L02_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L09_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSHSV1_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L03_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L06UIO_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L40FE_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L20_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L19_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L19_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L06HM_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L35_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSOL_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSMUMP_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSPCB_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSNO3P_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L26PP_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSPST_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PHPYPA_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L10AM_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PFC_POOL.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/UC_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L11PSA_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L11P_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSCHL_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L40_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L40_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L36_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/TELO_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L40T4_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSNH4THY.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L17_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSTFR_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSVARI_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L06VIT_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/VIT_2_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/VID_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/L04VOC_B.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Analgesic Pain Relievers",
    "Audiometry",
    "Balance",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Cognitive Functioning",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression",
    "Mental Health - Generalized Anxiety Disorder",
    "Mental Health - Panic Disorder",
    "Miscellaneous Pain",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Activity - Individual Activities",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Prostate Conditions",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Smoking - Adult Recent Tobacco Use & Youth Cigarette/Tobacco Use",
    "Smoking - Cigarette/Tobacco Use - Adult",
    "Smoking - Household Smokers",
    "Social Support",
    "Vision",
    "Weight History"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/ACQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/ALQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/RXQANA_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/AUQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BAQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/BPQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CDQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CFQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/HSQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DEQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DIQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DBQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/DUQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/ECQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/FSQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/HIQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/HCQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/HUQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/HOQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/IMQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/KIQ_U_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/MCQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CIQDEP_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CIQGAD_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/CIQPAN_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/MPQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OCQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OHQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/OSQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PUQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PAQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PAQIAF_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/PFQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/RXQ_RX_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/KIQ_P_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/RHQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/RDQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SXQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SMQMEC_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SMQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SMQFAM_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/SSQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/VIQ_B.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/WHQ_B.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DEMO_C.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Interview Technical Support File - Modification Codes",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 30-Day - File 1, Supplement Counts",
    "Dietary Supplement Use 30-Day - File 2, Participant's Use of Supplements",
    "Food Frequency Questionnaire - Look-Up Table FOODLOOK",
    "Food Frequency Questionnaire - Look-Up Table VARLOOK",
    "Food Frequency Questionnaire - Output from DietCalc Software",
    "Food Frequency Questionnaire - Raw Questionnaire Responses"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DR1IFF_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DR2IFF_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DR1TOT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DR2TOT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DRXFCD_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DRXMCD_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DSQ1_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DSQ2_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/FOODLK_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/VARLK_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/FFQDC_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/FFQRAW_C.XPT"]
    ],
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Balance",
    "Bioelectrical Impedance Analysis",
    "Blood Pressure",
    "Body Measures",
    "Cardiovascular Fitness",
    "Dermatology",
    "Dual Energy X-ray Absorptiometry - Android/Gynoid",
    "Dual-Energy X-ray Absorptiometry - Whole Body",
    "Lower Extremity Disease - Ankle Brachial Blood Pressure Index",
    "Lower Extremity Disease - Peripheral Neuropathy",
    "Oral Health - Addendum",
    "Oral Health - Dentition",
    "Oral Health - Periodontal/Lower",
    "Oral Health - Periodontal/Upper",
    "Oral Health - Recommendation of Care",
    "Physical Activity Monitor",
    "Vision"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/AUX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/AUXAR_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/AUXTYM_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BAX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BIX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BPX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BMX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/CVX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DEX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DXXAG_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/Dxa/Dxa.aspx",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/LEXAB_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/LEXPN_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHXADD_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHXDEN_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHXPRL_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHXPRU_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHXREF_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PAXRAW_C.ZIP",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/VIX_C.XPT"]
    ],
    [
    ["Acrylamide & Glycidamide",
    "Albumin & Creatinine - Urine",
    "Anti-Mullerian Hormone (AMH) & Inhibin-B (Surplus)",
    "Arsenics - Total & Speciated - Urine",
    "Autoantibodies - Immunofluorescence & Immunoprecipitation Analyses (Surplus)",
    "Bacterial vaginosis (BV) & Trichomonas vaginalis",
    "Brominated Flame Retardants (BFRs)",
    "Cadmium, Lead, & Total Mercury - Blood",
    "Chlamydia & Gonorrhea - Urine",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total & HDL",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Cotinine - Serum",
    "Coxiella Burnetii (Q Fever) Antibodies - Serum (Surplus)",
    "C-Reactive Protein (CRP), Bone Alkaline Phosphatase (BAP) & Parathyroid Hormone (PTH)",
    "Cytomegalovirus Antibodies - Serum (Surplus)",
    "Cytomegalovirus Genotypes - Urine (Surplus)",
    "Cytomegalovirus IgG Antibodies - Serum (Surplus)",
    "Cytomegalovirus shedding - Urine (Surplus)",
    "Dioxins, Furans, & Coplanar PCBs",
    "Environmental Phenols",
    "Epstein-Barr Virus (VCA IgG) - Serum (Surplus)",
    "Erythrocyte Protoporphyrin & Selenium",
    "Fasting Questionnaire",
    "Fatty Acids - Plasma (Surplus)",
    "Ferritin & Transferrin Receptor",
    "Folate - RBC & Serum, and Vitamin B12",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody & Surface Antigen; Hepatitis C: Confirmed Antibody & RNA (HCV-RNA); Hepatitis D Antibody",
    "Hepatitis C RNA (HCV-RNA) & HCV Genotype (Surplus)",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test, CD4+ T Lymphocytes & CD8+ T Cells",
    "Human Papillomavirus (HPV) - 6, 11, 16 & 18 Antibody - Serum: 4-plex CLIA",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Digene Hybrid Capture & Prototype Line Blot Assay",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Roche Linear Array",
    "Iodine - Urine",
    "Iron, Total Iron Binding Capacity (TIBC), & Transferrin Saturation",
    "Lead - Dust",
    "Measles, Rubella, & Varicella",
    "Melamine - Urine (Surplus)",
    "Mercury - Inorganic, Urine",
    "Metals - Urine",
    "Methicillin - Resistant Staphylococcus aureus (MRSA)",
    "Methylmalonic acid & Homocysteine",
    "Monoclonal gammopathy of undetermined significance (MGUS) (Surplus)",
    "Mumps Antibody - Serum (Surplus)",
    "Non-dioxin-like Polychlorinated Biphenyls",
    "Norovirus antibody - Serum",
    "Organophosphate Insecticides - Diakyl Phosphate Metabolites - Urine",
    "Perchlorate - Urine",
    "Pesticides - Current Use - Urine (Formerly Priority Pesticides, Non-persistent Pesticide Metabolites)",
    "Pesticides - Environmental - Urine",
    "Pesticides - Organochlorine Metabolites - Serum (Surplus)",
    "Phthalates - Urine",
    "Phytoestrogens - Urine",
    "Plasma Fasting Glucose, Serum C-peptide & Insulin",
    "Polyaromatic Hydrocarbons (PAHs) - Urine",
    "Polyfluoroalkyl Chemicals",
    "Pregnancy Test - Urine",
    "Prostate Specific Antigen (PSA)",
    "Sex Steroid Hormone - Men (Surplus)",
    "Standard Biochemistry Profile",
    "Syphilis-IgG, Syphilis Rapid Plasma Reagin (RPR) & Treponema pallidum Particle Agglutination (TP-PA)",
    "Toxoplasma (IgG) & Toxoplasma (IgM)",
    "Varicella-Zoster Virus Antibody (Surplus)",
    "Vitamin A, Vitamin E & Carotenoids",
    "Vitamin B6",
    "Vitamin C",
    "Vitamin D",
    "Volatile Organic Compounds - Blood, Water, & Related Questionnaire Items"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06AGE_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L16_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSAMH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06UAS_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSANA_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L34_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L28PBE_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06BMT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L05_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L13AM_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L13_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L25_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06COT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSQFEV_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L11_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSCMV_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSCMVG_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSCMV_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/SSUCSH_A.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L28DFP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L24EPH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSEBV_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L39EPP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSFA_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06TFR_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06NB_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L10_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L02HPA_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L02HBS_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L02_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSHCVR_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L09_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L03_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L52SER_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L37SWA_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L37SWR_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06UIO_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L40FE_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L20_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L19_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSMEL_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06UHG_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06HM_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L35_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06MH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSOL_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSMUMP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L28NPB_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSNORO_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L26OPD_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L04PER_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L26UPP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L24PP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L28OCP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L24PH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06PHY_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L10AM_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L31PAH_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L24PFC_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/UC_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L11PSA_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSCHL_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L40_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L36_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L17_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSVARI_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L45VIT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L43_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L06VIT_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/VID_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/L04VOC_C.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Analgesic Pain Relievers",
    "Audiometry",
    "Balance",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression",
    "Mental Health - Generalized Anxiety Disorder",
    "Mental Health - Panic Disorder",
    "Miscellaneous Pain",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Activity - Individual Activities",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Prostate Conditions",
    "Prostate Specific Antigen Follow-up",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Smoking - Adult Recent Tobacco Use & Youth Cigarette/Tobacco Use",
    "Smoking - Cigarette/Tobacco Use - Adult",
    "Smoking - Household Smokers",
    "Social Support",
    "Vision",
    "Weight History"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/ACQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/ALQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/RXQANA_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/AUQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BAQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/BPQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/CDQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/HSQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DEQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DIQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DBQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/DUQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/ECQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/FSQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/HIQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/HCQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/HUQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/HOQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/IMQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/KIQ_U_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/MCQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/CIQDEP_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/CIQGAD_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/CIQPAN_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/MPQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OCQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OHQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/OSQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PUQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PAQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PAQIAF_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PFQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/RXQ_RX_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/KIQ_P_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/PSQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/RHQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/RDQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SXQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SMQMEC_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SMQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SMQFAM_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/SSQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/VIQ_C.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2003-2004/WHQ_C.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DEMO_D.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Interview Technical Support File - Modification Codes",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 30-Day - File 1, Supplement Counts",
    "Dietary Supplement Use 30-Day - File 2, Participant's Use of Supplements",
    "Food Frequency Questionnaire - Look-Up Table FOODLOOK",
    "Food Frequency Questionnaire - Look-Up Table VARLOOK",
    "Food Frequency Questionnaire - Output from DietCalc Software",
    "Food Frequency Questionnaire - Raw Questionnaire Responses"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DR1IFF_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DR2IFF_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DR1TOT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DR2TOT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DRXFCD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DRXMCD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DSQ1_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DSQ2_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FOODLK_D.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VARLK_D.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FFQDC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FFQRAW_D.XPT"]
    ],
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Blood Pressure",
    "Body Measures",
    "Dual Energy X-ray Absorptiometry - Android/Gynoid",
    "Dual Energy X-ray Absorptiometry - Femur",
    "Dual Energy X-ray Absorptiometry - Spine",
    "Dual-Energy X-ray Absorptiometry - Whole Body",
    "Dual-Energy X-ray Absorptiometry - Whole Body",
    "Ophthalmology - Frequency Doubling Technology",
    "Ophthalmology - Retinal Imaging",
    "Oral Health",
    "Physical Activity Monitor",
    "Vision"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AUX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AUXAR_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AUXTYM_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BPX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BMX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DXXAG_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DXXFEM_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DXXSPN_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/Dxa/Dxa.aspx",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DXX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OPXFDT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OPXRET_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OHX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PAXRAW_D.ZIP",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VIX_D.XPT"]
    ],
    [
    ["Acrylamide & Glycidamide",
    "Albumin & Creatinine - Urine",
    "Allergen Specific IgE(s) & Total IgE - Serum",
    "Allergens - Household Dust",
    "Arsenics - Total & Speciated - Urine",
    "Brominated Flame Retardants (BFRs) - Pooled Samples",
    "Cadmium, Lead, & Total Mercury - Blood",
    "Chlamydia & Gonorrhea - Urine",
    "Cholesterol - HDL",
    "Cholesterol - LDL, Triglyceride & Apoliprotein (ApoB)",
    "Cholesterol - Total",
    "Complete Blood Count with 5-Part Differential - Whole Blood",
    "Cotinine - Serum",
    "C-Reactive Protein (CRP)",
    "Environmental Phenols & Parabens",
    "Epstein-Barr Virus (VCA IgG) - Serum (Surplus)",
    "Erythrocyte Protoporphyrin",
    "Fasting Questionnaire",
    "Ferritin",
    "Folate - RBC & Serum",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody, Surface Antigen; Hepatitis D Antibody",
    "Hepatitis C: Confirmed Antibody, RNA (HCV-RNA), & Genotype",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test, CD4+ T Lymphocytes & CD8+ T Cells",
    "Homocysteine",
    "Human Papillomavirus (HPV) - 6, 11, 16 & 18 Antibody - Serum",
    "Human Papillomavirus (HPV) - 6, 11, 16 & 18 Antibody - Serum: 4-plex CLIA",
    "Human Papillomavirus (HPV) - Multiplexed 6, 11, 16, 18, 31, 22, 45, 52 & 58 Antibody - Serum: 9-plex CLIA",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Digene Hybrid Capture & Roche Linear Array",
    "Iodine - Urine",
    "Iron, Total Iron Binding Capacity (TIBC), & Transferrin Saturation",
    "Mercury - Inorganic - Blood",
    "Mercury - Inorganic, Urine",
    "Metals - Urine",
    "Non-dioxin-like Polychlorinated Biphenyls & Mono-ortho-substituted Polychlorinated Biphenyls - Pooled Samples",
    "Oral Glucose Tolerance Test",
    "Organophosphate Insecticides - Diakyl Phosphate Metabolites - Urine",
    "Parathyroid Hormone",
    "Perchlorate, Nitrate & Iodide - Tap Water",
    "Perchlorate, Nitrate & Thiocyanate - Urine",
    "Pesticides - Carbamates & Organophosphorus Metabolites - Urine",
    "Pesticides - Current Use - Urine (Formerly Priority Pesticides, Non-persistent Pesticide Metabolites)",
    "Pesticides - Environmental - Urine",
    "Pesticides - Organochlorine Metabolites - Serum - Pooled Samples (Surplus)",
    "Phthalates - Urine",
    "Phytoestrogens - Urine",
    "Plasma Fasting Glucose & Insulin",
    "Polyaromatic Hydrocarbons (PAHs) - Urine",
    "Polychlorinated dibenzo-p-dioxins (PCDDs), Dibenzofurans (PCDFs) & Coplanar Polychlorinated Biphenyls (cPCBs) - Pooled Samples",
    "Polyfluoroalkyl Chemicals",
    "Pooled-Sample Technical Support File",
    "Pregnancy Test - Urine",
    "Prostate Specific Antigen (PSA)",
    "Salmonella & Campylobacter Antibodies (Surplus)",
    "Standard Biochemistry Profile",
    "Transferrin Receptor",
    "Vitamin A, Vitamin E & Carotenoids",
    "Vitamin B12",
    "Vitamin B6",
    "Vitamin C",
    "Vitamin D",
    "Volatile Organic Compounds - Blood & Related Questionnaire Items",
    "Volatile Organic Compounds - Water & Related Questionnaire Items",
    "Volatile Organic Compounds & Metabolites - Urine (Surplus)"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AMDGYD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/ALB_CR_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AL_IGE_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/ALDUST_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UAS_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BFRPOL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PBCD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/CHLMDA_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HDL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/TRIGLY_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/TCHOL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/CBC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/COT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/CRP_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/EPH_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SSEBV_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/EPP_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FASTQX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FERTIN_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FOLATE_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/GHB_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HEPA_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HEPB_S_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HEPBD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HEPC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HSV_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HIV_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HCY_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HPVSER_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HPVSER_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HPVSRM_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HPVSWR_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UIO_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FETIB_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/IHG_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UHG_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UHM_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PCBPOL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OGTT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OPD_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PTH_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/WPIN_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PERNT_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/CARB_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UPP_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PP_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PSTPOL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PHTHTE_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PHYTO_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/GLU_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PAH_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DOXPOL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PFC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/POOLTF_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/UCPREG_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PSA_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SSSAL_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BIOPRO_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/TFR_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VITAEC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/B12_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VIT_B6_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VIC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VID_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VOCWB_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VOC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SSUVOC_D.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Allergy",
    "Audiometry",
    "Blood Pressure & Cholesterol",
    "Bowel Health",
    "Cardiovascular Health",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Activity - Individual Activities",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Prostate Conditions",
    "Prostate Specific Antigen Follow-up",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Social Support",
    "Vision",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/ACQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/ALQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AGQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/AUQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BPQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/BHQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/CDQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HSQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DEQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DIQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DBQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DUQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/ECQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/FSQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HIQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HCQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HUQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/HOQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/IMQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/KIQ_U_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/MCQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/DPQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OCQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OHQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/OSQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PUQMEC_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PAQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PAQIAF_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PFQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/RXQ_RX_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/KIQ_P_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/PSQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/RHQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/RDQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SXQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SLQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SMQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SMQFAM_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SMQRTU_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/SSQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/VIQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/WHQ_D.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2005-2006/WHQMEC_D.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DEMO_E.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Interview Technical Support File - Modification Codes",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, Second Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, Second Day",
    "Dietary Supplement Use 30 Day - Individual Dietary Supplements",
    "Dietary Supplement Use 30-Day - Total Dietary Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DR1IFF_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DR2IFF_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DR1TOT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DR2TOT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DRXFCD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DRXMCD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DS1IDS_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DS2IDS_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DS1TOT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DS2TOT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DSQIDS_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DSQTOT_E.XPT"]
    ],
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Blood Pressure",
    "Body Measures",
    "Dual Energy X-ray Absorptiometry - Femur",
    "Dual Energy X-ray Absorptiometry - Spine",
    "Exhaled Nitric Oxide",
    "Ophthalmology - Frequency Doubling Technology",
    "Ophthalmology - Retinal Imaging",
    "Oral Health",
    "Spirometry - Pre and Post-Bronchodilator",
    "Spirometry - Raw Curve Data",
    "Vision"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/AUX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/AUXAR_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/AUXTYM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BPX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BMX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DXXFEM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DXXSPN_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/ENX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OPXFDT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OPXRET_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OHX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SPX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SPXRAW_E.ZIP",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VIX_E.XPT"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Apolipoprotein B",
    "Arsenics - Total & Speciated - Urine",
    "Atrazine and Metabolites",
    "Brominated Flame Retardants (BFRs) - Pooled Samples",
    "Cadmium, Lead, & Total Mercury - Blood",
    "Chlamydia & Gonorrhea - Urine",
    "Cholesterol - HDL",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Cotinine - Serum & Total NNAL - Urine",
    "C-Reactive Protein (CRP)",
    "DEET and Metabolites",
    "Environmental Phenols",
    "Epstein-Barr Virus (VCA IgG) - Serum (Surplus)",
    "Fasting Questionnaire",
    "Ferritin",
    "Folate - RBC & Serum",
    "Folate Forms - Individual - Serum",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody, Surface Antigen; Hepatitis D Antibody",
    "Hepatitis C Antibody Reflex Testing - Serum (Surplus)",
    "Hepatitis C: Confirmed Antibody, RNA (HCV-RNA), & Genotype",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test",
    "Human Papillomavirus (HPV) - 6, 11, 16 & 18 Antibody - Serum: 4-plex CLIA",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Digene Hybrid Capture & Roche Linear Array",
    "Iodine - Urine",
    "Mercury - Inorganic - Blood",
    "Mercury - Inorganic, Urine",
    "Metals - Urine",
    "Non-dioxin-like Polychlorinated Biphenyls & Mono-ortho-substituted Polychlorinated Biphenyls (Surplus)",
    "Oral Glucose Tolerance Test",
    "Organophosphate Insecticides - Diakyl Phosphate Metabolites - Urine",
    "Perchlorate, Nitrate & Thiocyanate - Urine",
    "Pesticides - Carbamates & Organophosphorus Metabolites - Urine",
    "Pesticides - Current Use - Urine (Formerly Priority Pesticides, Non-persistent Pesticide Metabolites)",
    "Pesticides - Environmental - Urine",
    "Pesticides - Organochlorine Metabolites - Serum - Pooled Samples (Surplus)",
    "Phthalates - Urine",
    "Phytoestrogens - Urine",
    "Plasma Fasting Glucose & Insulin",
    "Polyaromatic Hydrocarbons (PAHs) - Urine",
    "Polychlorinated dibenzo-p-dioxins (PCDDs), Dibenzofurans (PCDFs) & Coplanar Polychlorinated Biphenyls (cPCBs) Pooled Samples",
    "Polyfluoroalkyl Chemicals",
    "Pooled-Sample Technical Support File",
    "Pregnancy Test - Urine",
    "Prostate Specific Antigen (PSA)",
    "Pyrethroids, Herbicides, & OP Metabolites - Urine",
    "Standard Biochemistry Profile",
    "Thyroid Profile",
    "Transferrin Receptor",
    "Urine Specific Gravity Measurement (Surplus)",
    "Vitamin B6",
    "Vitamin D",
    "Volatile Organic Compounds - Blood & Related Questionnaire Items",
    "Volatile Organic Compounds - Trihalomethanes/MTBE/Nitromethane - Blood",
    "Volatile Organic Compounds - Water & Related Questionnaire Items"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/ALB_CR_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/APOB_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UAS_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UAM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BFRPOL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PBCD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CHLMDA_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HDL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/TRIGLY_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/TCHOL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CBC_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/COTNAL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CRP_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DEET_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/EPH_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSEBV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/FASTQX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/FERTIN_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/FOLATE_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/FOLFMS_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/GHB_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HEPA_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HEPB_S_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HEPBD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSHCV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HEPC_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HSV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HIV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HPVSER_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HPVSWR_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UIO_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/IHG_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UHG_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UHM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PCBPOL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OGTT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OPD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PERNT_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CARB_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UPP_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PP_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PSTPOL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PHTHTE_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PHYTO_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/GLU_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PAH_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DOXPOL_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PFC_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/POOLTF_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UCPREG_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PSA_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/UPHOPM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BIOPRO_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/THYROD_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/TFR_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSUSG_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VIT_B6_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VID_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VOCWB_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VOCMWB_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VOC_E.XPT"]
    ],
    [
    ["Acculturation",
    "Air Quality",
    "Alcohol Use",
    "Audiometry",
    "Blood Pressure & Cholesterol",
    "Bowel Health",
    "Cardiovascular Health",
    "Consumer Behavior",
    "Consumer Behavior Phone Follow-up Module - Adult",
    "Consumer Behavior Phone Follow-up Module - Child",
    "Current Health Status",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Income",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Prostate Conditions",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Social Support",
    "Vision",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/ACQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/AQQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/ALQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/AUQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BPQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/BHQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CDQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CBQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CBQPFA_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/CBQPFC_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HSQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DIQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DBQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DUQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/ECQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/FSQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HIQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HCQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HUQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/HOQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/IMQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/INQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/KIQ_U_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/MCQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/DPQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OCQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OHQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/OSQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PUQMEC_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PAQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/PFQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/RXQ_RX_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/KIQ_P_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/RHQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/RDQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SXQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SLQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SMQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SMQFAM_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SMQRTU_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/VIQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/WHQ_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/WHQMEC_E.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Interview Technical Support File - Modification Codes",
    "Dietary Screener Questionnaire",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, Second Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, Second Day",
    "Dietary Supplement Use 30 Day - Individual Dietary Supplements",
    "Dietary Supplement Use 30-Day - Total Dietary Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DR1IFF_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DR2IFF_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DR1TOT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DR2TOT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DRXFCD_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DRXMCD_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DTQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DS1IDS_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DS2IDS_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DS1TOT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DS2TOT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DSQIDS_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DSQTOT_F.XPT"]
    ],
    [
    ["Arthritis Body Measures",
    "Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Blood Pressure",
    "Body Measures",
    "Dual Energy X-ray Absorptiometry - Femur",
    "Dual Energy X-ray Absorptiometry - Spine",
    "Exhaled Nitric Oxide",
    "Oral Health - Dentition",
    "Oral Health - Periodontal",
    "Oral Health - Recommendation of Care",
    "Spirometry - Pre and Post-Bronchodilator",
    "Spirometry - Raw Curve Data"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ARX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/AUX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/AUXAR_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/AUXTYM_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BPX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BMX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DXXFEM_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DXXSPN_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ENX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OHXDEN_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OHXPER_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OHXREF_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SPX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SPXRAW_F.ZIP"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Apolipoprotein B",
    "Arsenics - Total & Speciated - Urine",
    "Brominated Flame Retardants (BFRs) - Pooled Samples",
    "Cadmium, Lead, & Total Mercury - Blood",
    "Caffeine & Caffeine Metabolites - Urine",
    "Chlamydia - Urine",
    "Cholesterol - HDL",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Cotinine - Serum & Total NNAL - Urine",
    "C-Reactive Protein (CRP)",
    "DEET and Metabolites",
    "Environmental Phenols",
    "Epstein-Barr Virus (VCA IgG) - Serum (Surplus)",
    "Fasting Questionnaire",
    "Ferritin",
    "Folate - RBC & Serum",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody, Surface Antigen; Hepatitis D Antibody",
    "Hepatitis C Antibody Reflex Testing - Serum (Surplus)",
    "Hepatitis C: Confirmed Antibody, RNA (HCV-RNA), & Genotype",
    "Hepatitis E : IgG & IgM Antibodies",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test",
    "Human Papillomavirus (HPV) - 6, 11, 16 & 18 Antibody - Serum",
    "Human Papillomavirus (HPV) - Oral Rinse",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Digene Hybrid Capture & Roche Linear Array",
    "Human Papillomavirus (HPV) Viral Load - Oral Rinse - Oral High-Risk HPV Infections (Surplus)",
    "Iodine - Urine",
    "Measles, Mumps, Rubella & Varicella",
    "Mercury - Inorganic - Blood",
    "Mercury - Inorganic, Urine",
    "Metals - Urine",
    "Non-dioxin-like Polychlorinated Biphenyls & Mono-ortho-substituted Polychlorinated Biphenyls - Pooled Samples",
    "Oral Glucose Tolerance Test",
    "Osmolality - Urine",
    "Perchlorate, Nitrate & Thiocyanate - Urine",
    "Pesticides - Environmental - Urine",
    "Pesticides - Organochlorine Pesticides - Serum - Pooled Samples",
    "Phthalates - Urine",
    "Phytoestrogens - Urine",
    "Plasma Fasting Glucose & Insulin",
    "Poliovirus Serotypes 1, 2, & 3 Antibodies - Serum (Surplus)",
    "Polyaromatic Hydrocarbons -Urine",
    "Polychlorinated dibenzo-p-dioxins (PCDDs), Dibenzofurans (PCDFs) & Coplanar Polychlorinated Biphenyls (cPCBs) - Pooled Samples",
    "Polyfluoroalkyl Chemicals",
    "Pooled-Sample Technical Support File",
    "Pregnancy Test - Urine",
    "Prostate Specific Antigen (PSA)",
    "Pyrethroids, Herbicides, & OP Metabolites - Urine",
    "Standard Biochemistry Profile",
    "Thyroid Profile",
    "Tissue Transglutaminase Assay (IgA-TTG) & IgA Endomyseal Antibody Assay (IgA EMA)",
    "Toxoplasma Gondii Antibody - Serum (Surplus)",
    "Trans Fatty Acids",
    "Transferrin Receptor",
    "Urine Flow Rate",
    "Vitamin B6",
    "Vitamin D",
    "Volatile Organic Compounds (VOCs) - Blood",
    "Volatile Organic Compounds (VOCs) - Trihalomethanes/MTBE/Nitromethane - Blood",
    "Volatile Organic Compounds (VOCs) - Water"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ALB_CR_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/APOB_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UAS_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BFRPOL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PBCD_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CAFE_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CHLMDA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HDL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/TRIGLY_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/TCHOL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CBC_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/COTNAL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CRP_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DEET_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/EPH_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SSEBV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/FASTQX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/FERTIN_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/FOLATE_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/GHB_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HEPA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HEPB_S_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HEPBD_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSHCV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HEPC_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HEPE_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HSV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HIV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HPVSER_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ORHPV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HPVSWR_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SSHPV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UIO_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/MMRV_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/IHG_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UHG_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UHM_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PCBPOL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OGTT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UCOSMO_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PERNT_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PP_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PSTPOL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PHTHTE_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PHYTO_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/GLU_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SSPOLI_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PAH_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DOXPOL_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PFC_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/POOLTF_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UCPREG_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PSA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UPHOPM_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BIOPRO_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/THYROD_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/TGEMA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SSTOXO_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/TFA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/TFR_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/UCFLOW_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VIT_B6_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VID_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VOCWB_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VOCMWB_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VOC_F.XPT"]
    ],
    [
    ["Acculturation",
    "Air Quality",
    "Alcohol Use",
    "Alcohol Use (Ages 18-19)",
    "Arthritis",
    "Audiometry",
    "Blood Pressure & Cholesterol",
    "Bowel Health",
    "Cardiovascular Health",
    "Consumer Behavior",
    "Consumer Behavior Phone Follow-up Module - Adult",
    "Consumer Behavior Phone Follow-up Module - Child",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Income",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Volatile Toxicant (Subsample)",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ACQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/AQQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ALQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ALQY_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ARQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/AUQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BPQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/BHQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CDQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CBQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CBQPFA_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/CBQPFC_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HSQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DEQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DIQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DBQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DUQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/ECQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/FSQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HIQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HCQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HUQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/HOQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/IMQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/INQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/KIQ_U_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/MCQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/DPQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OCQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OHQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/OSQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PUQMEC_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PAQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/PFQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/RXQ_RX_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/RHQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/RDQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SXQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SLQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SMQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SMQFAM_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/SMQRTU_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/VTQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/WHQ_F.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2009-2010/WHQMEC_F.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Interview Technical Support File - Modification Codes",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, Second Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, Second Day",
    "Dietary Supplement Use 30 Day - Individual Dietary Supplements",
    "Dietary Supplement Use 30-Day - Total Dietary Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DR1IFF_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DR2IFF_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DR1TOT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DR2TOT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DRXFCD_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DRXMCD_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DS1IDS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DS2IDS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DS1TOT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DS2TOT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DSQIDS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DSQTOT_G.XPT"]
    ],
    [
    ["Audiometry",
    "Audiometry - Acoustic Reflex",
    "Audiometry - Tympanometry",
    "Blood Pressure",
    "Body Measures",
    "Exhaled Nitric Oxide",
    "Fluorosis - Clinical",
    "Muscle Strength - Grip Test",
    "Oral Health - Dentition",
    "Oral Health - Periodontal",
    "Oral Health - Recommendation of Care",
    "Spirometry - Pre and Post-Bronchodilator",
    "Spirometry - Raw Curve Data",
    "Tuberculosis"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/AUX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/AUXAR_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/AUXTYM_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/BPX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/BMX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ENX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FLXCLN_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/MGX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXPER_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXREF_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SPX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SPXRAW_G.ZIP",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TBX_G.XPT"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Antibody to Toxocara spp. (Surplus)",
    "Apolipoprotein B",
    "Arsenics - Total & Speciated - Urine",
    "Arsenics - Total & Speciated - Urine - Special Sample",
    "Brominated Flame Retardants (BFRs) - Serum - Pooled Samples",
    "Cadmium, Lead, Total Mercury, Selenium, & Manganese - Blood",
    "Chlamydia - Urine",
    "Cholesterol - HDL",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Copper, Selenium & Zinc - Serum",
    "Cotinine - Serum & Total NNAL - Urine",
    "Cytomegalovirus IgG & IgM Antibodies - Serum",
    "DEET and Metabolites",
    "Environmental Phenols & Parabens",
    "Fasting Questionnaire",
    "Fatty Acids - Serum",
    "Folate - RBC",
    "Folate Forms - Total & Individual - Serum",
    "Glycohemoglobin",
    "Hepatitis A Antibody",
    "Hepatitis B Surface Antibody",
    "Hepatitis B: Core Antibody, Surface Antigen; Hepatitis D Antibody",
    "Hepatitis C Antibody Reflex Testing - Serum (Surplus)",
    "Hepatitis C: Confirmed Antibody, RNA (HCV-RNA), & Genotype",
    "Hepatitis E : IgG & IgM Antibodies",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test",
    "Human Papillomavirus (HPV) - Oral Rinse",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Digene Hybrid Capture & Roche Linear Array",
    "Iodine - Urine",
    "Mercury - Inorganic, Ethyl & Methyl - Blood",
    "Mercury - Inorganic, Urine",
    "Metals - Urine",
    "Metals - Urine - Special Sample",
    "Methylmalonic Acid",
    "Non-dioxin-like Polychlorinated Biphenyls & Mono-ortho-substituted Polychlorinated Biphenyls - Serum - Pooled Samples",
    "Oral Glucose Tolerance Test",
    "Osmolality - Urine",
    "Perchlorate, Nitrate & Thiocyanate - Urine",
    "Perchlorate, Nitrate & Thiocyanate - Urine - Special Sample",
    "Pesticides - Environmental - Urine",
    "Pesticides - Organochlorine Pesticides - Serum - Pooled Samples",
    "Phthalates & Plasticizers Metabolites - Urine",
    "Plasma Fasting Glucose & Insulin",
    "Polyaromatic Hydrocarbons (PAHs) - Urine",
    "Polyaromatic Hydrocarbons (PAHs)- Urine - Special Sample",
    "Polyfluoroalkyl Chemicals",
    "Pooled-Sample Technical Support File",
    "Pregnancy Test - Urine",
    "Standard Biochemistry Profile",
    "Thyroid Profile",
    "Tissue Transglutaminase Assay (IgA-TTG) & IgA Endomyseal Antibody Assay (IgA EMA)",
    "Total Testosterone",
    "Toxoplasma gondii Antibody - Serum (Surplus)",
    "Tuberculosis - Quantiferon_In_Gold",
    "Urine Flow Rate",
    "Vitamin B12",
    "Vitamin D",
    "Volatile Organic Compounds & Metabolites - Urine",
    "Volatile Organic Compounds & Metabolites - Urine - Special Sample",
    "Volatile Organic Compounds (VOCs) - Blood",
    "Volatile Organic Compounds (VOCs) - Trihalomethanes/MTBE/Nitromethane - Blood"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ALB_CR_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SSTOCA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/APOB_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UAS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UASS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/BFRPOL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PBCD_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CHLMDA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HDL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TRIGLY_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TCHOL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CBC_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CUSEZN_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/COTNAL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CMV_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEET_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/EPH_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FASTQX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FAS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FOLATE_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FOLFMS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/GHB_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HEPA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HEPB_S_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HEPBD_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2007-2008/SSHCV_E.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HEPC_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HEPE_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HSV_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HIV_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ORHPV_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HPVSWR_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UIO_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/IHGEM_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UHG_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UHM_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UHMS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/MMA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PCBPOL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OGTT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UCOSMO_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PERNT_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PERNTS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PP_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PSTPOL_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PHTHTE_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/GLU_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PAH_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PAHS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PFC_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/POOLTF_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UCPREG_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/BIOPRO_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/THYROD_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TGEMA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TST_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SSTOXO_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TB_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UCFLOW_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/VITB12_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/VID_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UVOC_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/UVOCS_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/VOCWB_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/VOCMWB_G.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Audiometry",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Cognitive Functioning",
    "Consumer Behavior",
    "Creatine Kinase",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis C Follow Up",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Income",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Pesticide Use",
    "Physical Activity",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Preventive Aspirin Use",
    "Reproductive Health",
    "Respiratory Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Taste & Smell",
    "Tuberculosis",
    "Volatile Toxicant (Subsample)",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ACQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ALQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/AUQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/BPQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CDQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CFQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CBQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CKQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HSQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DIQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DBQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DUQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/ECQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/FSQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HIQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HCQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HUQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/HOQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/IMQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/INQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/KIQ_U_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/MCQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DPQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OCQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PUQMEC_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PAQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/PFQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/RXQ_RX_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/RXQASA_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/RHQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/RDQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SXQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SLQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SMQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SMQFAM_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/SMQRTU_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/CSQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/TBQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/VTQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/WHQ_G.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/WHQMEC_G.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes",
    "Dietary Supplement Database - Blend Information",
    "Dietary Supplement Database - Ingredient Information",
    "Dietary Supplement Database - Product Information",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Individual Dietary Supplements, Second Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, First Day",
    "Dietary Supplement Use 24-Hour - Total Dietary Supplements, Second Day",
    "Dietary Supplement Use 30-Day - Individual Dietary Supplements",
    "Dietary Supplement Use 30-Day - Total Dietary Supplements"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DR1IFF_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DR2IFF_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DR1TOT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DR2TOT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DRXFCD_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSBI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSII.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DSPI.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DS1IDS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DS2IDS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DS1TOT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DS2TOT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DSQIDS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DSQTOT_H.XPT"]
    ],
    [
    ["Dual-Energy X-ray Absorptiometry - L3 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - L4 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - Spine",
    "Dual-Energy X-ray Absorptiometry - T10 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T11 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T12 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T4 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T5 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T6 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T7 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T8 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - T9 Vertebrae Morphology",
    "Dual-Energy X-ray Absorptiometry - Vertebral Fracture Assessment",
    "Fluorosis - Clinical",
    "Muscle Strength - Grip Test",
    "Oral Health - Dentition",
    "Oral Health - Periodontal",
    "Oral Health - Recommendation of Care",
    "Taste & Smell"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/BPX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/BMX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXAAC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXFEM_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXFRX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXL1_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXL2_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXL3_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXL4_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXSPN_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT10_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT11_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT12_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT4_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT5_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT6_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT7_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT8_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXT9_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DXXVFA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FLXCLN_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/MGX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXPER_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXREF_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CSX_H.XPT"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Aldehydes - Serum",
    "Aldehydes - Serum - Special Sample",
    "Antibody to Toxocara spp. (Surplus)",
    "Apolipoprotein B",
    "Arsenic - Total - Urine",
    "Arsenic - Total - Urine - Special Sample",
    "Arsenics - Speciated - Urine",
    "Arsenics - Speciated - Urine - Special Sample",
    "Blood Lead, Cadmium, Total Mercury, Selenium, and Manganese",
    "Blood mercury: inorganic, ethyl and methyl",
    "Brominated Flame Retardants (BFRs) - Serum - Pooled Samples",
    "Chlamydia - Urine",
    "Cholesterol - HDL",
    "Cholesterol - LDL & Triglycerides",
    "Cholesterol - Total",
    "Complete Blood Count with 5-part Differential - Whole Blood",
    "Copper, Selenium & Zinc - Serum",
    "Cotinine and Hydroxycotinine - Serum",
    "DEET and Metabolites",
    "Fasting Questionnaire",
    "Flame Retardant Metabolites - Urine (Surplus)",
    "Fluoride - Plasma",
    "Fluoride - Water",
    "Folate - RBC",
    "Folate Forms - Total & Individual - Serum",
    "Glycohemoglobin",
    "Hepatitis A",
    "Hepatitis B: core antibody, surface antigen, and Hepatitis D antibody",
    "Hepatitis B: Surface Antibody",
    "Hepatitis C: Confirmed Antibody (INNO-LIA)",
    "Hepatitis C: RNA (HCV-RNA) and Hepatitis C Genotype",
    "Hepatitis E: IgG & IgM Antibodies",
    "Herpes Simplex Virus Type-1 & Type-2",
    "Heterocyclic Aromatic Amines - Urine",
    "Heterocyclic Aromatic Amines (HCAA) - Urine - Special Sample",
    "HIV Antibody Test",
    "Human Papillomavirus (HPV) - Oral Rinse",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Roche Cobas & Roche Linear Array",
    "Human Papillomavirus (HPV) DNA Results from Penile Swab Samples: Roche Linear Array",
    "Insulin",
    "Iodine - Urine",
    "Mercury - Urine",
    "Metals - Urine",
    "Metals - Urine - Special Sample",
    "Methylmalonic Acid",
    "Non-dioxin-like Polychlorinated Biphenyls & Mono-ortho-substituted Polychlorinated Biphenyls - Serum - Pooled Samples",
    "Oral Glucose Tolerance Test",
    "Perchlorate, Nitrate & Thiocyanate - Urine",
    "Perchlorate, Nitrate & Thiocyanate - Urine - Special Sample",
    "Perfluoroalkyl and Polyfluoroalkyl Substances",
    "Perfluoroalkyl and Polyfluoroalkyl Substances - Linear and Branched PFOS and PFOA Isomers (Surplus)",
    "Perfluoroalkyl and Polyfluoroalkyl Substances (formerly Polyfluoroalkyl Chemicals - PFC)",
    "Perfluoroalkyl and Polyfluoroalkyl Substances in US children 3-11 Years of Age",
    "Personal Care and Consumer Product Chemicals and Metabolites",
    "Pesticides - Organochlorine Pesticides - Serum - Pooled Samples",
    "Phthalates and Plasticizers Metabolites - Urine",
    "Phthalates and Plasticizers Metabolites - Urine (Surplus)",
    "Plasma Fasting Glucose",
    "Polycyclic Aromatic Hydrocarbons (PAH) - Urine",
    "Pooled-Sample Technical Support File",
    "Pregnancy Test - Urine",
    "Sex Steroid Hormone - Serum",
    "Standard Biochemistry Profile",
    "Tissue Transglutaminase Assay (IgA-TTG) & IgA Endomyseal Antibody Assay (IgA EMA)",
    "Tobacco-specific Nitrosamines (TSNAs) - Urine",
    "Toxoplasma gondii Antibody - Serum (Surplus)",
    "Trichomonas - Urine",
    "Urine Flow Rate",
    "Vitamin B12",
    "Vitamin D",
    "Volatile N-Nitrosamine Compounds (VNAs) - Urine",
    "Volatile N-Nitrosamine Compounds (VNAs) - Urine - Special Sample",
    "Volatile Organic Compounds & Metabolites - Urine",
    "Volatile Organic Compounds & Metabolites - Urine",
    "Volatile Organic Compounds (VOCs) and Trihalomethanes/MTBE - Blood - Special Sample",
    "Volatile Organic Compounds and Trihalomethanes/MTBE - Blood"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ALB_CR_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ALD_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ALDS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSTOCA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/APOB_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UTAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UTASS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UASS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PBCD_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/IHGEM_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/BFRPOL_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CHLMDA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HDL_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TRIGLY_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TCHOL_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CBC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CUSEZN_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/COT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEET_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FASTQX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSFLRT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FLDEP_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FLDEW_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FOLATE_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FOLFMS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/GHB_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEPA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEPBD_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEPB_S_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSHEPC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEPC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEPE_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HSV_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HCAA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HCAAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HIV_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ORHPV_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HPVSWR_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HPVP_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/INS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UIO_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UHG_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UM_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UMS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/MMA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PCBPOL_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OGTT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PERNT_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PERNTS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSPFSU_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSPFAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PFAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSPFAC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/EPHPP_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PSTPOL_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PHTHTE_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSPHTE_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/GLU_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PAH_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/POOLTF_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UCPREG_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TST_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/BIOPRO_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TGEMA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TSNA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SSTOXO_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/TRICH_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UCFLOW_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VITB12_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VID_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VNA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VNAS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UVOC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/UVOCS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VOCWBS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VOCWB_H.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Cognitive Functioning",
    "Consumer Behavior",
    "Creatine Kinase",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Disability",
    "Drug Use",
    "Early Childhood",
    "Food Security",
    "Health Insurance",
    "Hepatitis",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Income",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Osteoporosis",
    "Pesticide Use",
    "Physical Activity",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Preventive Aspirin Use",
    "Reproductive Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Smoking - Secondhand Smoke Exposure",
    "Taste & Smell",
    "Volatile Toxicant (Subsample)",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ACQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ALQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/BPQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CDQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CFQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CBQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CKQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HSQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DIQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DBQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DLQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DUQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/ECQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/FSQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HIQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HEQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HUQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/HOQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/IMQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/INQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/KIQ_U_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/MCQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DPQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OCQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OSQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PUQMEC_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PAQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/PFQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/RXQ_RX_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/RXQASA_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/RHQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SXQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SLQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SMQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SMQFAM_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SMQRTU_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/SMQSHS_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/CSQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/VTQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/WHQ_H.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/WHQMEC_H.XPT"]
    ]
    ], [
    [
    ["Demographic Variables & Sample Weights"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT"]
    ],
    [
    ["Dietary Interview - Individual Foods, First Day",
    "Dietary Interview - Individual Foods, Second Day",
    "Dietary Interview - Total Nutrient Intakes, First Day",
    "Dietary Interview - Total Nutrient Intakes, Second Day",
    "Dietary Interview Technical Support File - Food Codes"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DR1IFF_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DR2IFF_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DR1TOT_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DR2TOT_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DRXFCD_I.XPT"]
    ],
    [
    ["Blood Pressure",
    "Body Measures",
    "Fluorosis - Clinical",
    "Oral Health - Dentition",
    "Oral Health - Recommendation of Care"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FLXCLN_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXREF_I.XPT"]
    ],
    [
    ["Albumin & Creatinine - Urine",
    "Apolipoprotein B",
    "Aromatic Diamines - Urine",
    "Arsenic - Total - Urine - Special Sample (Subsample)",
    "Arsenic - Total - Urine (Subsample)",
    "Blood Lead, Cadmium, Total Mercury, Selenium, and Manganese",
    "Blood mercury: inorganic, ethyl and methyl",
    "Chlamydia - Urine",
    "Cholesterol - High-Density Lipoprotein (HDL)",
    "Cholesterol - Low - Density Lipoprotein (LDL) & Triglycerides",
    "Cholesterol - Total",
    "Chromium & Cobalt",
    "Complete Blood Count with 5-Part Differential - Whole Blood",
    "Copper, Selenium & Zinc - Serum",
    "Cotinine and Hydroxycotinine - Serum",
    "Fasting Questionnaire",
    "Fluoride - Plasma",
    "Fluoride - Water",
    "Folate - RBC",
    "Folate Forms - Total & Individual - Serum",
    "Glycohemoglobin",
    "Hepatitis A",
    "Hepatitis B: Core antibody, Surface antigen, and Hepatitis D antibody",
    "Hepatitis B: Surface Antibody",
    "Hepatitis C: RNA (HCV-RNA) and Hepatitis C Genotype",
    "Hepatitis E: IgG & IgM Antibodies",
    "Herpes Simplex Virus Type-1 & Type-2",
    "HIV Antibody Test",
    "Human Papillomavirus (HPV) - Oral Rinse",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Roche Cobas High-Risk",
    "Human Papillomavirus (HPV) DNA - Vaginal Swab: Roche Linear Array",
    "Imidacloprid, 5-Hydroxy imidacloprid, Acetamiprid, N-desmethyl Acetamiprid, Clothianidin, and Thiacloprid in NHANES 2015-16 Surplus Urine",
    "Insulin",
    "Iodine - Urine",
    "Mercury - Urine",
    "Metals - Urine",
    "Metals - Urine - Special Sample (Subsample)",
    "Mono-2-ethyl-5-hydroxyhexyl terephthalate, mono-2-ethyl-5-carboxypentyl terephthalate, and monooxoisononyl phthalate - Urine (Surplus)",
    "Oral Glucose Tolerance Test",
    "Perfluoroalkyl and Polyfluoroalkyl",
    "Personal Care and Consumer Product Chemicals and Metabolites",
    "Phthalates and Plasticizers Metabolites - Urine",
    "Plasma Fasting Glucose",
    "Pregnancy Test - Urine",
    "Sex Steroid Hormone - Serum",
    "Speciated Arsenics - Urine - Special Sample (Subsample)",
    "Speciated Arsenics - Urine (Subsample)",
    "Standard Biochemistry Profile",
    "Trichomonas - Urine",
    "Urine Flow Rate",
    "Volatile Organic Compound (VOC) Metabolites - Urine",
    "Volatile Organic Compound (VOC) Metabolites - Urine - Special Sample",
    "Volatile Organic Compounds and Trihalomethanes/MTBE - Blood",
    "Volatile Organic Compounds and Trihalomethanes/MTBE - Blood - Special Sample"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/ALB_CR_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/APOB_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UADM_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UTASS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UTAS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PBCD_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/IHGEM_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CHLMDA_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HDL_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/TRIGLY_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/TCHOL_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CRCO_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CBC_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CUSEZN_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/COT_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FASTQX_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FLDEP_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FLDEW_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FOLATE_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/FOLFMS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/GHB_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEPA_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEPBD_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEPB_S_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEPC_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEPE_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HSV_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HIV_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/ORHPV_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HPVSWC_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HPVSWR_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SSNEON_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/INS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UIO_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UHG_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UM_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UMS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SSMHHT_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OGTT_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PFAS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/EPHPP_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PHTHTE_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/GLU_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UCPREG_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/TST_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UASS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UAS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BIOPRO_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/TRICH_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UCFLOW_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UVOC_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/UVOCS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/VOCWB_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/VOCWBS_I.XPT"]
    ],
    [
    ["Acculturation",
    "Alcohol Use",
    "Audiometry",
    "Blood Pressure & Cholesterol",
    "Cardiovascular Health",
    "Consumer Behavior",
    "Current Health Status",
    "Dermatology",
    "Diabetes",
    "Diet Behavior & Nutrition",
    "Disability",
    "Drug Use",
    "Early Childhood",
    "Health Insurance",
    "Hepatitis",
    "Hospital Utilization & Access to Care",
    "Housing Characteristics",
    "Immunization",
    "Income",
    "Kidney Conditions - Urology",
    "Medical Conditions",
    "Mental Health - Depression Screener",
    "Occupation",
    "Oral Health",
    "Physical Activity",
    "Physical Functioning",
    "Prescription Medications",
    "Prescription Medications - Drug Information",
    "Preventive Aspirin Use",
    "Reproductive Health",
    "Sexual Behavior",
    "Sleep Disorders",
    "Smoking - Cigarette Use",
    "Smoking - Household Smokers",
    "Smoking - Recent Tobacco Use",
    "Smoking - Secondhand Smoke Exposure",
    "Weight History",
    "Weight History - Youth"], 
    ["https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/ACQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/ALQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/AUQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CDQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/CBQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HSQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DIQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DBQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DLQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DUQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/ECQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HIQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HEQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HUQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/HOQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/IMQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/INQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/KIQ_U_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/MCQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DPQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OCQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PAQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PFQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/RXQ_RX_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/RXQ_DRUG.xpt",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/RXQASA_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/RHQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SXQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SLQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SMQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SMQFAM_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SMQRTU_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/SMQSHS_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/WHQ_I.XPT",
    "https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/WHQMEC_I.XPT"]
    ]
    ]]

def FuseData(self, InfoVariable, default, exportto):
    NameFile = ""
    Files = list()
    ii = 0
    s = 1
    for i in range(0, len(InfoVariable)):
        Temp = list()
        i = ii
        s = 1
        for j in range(i, len(InfoVariable)):
            if InfoVariable[i].split(" | ")[0] == InfoVariable[j].split(" | ")[0] and InfoVariable[i].split(" | ")[1] == InfoVariable[j].split(" | ")[1] and InfoVariable[i].split(" | ")[2] == InfoVariable[j].split(" | ")[2] and InfoVariable[i].split(" | ")[3] == InfoVariable[j].split(" | ")[3]:
                Temp.append(InfoVariable[j])
                ii = ii + 1
                if ii == len(InfoVariable): 
                    Files.append(Temp)
            else:
                if s == 1: 
                    Files.append(Temp)
                    s = 0
    FileLoad = list()
    for Item in Files:
        Indx = Item[0].split(" | ")
        NameFile = NameFile + Indx[4] + "--"
        with open(os.getcwd() + "/00-DownloadedData/" + NHANES_DATA[int(Indx[0])][int(Indx[1])][1][int(Indx[3])].split("/")[6], 'rb') as f:
            Colmns = xport.to_columns(f)
            DF = "pandas.DataFrame({"
            for SubItem in Item:
                SubIndx = SubItem.split(" | ")
                DF = DF + "'" + str(SubIndx[5]) + "':pandas.Series(" + str(Colmns[str(SubIndx[5])]) + "),"
            DF = DF[0:len(DF)-1]
            DF = DF + "})"
            FileLoad.append(DF)
    if default == "":
        default = "SDF"
    FileLoad[0] = FileLoad[0].replace("nan", "'NaN'")
    DFS = eval(FileLoad[0])
    for i in range(1, len(FileLoad)):
        FileLoad[i] = FileLoad[i].replace("nan", "'NaN'")
        DFS = pandas.merge(DFS, eval(FileLoad[i]), on='SEQN', how='outer').fillna(default)
    cont = 0
    if exportto == "Export to .XLSX":
        NameFile = NameFile[0:len(NameFile)] + str(0) + ".xlsx"
        while os.path.isfile(os.getcwd() + "/00-MergedData/" + NameFile):
            NameFile = NameFile[0:len(NameFile)-6] + str(cont) + ".xlsx"
            cont = cont + 1
        if cont > 9 or len(NameFile) > 180:
            NameFile = time.strftime("%H") + time.strftime("%M") + time.strftime("%S") + time.strftime("%I") + time.strftime("%M") + time.strftime("%S") + ".xlsx"
        DFS.to_excel(os.getcwd() + "/00-MergedData/" + NameFile)
    elif exportto == "Export to .CSV":
        NameFile = NameFile[0:len(NameFile)] + str(0) + ".csv"
        while os.path.isfile(os.getcwd() + "/00-MergedData/" + NameFile):
            NameFile = NameFile[0:len(NameFile)-5] + str(cont) + ".csv"
            cont = cont + 1
        if cont > 9 or len(NameFile) > 180:
            NameFile = time.strftime("%H") + time.strftime("%M") + time.strftime("%S") + time.strftime("%I") + time.strftime("%M") + time.strftime("%S") + ".csv"
        DFS.to_csv(os.getcwd() + "/00-MergedData/" + NameFile)
    elif exportto == "Export to .XPT":
        NameFile = NameFile[0:len(NameFile)] + str(0) + ".xpt"
        while os.path.isfile(os.getcwd() + "/00-MergedData/" + NameFile):
            NameFile = NameFile[0:len(NameFile)-5] + str(cont) + ".xpt"
            cont = cont + 1
        if cont > 9 or len(NameFile) > 180:
            NameFile = time.strftime("%H") + time.strftime("%M") + time.strftime("%S") + time.strftime("%I") + time.strftime("%M") + time.strftime("%S") + ".xpt"
        with open(os.getcwd() + "/00-MergedData/" + NameFile, 'wb') as File:
            xport.from_rows(DFS.to_dict('records'), File)
    messagebox.showinfo("INFORMATION", "Location of the file on your computer\n\n" + os.getcwd() + "/00-MergedData/" + NameFile) 
    return DFS

def DownloadFile(WebAddress, LocalAddress):
    if not os.path.isfile(os.getcwd() + "/00-DownloadedData/" + LocalAddress):
        if IsInternetUp():
            Discharged = urllib.request.urlopen(WebAddress).read()
            with open(os.getcwd() + "/00-DownloadedData/" + LocalAddress, 'wb') as File:
                File.write(Discharged) 
        else:
            messagebox.showinfo("INFORMATION", "Without Internet")
            
def IsInternetUp():
    try:
        urllib.request.urlopen('https://www.google.com/')
        return True
    except:
        return False
            
def Licencia():
    try:
        urllib.request.urlopen('https://www.instagram.com/jorge_m.a.l/')
        return True
    except:
        return False
    
def ItemsColors(self):
    i = 0
    for Item in self.List1.get(0, tk.END):
        if i % 2 == 0:
            self.List1.itemconfig(i, {'fg':'purple'})
        else:
            self.List1.itemconfig(i, {'fg':'green'})
        i = i + 1
    i = -1
    j = 0
    for Item in self.List2.get(0, tk.END):
        if len(Item.split(" | ")) == 3:
            i = i + 1
        else:
            if i % 2 == 0:
                self.List2.itemconfig(j, {'fg':'purple'})
            else:
                self.List2.itemconfig(j, {'fg':'green'})
        j = j + 1
    j = 0

def LoadVariables(self):
    GetListFiles = self.List1.get(0, tk.END)
    for ItemFile in GetListFiles:
        SpltFile = ItemFile.split(" | ")
        IntNHANES = list(self.Comb1["values"]).index(SpltFile[0])-1
        IntFile = list(self.Comb2["values"]).index(SpltFile[1])-1
        IndxFile = NHANES_DATA[IntNHANES][IntFile][0].index(SpltFile[2])
        Temp = NHANES_DATA[IntNHANES][IntFile][1][IndxFile]
        DownloadFile(Temp, Temp.split("/")[6])
        if not Temp.split("/")[6].split(".")[1] == "XPT":
            messagebox.showinfo("INFORMATION", "The file extension to load variables is not valid.\nFile: " + os.getcwd() + "/00-DownloadedData/" + Temp.split("/")[6])
        else:
            if (os.path.isfile(os.getcwd() + "/00-DownloadedData/" + Temp.split("/")[6])):
                self.List2.insert(END, ItemFile)
                for Variable in xport.Reader(open(os.getcwd() + "/00-DownloadedData/" + Temp.split("/")[6], 'rb')).fields:
                    self.List2.insert(END, str(IntNHANES) + " | " + str(IntFile) + " | " + str(0) + " | " + str(IndxFile) + " | " + ItemFile.split(" | ")[2] + " | " + Variable)
            else:
                messagebox.showinfo("INFORMATION", "The file '" + ItemFile + "' could not be downloaded.")
    ItemsColors(self)

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        Font1 = font.Font(family="Helvetica", size=9, weight="bold")
        main_window.title("SoftDataFusion - NHANES")
        main_window.resizable(0, 0)
        WidthWindow = 1210
        HeightWindow = 500
        BackgroundWindow = '#fff'
        BackgroundEvents = '#f4f8ff'

        self.MnBar = tk.Menu(self)

        self.Mn0 = tk.Menu(self.MnBar, bg=BackgroundWindow, tearoff=False)
        self.MnBar.add_cascade(label="Data selection options", underline=0, menu=self.Mn0)
        self.Add00 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/00Add.png")
        self.Mn0.add_command(label="Add file to the list to merge", underline=1, command=self.OppreButt1, image=self.Add00, compound=LEFT, accelerator="Ctrl+Q")
        self.Move00 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/00Move.png")
        self.Mn0.add_command(label="Remove file from list to merge", underline=1, command=self.OppreButt2, image=self.Move00, compound=LEFT, accelerator="Ctrl+W")
        self.Load00 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/00Load.png")
        self.Mn0.add_command(label="Load variables", underline=1, command=self.OppreButt8, image=self.Load00, compound=LEFT, accelerator="Ctrl+E")

        self.Mn1 = tk.Menu(self.MnBar, bg=BackgroundWindow, tearoff=False)
        self.MnBar.add_cascade(label="Variable selection options", underline=0, menu=self.Mn1)
        self.AddAll01 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/01AddAll.png")
        self.Mn1.add_command(label="Add all variables", underline=1, command=self.OppreButt9, image=self.AddAll01, compound=LEFT, accelerator="Ctrl+A")
        self.Add01 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/01Add.png")
        self.Mn1.add_command(label="Add variable", underline=1, command=self.OppreButt10, image=self.Add01, compound=LEFT, accelerator="Ctrl+S")
        self.Move01 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/01Move.png")
        self.Mn1.add_command(label="Move variable", underline=1, command=self.OppreButt11, image=self.Move01, compound=LEFT, accelerator="Ctrl+D")
        self.MoveAll01 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/01MoveAll.png")
        self.Mn1.add_command(label="Move all variable", underline=1, command=self.OppreButt12, image=self.MoveAll01, compound=LEFT, accelerator="Ctrl+F")
        self.ValCel01 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/01ValCel.png")
        self.Mn1.add_command(label="Value for cells with no match", underline=1, command=self.Copy, image=self.ValCel01, compound=LEFT, accelerator="Ctrl+C")

        self.Mn2 = tk.Menu(self.MnBar, bg=BackgroundWindow, tearoff=False)
        self.MnBar.add_cascade(label="File merge options", underline=0, menu=self.Mn2)
        self.Merg02 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/02Merg.png")
        self.Mn2.add_command(label="NEW MERGE", underline=1, command=self.OppreButt4, image=self.Merg02, compound=LEFT, accelerator="Ctrl+Z")
        self.NewM02 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/02NewM.png")
        self.Mn2.add_command(label="MERGE FILES", underline=1, command=self.OppreButt3, image=self.NewM02, compound=LEFT, accelerator="Ctrl+X")

        self.Mn3 = tk.Menu(self.MnBar, bg=BackgroundWindow, tearoff=0)
        self.MnBar.add_cascade(label="Help", menu=self.Mn3)
        self.Tuto03 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/03Tuto.png")
        self.Mn3.add_command(label="Tutorial", underline=1, command=self.Tutorial, image=self.Tuto03, compound=LEFT, accelerator="Ctrl+T")
        self.Abou03 = tk.PhotoImage(file=os.getcwd() + "/ImgSys/03Abou.png")
        self.Mn3.add_command(label="About", underline=1, command=self.About, image=self.Abou03, compound=LEFT, accelerator="Ctrl+Y")

        self.bind_all("<Control-q>", self.OppreButt1)
        self.bind_all("<Control-w>", self.OppreButt2)
        self.bind_all("<Control-e>", self.OppreButt8)
        self.bind_all("<Control-a>", self.OppreButt9)
        self.bind_all("<Control-s>", self.OppreButt10)
        self.bind_all("<Control-d>", self.OppreButt11)
        self.bind_all("<Control-f>", self.OppreButt12)
        self.bind_all("<Control-c>", self.Copy)
        self.bind_all("<Control-z>", self.OppreButt4)
        self.bind_all("<Control-x>", self.OppreButt3)
        self.bind_all("<Control-t>", self.Tutorial)
        self.bind_all("<Control-y>", self.About)

        try:
            self.master.config(menu=self.MnBar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.MnBar)

        f1 = 20
        f2 = 60
        f3 = 90
        f4 = 160

        self.Canv1 = Canvas(self, bg=BackgroundWindow, width=WidthWindow, height=HeightWindow, bd=0, highlightthickness=0)
        self.Canv1.pack()

        self.Labe1 = ttk.Label(self, background=BackgroundWindow, text="NHANES :", font=Font1)
        self.Labe1.place(x=20, y=f1 + 1)

        self.Comb1 = ttk.Combobox(self, state="readonly", width=14)
        self.Comb1.place(x=80, y=f1)
        self.Comb1["values"] = ["Select NHANES", 
            "1999 - 2000", 
            "2001 - 2002", 
            "2003 - 2004",
            "2005 - 2006",
            "2007 - 2008",
            "2009 - 2010",
            "2011 - 2012",
            "2013 - 2014",
            "2015 - 2016"]
        self.Comb1.current(0)
        self.Comb1.bind('<<ComboboxSelected>>', self.ChangeComb1)

        self.Labe2 = ttk.Label(self, background=BackgroundWindow, text="DATA :", font=Font1)
        self.Labe2.place(x=200, y=f1 + 1)

        self.Comb2 = ttk.Combobox(self, state="readonly", width=11)
        self.Comb2.place(x=244, y=f1)
        self.Comb2["values"] = ["Select DATA",
            "Demographics", 
            "Dietary", 
            "Examination", 
            "Laboratory", 
            "Questionnaire"]
        self.Comb2.current(0)
        self.Comb2.bind('<<ComboboxSelected>>', self.ChangeComb2)

        self.Labe3 = ttk.Label(self, background=BackgroundWindow, text="FILE :", font=Font1)
        self.Labe3.place(x=345, y=f1 + 1)

        self.Comb3 = ttk.Combobox(self, state="readonly", width=130)
        self.Comb3.place(x=381, y=f1)
        self.Comb3["values"] = ["Select FILE"]
        self.Comb3.current(0)

        self.List1 = tk.Listbox(self, bg=BackgroundEvents, width=133, height=5, foreground="green")
        self.List1.place(x=381, y=f2-10)

        self.Canv2 = Canvas(self, bg=BackgroundWindow, width=287, height=80)
        self.Canv2.place(x=50, y=f2)

        self.Butt1 = ttk.Button(self, width=40, text="Add file to the list to merge")
        self.Butt1.place(x=70, y=f2 + 14)
        self.Butt1["command"] = self.OppreButt1

        self.Butt2 = ttk.Button(self, width=40, text="Remove file from list to merge")
        self.Butt2.place(x=70, y=f3 + 14)
        self.Butt2["command"] = self.OppreButt2

        self.Canv3 = Canvas(self, bg=BackgroundWindow, width=WidthWindow-25, height=HeightWindow-193)
        self.Canv3.place(x=10, y=f4)    

        self.Canv4 = Canvas(self, bg=BackgroundWindow, width=160, height=155)
        self.Canv4.place(x=WidthWindow-208, y=f4-20)

        self.Canv41 = Canvas(self, bg=BackgroundWindow, width=143, height=85)
        self.Canv41.place(x=WidthWindow-200, y=f4 + 35)

        self.Comb4 = ttk.Combobox(self, state="readonly", width=17)
        self.Comb4.place(x=WidthWindow-188, y=f4 + 50)
        self.Comb4["values"] = ["Select - Export to...",
            "Export to .CSV", 
            "Export to .XPT", 
            "Export to .XLSX"]
        self.Comb4.current(0)

        self.Butt3 = ttk.Button(self, width=20, text="MERGE FILES")
        self.Butt3.place(x=WidthWindow-191, y=f4 + 85)
        self.Butt3["command"] = self.OppreButt3

        self.Butt4 = ttk.Button(self, width=20, text="NEW MERGE")
        self.Butt4.place(x=WidthWindow-191, y=f4 - 5)
        self.Butt4["command"] = self.OppreButt4

        self.Canv6 = Canvas(self, bg=BackgroundWindow, width=160, height=50)
        self.Canv6.place(x=417, y=f4-20)

        self.Butt8 = ttk.Button(self, width=20, text="Load variables")
        self.Butt8.place(x=434, y=f4 - 5)
        self.Butt8["command"] = self.OppreButt8

        self.Canv7 = Canvas(self, bg=BackgroundWindow, width=160, height=207)
        self.Canv7.place(x=417, y=f4 + 75)

        self.Butt9 = ttk.Button(self, width=20, text="Add all variables       ->")
        self.Butt9.place(x=434, y=f4 + 90)
        self.Butt9["command"] = self.OppreButt9

        self.Butt10 = ttk.Button(self, width=20, text="Add variable             ->")
        self.Butt10.place(x=434, y=f4 + 130)
        self.Butt10["command"] = self.OppreButt10

        self.Butt11 = ttk.Button(self, width=20, text="<-           Move variable")
        self.Butt11.place(x=434, y=f4 + 170)
        self.Butt11["command"] = self.OppreButt11

        self.Butt12 = ttk.Button(self, width=20, text="<-    Move all variables")
        self.Butt12.place(x=434, y=f4 + 210)
        self.Butt12["command"] = self.OppreButt12

        self.Entry1 = Entry(self, bg=BackgroundEvents, width=10)
        self.Entry1.place(x=470, y=f4 + 250)
        CreateToolTip(self.Entry1, "Value for cells with no match")

        self.Labe3 = ttk.Label(self, background=BackgroundWindow, text="WHAT VARIABLES OF THE FILES TO MERGE", font=Font1)
        self.Labe3.place(x=25, y=f4 + 5)

        self.Labe4 = ttk.Label(self, background=BackgroundWindow, text="VARIABLES TO SELECT", font=Font1)
        self.Labe4.place(x=130, y=f4 + 35)

        self.Labe5 = ttk.Label(self, background=BackgroundWindow, text="SELECTED VARIABLES", font=Font1)
        self.Labe5.place(x=723, y=f4 + 35)

        self.List2 = tk.Listbox(self, bg=BackgroundEvents, width=60, height=15)
        self.List2["fg"] = ["blue"]
        self.List2.place(x=28, y=f4 + 55)

        self.List3 = tk.Listbox(self, bg=BackgroundEvents, width=60, height=15)
        self.List3["fg"] = ["maroon2"]
        self.List3.place(x=605, y=f4 + 55)

        self.Canv5 = Canvas(self, bg=BackgroundWindow, width=197, height=173)
        self.Canv5.place(x=WidthWindow-229, y=f4 + 150)

        self.LoImg = tk.PhotoImage(file=os.getcwd() + "\ImgSys\Icono.png")

        self.JButton111 = tk.Button(self)
        self.JButton111["image"] = self.LoImg
        self.JButton111["bg"] = "white"
        self.JButton111["border"] = "0"
        self.JButton111["command"] = self.About
        self.JButton111.pack(side="top")
        self.JButton111.place(x=WidthWindow-203, y=f4 + 163)

        self.ImgAct = 1

        self.Fondo = tk.PhotoImage(file=os.getcwd() + "/ImgSys/0401.png")
        self.JButton000 = tk.Button(self, bg="white", border=0, command=self.About, image=self.Fondo)
        self.JButton000.pack(side="top")

        self.Back = tk.PhotoImage(file=os.getcwd() + "/ImgSys/05001.png")
        self.JButton111 = tk.Button(self, bg="white", border=0, command=self.BackTutorial, image=self.Back)
        self.JButton111.pack(side="top")

        self.Next = tk.PhotoImage(file=os.getcwd() + "/ImgSys/05002.png")
        self.JButton222 = tk.Button(self, bg="white", border=0, command=self.NextTutorial, image=self.Next)
        self.JButton222.pack(side="top")

        self.CloseT = tk.PhotoImage(file=os.getcwd() + "/ImgSys/05003.png")
        self.JButton333 = tk.Button(self, bg="white", border=0, command=self.CloseTutorial, image=self.CloseT)
        self.JButton333.pack(side="top")

        main_window.configure(width=WidthWindow, height=HeightWindow)
        self.place(width=WidthWindow, height=HeightWindow)

    def Tutorial(self, * event):
        WidthWindow = 1210
        HeightWindow = 500
        self.JButton000.place(x=-1, y=-1)
        self.JButton111.place(x=2, y=(HeightWindow / 2)-20)
        self.JButton222.place(x=WidthWindow-22, y=(HeightWindow / 2)-20)
        self.JButton333.place(x=WidthWindow-22, y=1)
    
    def CloseTutorial(self, * event):
        if self.JButton000.winfo_ismapped():
            self.NextImg = tk.PhotoImage(file=os.getcwd() + "/ImgSys/0401.png")
            self.JButton000["image"] = self.NextImg
            self.JButton000.place_forget()
            self.JButton111.place_forget()
            self.JButton222.place_forget()
            self.JButton333.place_forget()
            self.ImgAct = 1
         
    def NextTutorial(self, * event):
        self.ImgAct = self.ImgAct + 1
        if self.ImgAct == 20:
            self.ImgAct = 19
        else:
            self.NextImg = tk.PhotoImage(file=os.getcwd() + "/ImgSys/040" + str(self.ImgAct) + ".png")
            self.JButton000["image"] = self.NextImg
         
    def BackTutorial(self, * event):
        self.ImgAct = self.ImgAct - 1
        if self.ImgAct <= 0:
            self.ImgAct = 1
        else:
            self.NextImg = tk.PhotoImage(file=os.getcwd() + "/ImgSys/040" + str(self.ImgAct) + ".png")
            self.JButton000["image"] = self.NextImg
        
    def About(self, * event):
        BackgroundWindow = '#fff'
        nw = tk.Toplevel(self, bg=BackgroundWindow)
        nw.title("About")
        nw.geometry('500x400+400+150')
        nw.configure(bg=BackgroundWindow)
        self.Canv00 = Canvas(nw, bg=BackgroundWindow, width=197, height=173)
        self.Canv00.place(x=150, y=10)
        self.LoImg00 = tk.PhotoImage(file=os.getcwd() + "/ImgSys\Icono.png")
        self.JButton00 = tk.Button(nw)
        self.JButton00["image"] = self.LoImg00
        self.JButton00["bg"] = "white"
        self.JButton00["border"] = "0"
        self.JButton00.pack(side="top")
        self.JButton00.place(x=176, y=20)
        self.Canv01 = Canvas(nw, bg=BackgroundWindow, width=500, height=173)
        self.Canv01.place(x=-1, y=205)
        Font1 = font.Font(family="Helvetica", size=9, weight="bold")
        self.Labe000 = ttk.Label(nw, background=BackgroundWindow, text="Interactive software for the automatic integration of medical databases published by", font=Font1)
        self.Labe000.place(x=10, y=230)
        self.Labe001 = ttk.Label(nw, background=BackgroundWindow, text="NHANES for particular research processes in the health area, SoftDataFusion resea-", font=Font1)
        self.Labe001.place(x=10, y=250)
        self.Labe002 = ttk.Label(nw, background=BackgroundWindow, text="rch tool.", font=Font1)
        self.Labe002.place(x=10, y=270)
        self.Labe003 = ttk.Label(nw, background=BackgroundWindow, text="Developed by", font=Font1)
        self.Labe003.place(x=10, y=305)
        self.Labe004 = ttk.Label(nw, background=BackgroundWindow, text="Jorge M. Anaya Leon", font=Font1)
        self.Labe004.place(x=20, y=330)
        self.Labe005 = ttk.Label(nw, background=BackgroundWindow, text="Jorgeleon132@gmail.com", font=Font1)
        self.Labe005.place(x=20, y=350)
        self.Canv0112 = Canvas(nw, bg=BackgroundWindow, width=285, height=70)
        self.Canv0112.place(x=190, y=290)
        self.Labe006 = ttk.Label(nw, background=BackgroundWindow, text="Send your email to the contact to subscribe", font=Font1)
        self.Labe006.place(x=210, y=305)
        self.Labe007 = ttk.Label(nw, background=BackgroundWindow, text="to system news or visit the website", font=Font1)
        self.Labe007.place(x=210, y=325)
        self.link = Linkbutton(nw, text="here...", command=self.link_clicked)
        self.link.place(x=420, y=325)
        nw.focus_set()
        nw.grab_set()
    
    def link_clicked(self):
        import webbrowser
        webbrowser.open("http://softdatafusion.sistemasadministrativosdecolombia.com/")

    def ChangeComb1(self, event):
        self.Comb2.current(0)
        self.Comb3["values"] = ["Select FILE"]
        if self.Comb1.current()-1 == -1:
            messagebox.showinfo("INFORMATION", "You must select an NHANES.")
            self.Comb1.focus_set()
            
    def ChangeComb2(self, event):
        self.Comb3.current(0)
        Comb1Item = self.Comb1.current()-1
        Comb2Item = self.Comb2.current()-1
        if Comb1Item > -1:
            if  Comb2Item > -1:
                self.Comb3["values"] = ["Select FILE"] + NHANES_DATA[Comb1Item][Comb2Item][0]
            else:
                messagebox.showinfo("INFORMATION", "You must select an Data.")
                self.Comb2.focus_set()
        else:
            messagebox.showinfo("INFORMATION", "You must select an NHANES.")
            self.Comb1.focus_set()
    
    def OppreButt1(self, * event):
        if self.Comb3.current()-1 > -1:
            self.List1.insert(END, str(self.Comb1.get()) + " | " + str(self.Comb2.get()) + " | " + self.Comb3.get())
        else:
            messagebox.showinfo("INFORMATION", "You must select an FILE.")
            self.Comb3.focus_set()
        ItemsColors(self)
    
    def OppreButt2(self, * event):
        List1Size = self.List1.size()
        if List1Size > 0:
            List1Item = self.List1.curselection()
            if List1Item == ():
                messagebox.showinfo("INFORMATION", "You must select an FILE from the list.")
            else:
                self.List1.delete(List1Item)                
                ItemsColors(self)
        else:
            messagebox.showinfo("INFORMATION", "There are no FILES in the list.")
    
    def OppreButt3(self, * event):
        if self.List3.size() > 0:
            if self.Comb4.current()-1 == -1:
                messagebox.showinfo("INFORMATION", "You must select an Select - Export to...")
                self.Comb4.focus_set()
            else:
                if not Licencia():
                    self.About(self)
                    messagebox.showinfo("INFORMATION", "Without Internet or expired license. Contact by email with the SoftData Fusion provider for more information.")
                else:
                    urllib.request.urlopen('http://softdatafusion.sistemasadministrativosdecolombia.com/Hacer.php?q=;29')
                    messagebox.showinfo("INFORMATION", "Start MERGER...")
                    FuseData(self, sorted(self.List3.get(0, tk.END)), self.Entry1.get(), str(self.Comb4.get()))
                    messagebox.showinfo("INFORMATION", "Files MERGED successfully.")
        else:
            messagebox.showinfo("INFORMATION", "There are no SELECTED VARIABLES in the list.")
                
    def OppreButt4(self, * event):
        f4 = 160
        self.Comb1.current(0)
        self.Comb2.current(0)
        self.Comb3["values"] = ["Select FILE"]
        self.Comb3.current(0)
        self.Comb4.current(0)
        self.List1.delete(0, END)
        self.List2.delete(0, END)
        self.List3.delete(0, END)
        self.Entry1.delete(0, 'end')
        
    def OppreButt8(self, * event):
        self.List2.delete(0, END)
        self.List3.delete(0, END)
        if self.List1.size() > 0:
            messagebox.showinfo("INFORMATION", "Start load of VARIABLES...")
            LoadVariables(self)
            messagebox.showinfo("INFORMATION", "End of loading of VARIABLES.")
        else:
            messagebox.showinfo("INFORMATION", "There are no FILES in the list.")
    
    def OppreButt9(self, * event):
        self.List3.delete(0, END)
        if self.List2.size() > 0:
            for Item in self.List2.get(0, tk.END):
                if len(Item.split(" | ")) > 4:
                    self.List3.insert(END, Item)
            ItemsColors(self)
        else:
            messagebox.showinfo("INFORMATION", "There are no VARIABLES TO SELECT in the list.")
        
    def OppreButt10(self, * event):
        List1Size = self.List2.size()
        if List1Size > 0:
            List2Item = self.List2.curselection()
            if List2Item == ():
                messagebox.showinfo("INFORMATION", "You must select an VARIABLE TO SELECT from the list.")
            else:
                GetList2Item = self.List2.get(List2Item, List2Item)[0]
                if len(GetList2Item.split(" | ")) > 4:
                    self.List3.insert(END, GetList2Item)
                    ItemsColors(self)
                else:
                    messagebox.showinfo("INFORMATION", "You must select an VARIABLE TO SELECT from the list, except files.")
        else:
            messagebox.showinfo("INFORMATION", "There are no VARIABLES TO SELECT in the list.")
            
    def OppreButt11(self, * event):
        List1Size = self.List3.size()
        if List1Size > 0:
            List1Item = self.List3.curselection()
            if List1Item == ():
                messagebox.showinfo("INFORMATION", "You must select an SELECTED VARIABLES from the list.")
            else:
                self.List3.delete(List1Item)                
                ItemsColors(self)
        else:
            messagebox.showinfo("INFORMATION", "There are no SELECTED VARIABLES in the list.")
            
    def OppreButt12(self, * event):
        if self.List3.size() > 0:
            self.List3.delete(0, END)
        else:
            messagebox.showinfo("INFORMATION", "There are no SELECTED VARIABLES in the list.")
    
    def Copy(self, * event):
        self.Entry1.focus_set()
    
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     
        self.wraplength = 180   
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left', background="#ffffff", relief='solid', borderwidth=1, wraplength=self.wraplength)        
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
            
class Linkbutton(ttk.Button):
    
    def __init__(self, * args, ** kwargs):
        super().__init__(*args, ** kwargs)
        
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = Font(family=label_font, size=9)
        
        style = ttk.Style()
        style.configure("Link.TLabel", background="#ffffff", foreground="#357fde", font=self.font)
        
        self.configure(style="Link.TLabel", cursor="hand2")
        
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)
    
    def on_mouse_enter(self, event):
        self.font.configure(underline=True)
    
    def on_mouse_leave(self, event):
        self.font.configure(underline=False)
            
if __name__ == "__main__":
    main_window  = tk.Tk()
    main_window.geometry('+50+50')
    app = Application(main_window)
    app.mainloop()
    try:
        main_window.destroy()
    except:
        print("Closing.../Close")