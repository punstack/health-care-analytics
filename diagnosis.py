import re
import pandas as pd

def mapped_diagnosis(df_column):
    diagnosis_mapping = {
        r'\bMULTITRAUMA\b|\bPOLYT[R]?AUMA\b|\bMULTIPLE[ ]TRAUMA[S]?\b': 'Trauma/Injury',
        r'\bSTAB\b|\bSTABBI[NM]G\b': 'Trauma/Injury',
        r'\bM[P]?OTOR\b|\bMOTORCYCLE\b|\bMOTORVEHICLE\b|\bVEHICLE\b|\bBICYCLE\b|\bBIKE\b|\bSTRUCK\b|\bBICYCLE/CAR\b|\bATV\b|\bPEDESTRIAN\b|\bCAR\b|\bMVA\b': 'Trauma/Injury',
        r'\bFRACTURE[S]?\b|\bFRACUTRE\b|\bFRACTURED\b|\bF[R]?X[S]?\b|\bINJURY\b': 'Trauma/Injury',
        r'\bT[R]?[AE]?UM[A]?\b|\bWOU[MN]D\b|\bLACERATION\b': 'Trauma/Injury',
        r'\bS/PFALL[S]?|\bFAL[L]?[S]?\b|\bDISLOCATION\b': 'Trauma/Injury',
        r'\bGUN\b|\bGUN[ ]?SHOT\b|\bGSW\b': 'Trauma/Injury',
        r'\b0681\b': 'Trauma/Injury',
        r'\bTEAR\b': 'Trauma/Injury',
        r'\bHEMATOMA\b': 'Trauma/Injury',
        r'\bHEMOTHORAX\b': 'Trauma/Injury',
        r'\bASSAULT\b': 'Trauma/Injury',
        r'\bFEMUR[ ]NON[ ]UNION\b': 'Trauma/Injury',
        r'\bTIB;FIB\b': 'Trauma/Injury',
        r'\bINJURY\b|\bINJURIES\b': 'Trauma/Injury',
        r'\bBITE[S]?\b': 'Trauma/Injury',
        r'\bKICKED[ ]BY[ ]HORSE\b': 'Trauma/Injury',

        r'\bNECROTIZING\b|\bNECROTISING\b|\bNECTROTIZING\b|\bNECROTZING\b|\bNECROSIS\b': 'Infections',
        r'\bSEP[S]?I[S]?S\b|\bSEPISI\b|\bSEPTIC\b': 'Infections',
        r'\bENTEROCOCCUS\b': 'Infections',
        r'\bSHINGLES\b': 'Infections',
        r'\bFASCIETIS\b|\bFASCITITIS\b|\bFASCITIS\b|\bFASCEITIS\b|\bFASCIITIS\b|\bFASCILITIS\b|\bFASCIATIS\b': 'Infections',
        r'\bDISCITIS\b': 'Infections',
        r'\bPYLEONEPHRITIS\b|\bPYELONEPHRITIS\b|\bPYLONEPHRITIS\b|\bUTI\b': 'Infections',
        r'\bVRE\b': 'Infections',
        r'\bFLU\b|\bINFLUENZA\b': 'Infections',
        r'\bOSTEOMYLITIS\b|\bOSTEMOYELITIS\b': 'Infections',
        r'\bC[-]?DIFF\b|\bC[.]?[ ]DIF[F]?\b': 'Infections',
        r'\bLEUKOCYTOSIS\b': 'Infections',
        r'\bMENI[N]?GITIS\b': 'Infections',
        r'\bHIV\b': 'Infections',
        r'\bMONO\b|\bMONONUCLEOSIS\b|\bEBV\b': 'Infections',
        r'\bNEURO[ ]?SYPHIL[L]?IS\b': 'Infections',
        r'\bHEPATITIS\b': 'Infections',
        r'\bURINARY\b': 'Infections',
        r'\bUROSEPSIS\b|\bUROSPEPSIS\b|\bPNEUMOSEPSIS\b': 'Infections',
        r'\bCELL[IU]LITIS\b|\bCELL[IU]LTIIS\b': 'Infections',
        r'\bINFECTI[O]?N\b|\bINFECTED\b': 'Infections',
        r'\bBACT[E]?REMIA\b': 'Infections',
        r'\bMENINGITIS\b|\bMENINGITITIS\b': 'Infections',
        r'\bAB[S]?CESS\b': 'Infections',
        r'\bPERITONITIS\b': 'Infections',
        r'\bOSTEOMYELITIS\b|\bMYELITIS\b': 'Infections',
        r'\bASPERGILOMA\b': 'Infections',
        r'\bMETHICILLIN RESISTANT STAPH AUREUS\b|\bMRSA\b': 'Infections',
        r'\bSYPHILIS\b': 'Infections',
        r'\bSTAPH\b': 'Infections',

        r'\bHODGKIN\'S\b|\bNON[-]?HODGKIN\'S\b|\bHODGKINS\b|\bNONHODGKINS\b': 'Cancer',
        r'\bHEPATOMA\b': 'Cancer',
        r'\bL[E]?UKEMIA\b': 'Cancer',
        r'\bMYELOMA\b': 'Cancer',
        r'\bSA[R]?COMA\b': 'Cancer',
        r'\bCHEMO\b|\bCHEMOTHERAPY\b|\bCANCER\b|\bCNACER\b|\bTUMOR\b': 'Cancer',
        r'\bALLO TX\b': 'Cancer',
        r'\bTHYMOMA\b': 'Cancer',
        r'\bAML\b': 'Cancer',
        r'\bGBM\b': 'Cancer',
        r'\bTYPHLITIS\b': 'Cancer',
        r'\bTURBT\b': 'Cancer',
        r'\bCA\b|\bCA/SDA\b': 'Cancer',
        r'\bMETASTATIC\b|\bMALIGNANT\b': 'Cancer',
        r'\bMELANOMA\b': 'Cancer',
        r'\bGLIOB[L]?ASTOMA\b': 'Cancer',
        r'\bL[UY][MN]PHOMA\b': 'Cancer',
        r'\bMENIGIOMA\b': 'Cancer',
        r'\bCARCINOMA\b|ADENOCARCINOMA': 'Cancer',
        r'\bMYELOFIBROSIS\b': 'Cancer',
        r'\bCMML\b': 'Cancer',
        r'\bCARCINOMATOSIS\b': 'Cancer',
        r'\bMETASTISIS\b|\bMETASTASIS\b': 'Cancer',
        r'\bCHOLANGIOCARCINOMA\b|\bCHOLANGIOLIOLITIS\b': 'Cancer', 

        r'\bARF\b|\bGIB\b': 'Renal Issues',
        r'\bCRF\b': 'Renal Issues',
        r'\bCONN\'S\b': 'Renal Issues',
        r'\bREN[A]?L\b': 'Renal Issues',
        r'\bKIDNEY\b': 'Renal Issues',
        r'\bHYDRONEPHROSIS\b': 'Renal Issues',
        r'\bDIALYSIS\b': 'Renal Issues',

        r'\bHIBILIRUBIN\b|\bHYPERBILIRUBEN\b|\bHYPERBILRUBINEIMA\b|\bHYPERVILIRUBINEMIA\b|\bBILIRUBINEMIA\b|\bBILIRUBEN\b': 'Liver Issues',
        r'\bINSULIN[ ]DENSENTIZATION\b': 'Liver Issues',
        r'\bACSITES\b|\bASCIT[IE]S\b|\bASCITIES\b': 'Liver Issues',
        r'\bTRANSAMINITIS\b': 'Liver Issues',
        r'\bL[L]?IVE[R]?\b': 'Liver Issues',
        r'\bHEPATIC\b': 'Liver Issues',
        r'\bCIRRHOSIS\b': 'Liver Issues',
        r'\bJAUNDICE\b': 'Liver Issues',

        r'\bPREGNANCY\b|\bLABOR\b|\bC[ ]?SECTION\b': 'Neonatal Care',
        r'\bFAILURE[ ]TO[ ]THIRVE\b|\bFAILURE[ ]TO[ ]THRIVE\b|\bFTT\b': 'Neonatal Care',
        r'\bPREMATURE\b|\bPRE[-]?MATURITY\b': 'Neonatal Care',
        r'\bDUSKY SPELLS\b': 'Neonatal Care',
        r'\bNEWBORN\b': 'Neonatal Care',
        r'\bFETAL\b': 'Neonatal Care',
        r'\bWK[S]?\b|\bWEEK[S]?\b|\bCONTRACTIONS\b': 'Neonatal Care',

        r'\bATRAIL\b|\bATRIAL\b': 'Cardiovascular Issues',
        r'\bCHORDAE\b': 'Cardiovascular Issues',
        r'\bSVT\b|\bSVC\b|\bICD\b': 'Cardiovascular Issues',
        r'\b\+MIBI\b': 'Cardiovascular Issues',
        r'\bFORAMEN OVALE\b|\bPFO\b': 'Cardiovascular Issues',
        r'\bCABG[E]?\b': 'Cardiovascular Issues',
        r'\bV-?TACH\b|\bVT\b|\bVT/VF\b': 'Cardiovascular Issues',
        r'\bMVR\b': 'Cardiovascular Issues',
        r'\bMYO[I]?CARDIAL\b|\bM.?I.?\b': 'Cardiovascular Issues',
        r'\bARREST\b|\bPOST[-]?ARREST\b': 'Cardiovascular Issues',
        r'\bVENTRICULAR[ ]FIBRILLATION\b|\bV[-]?FIB\b': 'Cardiovascular Issues',
        r'\bBIGEMINY\b': 'Cardiovascular Issues',
        r'\bBRADYARRHYTHMIA\b|\bBRAD[Y]?CARDIA\b': 'Cardiovascular Issues',
        r'\bEKG\b': 'Cardiovascular Issues',
        r'\bTVR\b': 'Cardiovascular Issues',
        r'\bPER[I]?CARDITIS\b': 'Cardiovascular Issues',
        r'\bC[A]?ORO[NM]A[R]?Y\b': 'Cardiovascular Issues',
        r'\bTORSADE\b': 'Cardiovascular Issues',
        r'\bPALP[AI]TATIONS\b': 'Cardiovascular Issues',
        r'\bVENTRICULAR\b': 'Cardiovascular Issues',
        r'\bBENTAL[L]?\b': 'Cardiovascular Issues',
        r'\bAF[R]?IBULATION\b|\bA[ -]? FIB\b|\bA[-]?FIB\b': 'Cardiovascular Issues',
        r'\bA[-,]FLUTTER\b': 'Cardiovascular Issues',
        r'\bTAC[HK]YCARDIA\b': 'Cardiovascular Issues',
        r'\bLEAD\b': 'Cardiovascular Issues',
        r'\bCONGESTIVE HEART DISEASE\b': 'Cardiovascular Issues',
        r'\bSTRESS TEST\b': 'Cardiovascular Issues',
        r'\bANGI[N]?A\b': 'Cardiovascular Issues',
        r'\bM[EI]T[R]?[I]?AL\b|\bMITRO\b': 'Cardiovascular Issues',
        r'\bTACHY\b|\bTACHYCARDIA\b': 'Cardiovascular Issues',
        r'\bH[E]?ART\b|\bCARDIAC\b|\bCARDIOGENIC\b|\bCARDIOMYOPATHY\b|\bPACEMAKER\b': 'Cardiovascular Issues',
        r'\bELEVATED[ ]TROPONIN\b': 'Cardiovascular Issues',
        r'\bDEFIBRILLATOR\b': 'Cardiovascular Issues',
        r'\bARRYTHMIA\b': 'Cardiovascular Issues',
        r'\bTRICUSPID\b': 'Cardiovascular Issues',
        r'\bMR\\\\\b|\bMR\\\b|\bMR\b|\bMR\\MITRAL\b': 'Cardiovascular Issues',
        r'\bREGURGITATION\b': 'Cardiovascular Issues',
        r'\bSYNCOPE\b': 'Cardiovascular Issues',
        r'\bCAROTID\b': 'Cardiovascular Issues',
        r'\bAORTIC\b': 'Cardiovascular Issues',
        r'\b[N]?STEMI\b': 'Cardiovascular Issues',
        r'\bPERICARDIAL\b': 'Cardiovascular Issues',
        r'\bENDOCARDITIS\b': 'Cardiovascular Issues',
        r'\bCHF\b|\bCAD\b': 'Cardiovascular Issues',
        r'\bM[.]?I[.]?\b': 'Cardiovascular Issues',
        r'\bAICD FIRING\b': 'Cardiovascular Issues',
        r'\bTAMPON[AE]DE\b': 'Cardiovascular Issues',
        r'\bV[-]?TACH\b': 'Cardiovascular Issues',
        r'\bASD\b': 'Cardiovascular Issues',
        r'\bRECANALIZATION\b': 'Cardiovascular Issues',
        r'\bCAVERNOUS\b': 'Cardiovascular Issues',
        r'\bAVR\b|\bBRADY\b|\bCARDIA\b|\bBRADYCARDIA\b': 'Cardiovascular Issues',

        r'\bP[MN]E[U]?MO[NM]IA\b|\bPNEUMNOIA\b|\bPNAUMONIA\b|\bPNA\b|\bPNEUMONI\b': 'Respiratory Issues',
        r'\bINFILTRATE[S]?\b': 'Respiratory Issues',
        r'\bCHOKE\b|\bCHOKING\b': 'Respiratory Issues',
        r'\bCOUGH\b': 'Respiratory Issues',
        r'\bASPIRATION\b': 'Respiratory Issues',
        r'\b[R]?[AE]SP[.]?\b|\bRE[S]?PIRATO[RT]Y\b|\bRESPITORY\b': 'Respiratory Issues',
        r'\bTHROAT\b|\bVOCAL\b': 'Respiratory Issues',
        r'\bLARYNGOSPASM\b': 'Respiratory Issues',
        r'\bTRACHEOMALACIA\b|\bTRACHEOSTOMY\b|\bTRACHEOBRONCHOPLASTY\b': 'Respiratory Issues',
        r'\bLOBE[ ]COLLAPSE\b': 'Respiratory Issues',
        r'\bPULMO[M]?[NM]ARY\b|\bPE\b': 'Respiratory Issues',
        r'\bCOPD\b': 'Respiratory Issues',
        r'\bPE\b|\bPULM\b|\bPNEUMOPERTONEUM\b': 'Respiratory Issues',
        r'\bLUNG\b': 'Respiratory Issues',
        r'\bDIAPHRA[G]?MATIC\b': 'Respiratory Issues',
        r'\bCHYLOTHORAX\b': 'Respiratory Issues',
        r'\bARDS\b': 'Respiratory Issues',
        r'\bSHORTNESS[ ]OF[R]?[ ]BREATH\b|\bSOB\b': 'Respiratory Issues',
        r'\bTRACHEOBROCHOMALACIA\b|\bTRACHEO-BRONCHEO\b|\bTRACHEOBRONCHIO\b|\bTRACHEO[-]?BRONCHEAL\b|\bTRACHEOBRONCHOMALACIA\b|\bTRACHEOBRONCOMALICIA\b': 'Respiratory Issues',
        r'\bH[EY]MOP[T]?YSIS\b|\bHEMPOTYSIS\b': 'Respiratory Issues',
        r'\bTACHYPNEA\b': 'Respiratory Issues',
        r'\bHEMIPTHSIS\b': 'Respiratory Issues',
        r'\bTRACH\b|\bTRACHEA\b|\bTRACIAL\b|\bTRACHEOSTOMY\b|\bTRA[N]?CHEAL\b|\bTRACHAEL\b|\bTRACHEO\b': 'Respiratory Issues',
        r'\bEMPHSYEMA\b|\bEMPYEMA\b': 'Respiratory Issues',
        r'\bFIBROTHORAX\b': 'Respiratory Issues',
        r'\bMESOTHELIOMA\b': 'Respiratory Issues',
        r'\bCAVITARY\b': 'Respiratory Issues',
        r'\bASTH[M]?A\b|\bASTHMATICUS\b|\bASTH[A]?MA\b': 'Respiratory Issues',
        r'\bDYSPN[IE]A\b|\bDYPSNEA\b': 'Respiratory Issues',
        r'\bHYPOXIA\b': 'Respiratory Issues',
        r'\bCHEST\b': 'Respiratory Issues',
        r'\bCOPD\b|\bCHRONIC OBST PULM DISEASE\b': 'Respiratory Issues',
        r'\bBRADYCARDIA\b': 'Respiratory Issues',
        r'\bPL[E]?URAL\b': 'Respiratory Issues',
        r'\bAIRWAY\b': 'Respiratory Issues',
        r'\b\+ETT.?\\?CATH\b': 'Respiratory Issues',
        r'\bPNEUMOTHORAX\b': 'Respiratory Issues',
        r'\bSTRIDOR\b': 'Respiratory Issues',
        r'\bBRONCHIAL\b|\bBRONCHIATISIS\b|\bBRONCHIOLE[S]?\b|\bBRONCHITIS\b|\bBRACHEAL\b': 'Respiratory Issues',
        r'\bTB\b': 'Respiratory Issues',
        r'\bBOERHAAVE\b': 'Respiratory Issues',
        r'\bRESPIRATOR\b|\bVENTILLATOR\b|\bVENT\b': 'Respiratory Issues',

        r'\bACHALASIA\b': 'Gastrointestinal Issues',
        r'\bMIR[R]?IZ[Z]?I\b': 'Gastrointestinal Issues',
        r'\bFOOD\b': 'Gastrointestinal Issues',
        r'\bVENTRAL[ ]HERNIA\b': 'Gastrointestinal Issues',
        r'\bENTERIC[ ]FISTULA\b|\bENTEROCUTANEUS[ ]FISTULA\b|\bENTERO[ ]?CUTA[N]?EOUS\b|\bINTRACUTANEOUS[ ]FISTULA\b': 'Gastrointestinal Issues',
        r'\bCECUM\b': 'Gastrointestinal Issues', 
        r'\bABDMOMINAL\b|\bABDOMEN\b|\bABDOMAL\b|\bABD[.]?\b|\bAB[D]?OMINAL\b|\bADBOMINAL\b': 'Gastrointestinal Issues',
        r'\bSUPRA[ ]?GLOTTITIS\b|\bEPIGLOT[T]?ITIS\b|\bSUPERGLOTTITIS\b': 'Gastrointestinal Issues',
        r'\bSPLEEN\b|\bSPLENOMEGALIA\b|\bSPLE[E]?NECTOMY\b|\bSPLENOMEGALY\b|\bSPLENIC\b': 'Gastrointestinal Issues',
        r'\bPANCREAS\b|\bPA[NR]CREATIC\b|\bPAN[C]?R[E]?ATITIS\b': 'Gastrointestinal Issues',
        r'\bBIL[L]?IARY\b|\bBILE\b': 'Gastrointestinal Issues',
        r'\bBARRETT\'S\b': 'Gastrointestinal Issues',
        r'\bCOLON\b|\bCOLON[G]?IC\b': 'Gastrointestinal Issues',
        r'\bINSULINOMA\b': 'Gastrointestinal Issues',
        r'\bOSTOMY\b': 'Gastrointestinal Issues',
        r'\bCHRON\'S\b|\bCROHN\'S\b|\bCHRONS\b|\bCROHNS\b': 'Gastrointestinal Issues',
        r'\bSWALLOWED\b|\bINGESTED\b|\bINGE[G]?STION\b': 'Gastrointestinal Issues',
        r'\bDYSPHAGIA\b': 'Gastrointestinal Issues',
        r'\bGASTRIC\b|\bGASTRO\b|\bGASTROINTES[T]?INAL\b|\bGASTROINSTESTINAL\b|\bG I\b|\bG.I.\b': 'Gastrointestinal Issues',
        r'\bES[O]?PHAGUS\b|\bESOPHAGEAL\b|\bEPIGLOTTIS\b|\bEPIGLOTTAL\b|\bDIVERTICULAR\b|\bDIVERTICULITIS\b': 'Gastrointestinal Issues',
        r'\bCHOLECYSITIS\b|\bCHOLELITHIASIS\b|\bCHOLENGITIS\b|\bCHOELITHIASIS\b|\bCHOLYCYSTITIS\b|\bCHOLEDOCALITHIASIS\b|\bCHOALNGITIS\b|\bCHOLANGITIS\b|\bCHOLECYSTITIS\b|\bCHOLECYSTIS\b|\bCHOLEDOCHOLITHIASIS\b': 'Gastrointestinal Issues',
        r'\bBPH\b': 'Gastrointestinal Issues',
        r'\bMEGACOLO[MN]\b': 'Gastrointestinal Issues',
        r'\bCONSTIPATION\b|\bINCONTINENCE\b|\bURETERAL\b|\bURETHERAL\b|\bRECTAL\b|\bPROSTATITIS\b|\bBLADDER\b|\bURETER\b|\bPELVIC\b|\bBOWEL\b': 'Gastrointestinal Issues',
        r'\bG[- ]?TUBE\b|\bJ-TUBE\b|\bG-J\b': 'Gastrointestinal Issues',
        r'\bINTESTINAL\b': 'Gastrointestinal Issues',
        r'\bGERD\b': 'Gastrointestinal Issues',
        r'\bPERFORATED[ ]VISCOUS\b': 'Gastrointestinal Issues',
        r'\bVOLVUL[O]?US\b|\bVULVULOS\b': 'Gastrointestinal Issues',
        r'\bBRBPR\b|\bBRIGHT RED BLOOD PER RECTUM\b': 'Gastrointestinal Issues',
        r'\bIDDM\b|\bDIABETES\b|\bDIABETIC\b': 'Gastrointestinal Issues',
        r'\bHEMOPERITONEUM\b': 'Gastrointestinal Issues',
        r'\bINGUINAL[ ]HERNIA[S]?\b|\bHIATAL[ ]HERNIA\b|\bVENTRAL[ ]HERNIA\b|\bINGU[I]?NAL\b': 'Gastrointestinal Issues', 
        r'\bCHOLE\b': 'Gastrointestinal Issues',
        r'\bGASTRINOMA\b': 'Gastrointestinal Issues', 
        r'\bPOUCHITIS\b': 'Gastrointestinal Issues',
        r'\bSTOMACH\b': 'Gastrointestinal Issues',
        r'\bILEUS\b|\bILIEUM\b|\bDUODE[N]?UM\b|\bDUODENAL\b|\bJEJUNUM\b|\bJEJUNAL\b': 'Gastrointestinal Issues', 
        r'\bGUT\b|\bGI\b': 'Gastrointestinal Issues',
        r'\bGARDNERS\b|\bRAYNAUDS\b': 'Gastrointestinal Issues', 
        r'\bPANOLITIS\b|\bIBD\b': 'Gastrointestinal Issues',
        r'\bFASCIAL\b': 'Gastrointestinal Issues', 
        r'\bEXPLORATORY[ ]LAP\b': 'Gastrointestinal Issues',
        r'\bODYNOPHAGIA\b': 'Gastrointestinal Issues', 
        r'\bFREE[ ]AIR\b': 'Gastrointestinal Issues',
        r'\bERCP\b': 'Gastrointestinal Issues',
        r'\bGALL[ ]?STONE[S]?\b|\bSTONE\b|\bGALL[ ]?BLADDER\b|\bURINE\b': 'Gastrointestinal Issues',
        r'\bOGILV[I]?E\b': 'Gastrointestinal Issues',
        r'\bINTUSSUCEPTION\b': 'Gastrointestinal Issues',
        r'\bR/O[ ]HERSCH\b': 'Gastrointestinal Issues',
        r'\bCYSTO[ ]SUPRATOIC[ ]TUBE\b': 'Gastrointestinal Issues',
        r'\bMIDLINE[ ]HERNIA\b': 'Gastrointestinal Issues',
        r'\bMEL[AE]NA\b': 'Gastrointestinal Issues',
        r'\bPOLYP ADENOMATOUS\b': 'Gastrointestinal Issues',
        r'\bAMPULLARY\b': 'Gastrointestinal Issues',
        r'\bAPPENDECTOMY\b': 'Gastrointestinal Issues',
        r'\bUGIB\b': 'Gastrointestinal Issues',
        r'\bAPPENDICITIS\b': 'Gastrointestinal Issues',
        r'\bINCARCERATED[ ]HERNIA\b|\bINCISIONAL[ ]HERNIA\b|\bVENTRAL[ ]HERNIA\b': 'Gastrointestinal Issues',
        r'\bMESENTERIC\b': 'Gastrointestinal Issues',
        r'\bCOLITIS\b': 'Gastrointestinal Issues',
        r'\bCHOLANGIOPANCREATOGRAPHY\b': 'Gastrointestinal Issues',
        r'\bGASTROPARESIS\b|\bGASTROENTERISTIS\b|\bGASTROENTERITIS\b': 'Gastrointestinal Issues',
        r'LARYNGOTRACHIAL': 'Gastrointestinal Issues',
        r'\bDUODENITIS\b|\bEPIGASTRIC\b': 'Gastrointestinal Issues',

        r'\bCP\b': 'Neurological Issues',
        r'\bATAXIA\b': 'Neurological Issues',
        r'\bPSYCHOSIS\b|\bAUTONOMIC DYSFUNCTION\b': 'Neurological Issues',
        r'\bEEG\b': 'Neurological Issues',
        r'\bTHORACIC\b': 'Neurological Issues',
        r'\bMYELOPATHY\b': 'Neurological Issues',
        r'\bBRAIN\b': 'Neurological Issues',
        r'\bCERVICAL\b': 'Neurological Issues',
        r'\bDIPLOPIA\b': 'Neurological Issues',
        r'\bAMS\b': 'Neurological Issues',
        r'\bSUB[ ]?ARACH[A]?NOID\b|\bSUBARACHNIOD\b|\bSUBARACH[NR]OID\b|\bARACHNOID\b': 'Neurological Issues',
        r'\bTRIGEMINAL\b': 'Neurological Issues',
        r'\bNEURALGIA\b': 'Neurological Issues',
        r'\bDELTA[ ]MS\b': 'Neurological Issues',
        r'\bC2FRACTURE\b': 'Neurological Issues',
        r'\bSEROTONIN\b': 'Neurological Issues',
        r'\bNEUROACIDOSIS\b|\bNEUROSAICOIODOSIS\b': 'Neurological Issues',
        r'\bCHARCOT\b': 'Neurological Issues',
        r'\bDYSTONI[AC]\b': 'Neurological Issues',
        r'\bLUM[B]?AR\b': 'Neurological Issues',
        r'\bSPONDYLOLISTHESIS\b|\bSPONDYLOLOTHIASIS\b': 'Neurological Issues',
        r'\bEPILEPSY\b|\bEPI\b': 'Neurological Issues',
        r'\bFACIAL DROOP\b': 'Neurological Issues',
        r'\bCER[E]?BRAL\b': 'Neurological Issues',
        r'\bPNEUMOCEPHALUS\b': 'Neurological Issues',
        r'\bKEARNS SAYER\b': 'Neurological Issues',
        r'\bDEPRESSION\b|\bANXIETY\b': 'Neurological Issues',
        r'\bCEREBELL[AE]R\b|\bCEREBELLA\b|\bCEREBELLUM\b': 'Neurological Issues',
        r'\bMY[AE]STHENIA\b|\bMG\b': 'Neurological Issues',
        r'\bPARAPLEGIA\b|\bPARALYSIS\b': 'Neurological Issues',
        r'\bSDH\b': 'Neurological Issues',
        r'\bMENING[I]?OMA\b|\bMENGIOMA\b': 'Neurological Issues',
        r'\bAPHASIA\b': 'Neurological Issues',
        r'\bCNS\b': 'Neurological Issues',
        r'\bCONCUSSION\b': 'Neurological Issues',
        r'\bPOLYDIPSIA\b|\bPOLYDISPIA\b': 'Neurological Issues',
        r'\bTHALAMIC\b': 'Neurological Issues',
        r'\bCORD\b|\bDISC\b|\bSPINE\b|\bSPI[A]?NAL\b|\bVERTEBRAL\b': 'Neurological Issues',
        r'\bBASAL[ ]GANGLIA\b': 'Neurological Issues',
        r'\bICB\b|\bTIA\b|\bICH\b|\bIPH\b': 'Neurological Issues',
        r'\bSCOLIOSIS\b|\bKYPHOSIS\b|\bKYPHOSCOLIOSIS\b': 'Neurological Issues',
        r'\bMENT[AQ]L\b|\bDEL[IE]RIUM\b': 'Neurological Issues',
        r'\bCRANIAL\b|\bSKULL\b|\bCRANIOTOMY\b|\bINTRACRANIAL\b|\bINTRACRAINIAL\b|\bINTERCRANIAL\b': 'Neurological Issues',
        r'\bINTERPARENCYMAL\b|\bINTRAPARENCHYMAL\b|\bPARENCHYMAL\b|\bINTRAPRAECHYMAL\b': 'Neurological Issues',
        r'\bLAMINECTOMY\b': 'Neurological Issues',
        r'\bSEI[SZ]URE[S]?\b|\bSEZIZURE[S]?\b|\bSIEZURE[S]?\b|\bSEZIURE\b': 'Neurological Issues',
        r'\bAMYLOIDOSIS\b': 'Neurological Issues',
        r'\bGBS\b|\bSCI\b|\bSAH\b|\bCVA\b': 'Neurological Issues',
        r'\bMS\b': 'Neurological Issues',
        r'\bCATATONIA\b': 'Neurological Issues',
        r'\bPINEAL\b': 'Neurological Issues',
        r'\bMYASTHENIA GRAVIS\b|\bMYESTEMIA\b|\bMG\b|\bMY[AE]STHENIC\b|\bGRAVIS\b': 'Neurological Issues',
        r'\bANTERIOR CERVICAL COLLECTION\b|\bACDF\b': 'Neurological Issues',
        r'\bCOLLID CYST\b': 'Neurological Issues',
        r'\bGUILLAIN[- ]?BARRE\b|\bGUILLIAN\b|\bGUIANNE\b|\bGILLIAM\b|\bGU[I]?LL[I]?AN\b': 'Neurological Issues',
        r'\bSUBDURAL\b': 'Neurological Issues',
        r'\bSTR[OU]KE\b': 'Neurological Issues',
        r'\bENCEPHALOPATHY\b|\bHYDROCEPHALUS\b|\bENCEPHALOMYELITIS\b': 'Neurological Issues',
        r'\bCEREBRO[BV]AS[CV]ULAR\b': 'Neurological Issues',
        r'\bEPILEPTIC\b|\bEP[IE]LEPTICUS\b': 'Neurological Issues',
        r'\bHEMIPARESIS\b|\bHEMOPARINEUM\b': 'Neurological Issues',
        r'\bVISUAL\b': 'Neurological Issues',
        r'\bCHIARI\b': 'Neurological Issues',
        r'\bNEURO\b|\bNUERO\b|\bNEUROPATHY\b': 'Neurological Issues',
        r'\bLOBE[ ]LESION\b': 'Neurological Issues',
        r'\bSPONDYLOSIS\b': 'Neurological Issues',
        r'\bMYLEOPATHY\b': 'Neurological Issues',
        r'\bSCHIZOPHRENIA\b': 'Neurological Issues',
        r'\bFRONTAL[ ]LOBE\b|\bPARIETAL[ ]LOBE\b|\bOCCIPITAL[ ]LOBE\b|\bTEMPORAL[ ]LOBE\b': 'Neurological Issues',
        r'\bEQUINA\b': 'Neurological Issues',
        r'\bLYME\b': 'Neurological Issues',

        r'\bANEURSYM\b|\bANUERYSM\b|\bANEURYSM\b': 'Blood Conditions',
        r'\bEPISTAXIS\b': 'Blood Conditions',
        r'\bHYPERPARATHYROIDISM\b|\bHYPOPARATHYROIDISM\b|\bHYPERTHYROIDISM\b|\bHYPOTHYROIDISM\b': 'Blood Conditions',
        r'\bHYPERCARBIA\b': 'Blood Conditions',
        r'\bARTERIAL\b|\bATERIAL\b|\bARTERAL\b|\b[A]?VASCULAR\b': 'Blood Conditions',
        r'\bCOMPARTMENT[ ]SYNDROME\b': 'Blood Conditions',
        r'\bHCT[ ]DROP\b': 'Blood Conditions',
        r'\bHYPER[ ]?STIMULATION\b': 'Blood Conditions',
        r'\bHEMORRHAGIC|HEMORRHAGE\b': 'Blood Conditions',
        r'\bHYPOXEMIA\b': 'Blood Conditions',
        r'\bACIDOSIS\b': 'Blood Conditions',
        r'\bIPH\b|\bTTP\b|\bSMA\b|\bIVC\b|\bCFA\b|\bDIC\b|\bDVT\b|\bMVC\b|\bPVD\b|\bHTN\b|\bDKA\b': 'Blood Conditions',
        r'\bCOAGULOPATHY\b': 'Blood Conditions',
        r'\bCAVENOMA\b': 'Blood Conditions',
        r'\bELEVATED\b': 'Blood Conditions',
        r'\bATHERSCLEROSIS\b|\bARTHEROSCLEROSIS\b': 'Blood Conditions',
        r'\bRHABDO\b|\bRHABDOM[M]?YOLYSIS\b': 'Blood Conditions',
        r'\bTRIPLE[ ]A\b|\bAAA\b|bBTYPE[ ]A\b': 'Blood Conditions',
        r'\bARTERIOVENOUS\b|\bAV\b': 'Blood Conditions',
        r'\bTHROMBOS\b|\bTHROMBOCYTOPENIC\b|\bTHROBO[CV]YTOPENIA\b|\bTHROMBECTOMY\b|\bTHROMBOSIS\b|\bTHROMBOEMBOLISM\b': 'Blood Conditions',
        r'\bENDARARECTOMY\b': 'Blood Conditions',
        r'\bAOTRIC\b|\bAORTA\b|\bAORTIC\b': 'Blood Conditions',
        r'\bHYPOKALEMI[M]?A\b|\bHYPERKALEMIA\b|\bKALEMIA\b': 'Blood Conditions',
        r'\bHYPOTENSIO[NM]\b|\bHYPERTENSIO[NM]\b|\bHYPOTENSIVE\b|\bHYPERTEN[B]?SIVE\b': 'Blood Conditions',
        r'\bHYPONATREMIA\b|\bHYPERNATREMIA\b|\bNATREMIA\b': 'Blood Conditions',
        r'\bHYPERMAGNESEMIA\b|\bHYPOMAGNESEMIA\b': 'Blood Conditions',
        r'\bMYXEDEMA\b': 'Blood Conditions',
        r'\bGLUCOSE\b': 'Blood Conditions',
        r'\bACIDEMIA\b': 'Blood Conditions',
        r'\bVASCULITIS\b': 'Blood Conditions',
        r'\bCLOT\b': 'Blood Conditions',
        r'\bAR[I]?TERITIS\b': 'Blood Conditions',
        r'\bHYPOCAPNEA\b': 'Blood Conditions',
        r'\bKE[T]?O[A]?CIDOSIS\b': 'Blood Conditions',
        r'\bH[Y]?PER[E]?GLYCEMIA\b|\bH[Y]?POGLYCEMIA\b|\bHIGH[ ]BLOOD[ ]SUGAR\b|\bLOW[ ]BLOOD[ ]SUGAR\b': 'Blood Conditions',
        r'\bILIAC\b': 'Blood Conditions',
        r'\bANASARCA\b': 'Blood Conditions',
        r'\bPHLEGMASIA\b': 'Blood Conditions',
        r'\bANEMIA\b': 'Blood Conditions',
        r'\bHYPERBILIRUBIN[IE]MIA\b|\bHYPERBILIRUBERIMIA\b': 'Blood Conditions',
        r'\bSICKLE[ ]CELL\b': 'Blood Conditions',
        r'\bANGIO\b': 'Blood Conditions',
        r'\bHYPERCALCEMIA\b': 'Blood Conditions',
        r'\bCAROTIS[ ]ARTERY[ ]STENOSIS\b': 'Blood Conditions',
        r'\bCLOTTED[ ]IV[ ]FISTULA\b': 'Blood Conditions',
        r'\bATHEROSCLEROSIS\b|\bARTHROSLOROSIS\b': 'Blood Conditions',
        r'\bULCER\b': 'Blood Conditions',
        r'\bLITHIUM\b|\bLI\b': 'Blood Conditions',
        r'\bMASTOCYTOSIS\b|\bSTENOSIS\b': 'Blood Conditions',
        r'\bNEUTROPENIA\b|\bPANCYTOPENIA\b': 'Blood Conditions',
        r'\bISCHEMIC\b|\bIS[C]?HEMIA\b': 'Blood Conditions',
        r'\bGANGRENE\b': 'Blood Conditions',
        r'\bVOLUME[ ]OVERLOAD\b|\bFLUID[ ]OVERLOAD\b': 'Blood Conditions',
        r'\bPERIPHERAL[ ]INSUFFICIENCY\b': 'Blood Conditions',
        r'\bMETHYLGLOBLUIN\b': 'Blood Conditions',
        r'\bWBC\b|\bELECTROLYTE[S]\b': 'Blood Conditions',

        r'\bDRUG\b|\bOD\b|\bOVER[ ]?DOSE\b|\bTOXICITY\b|\bINTOXICATION\b': 'Substance-Related Issues',
        r'\bMULTIPLE\b|\bSUB[S]?TANCE\b|\bPOLY[ ]?SUB[S]?TANCE\b|\bMULTISUB[S]?TANCE\b|\bSUB[S]?TANCE[ ]ABUSE\b|\bWITHDRAW[AE]?L\b|\bWD\b|\bPOLYSUBSTNACE\b': 'Substance-Related Issues',
        r'\bTY[LN]E[LN]OL\b|\bOPIATE\b|\bOPIOID\b|\bTEGRETOL\b|\bCOCAINE\b|\bLI\b|\bLITHIUM\b|\bSTEROID[S]?\b': 'Substance-Related Issues',
        r'\bETOH\b|\bETHANOL\b|\bALCOHOL\b|\bBENZO\b|\bB-BLOCKER\b': 'Substance-Related Issues',
        r'\bASPIRIN\b|\bBENADRYL\b|\bBACOFLEN\b|\bDIGOXIN\b|\bBENZODIAZEPINE\b|\bCCB\b|\bETHYLENE GLYCOL\b|\bHEROIN\b|\bHERION\b': 'Substance-Related Issues',
        r'\bALCOHOLIC\b|\bDEPAKOTE\b|\bCITALOPRAM\b|\bDETOX\b|\bTCA\b|\bTRAZADONE\b': 'Substance-Related Issues', 

        r'\bFEMUR\b': 'Other',
        r'\bTOXIC SHOCK\b': 'Other',
        r'\bMALAISE\b': 'Other',
        r'\bUNRESPONSIVE\b': 'Other',
        r'\bHONK\b': 'Other',
        r'\bSLEEP\b|\bAPNEA\b': 'Other',
        r'\bRULE OUT\b': 'Other',
        r'\bFOREIGN\b|\bDEFECT\b': 'Other',
        r'\bENDOMETRITIS\b': 'Other',
        r'\bWEIGHT\b': 'Other',
        r'\bPRESYNCOPE\b': 'Other',
        r'\bFO[O]?UND DOWN\b': 'Other',
        r'\bGRAFT\b|\bTISSUE\b': 'Other',
        r'\bPSYCH\b': 'Other',
        r'\bTRANSPLANT\b': 'Other',
        r'\bPULSELESS\b|\bNUMBNESS\b': 'Other',
        r'\bGUMS\b|\bEDEMA\b|\bOOZING\b|\bLEAKING\b|\bLEAK[S]\b|\bLEAKAGE[S]?\b': 'Other',
        r'\bSPEECH\b': 'Other',
        r'\bPES\b|\bPLANOVALGULS\b|\bPLANO\b': 'Other',
        r'\bANKLE\b': 'Other',
        r'\bDEHISCENCE\b': 'Other',
        r'\bDIZZINESS\b': 'Other',
        r'\bFAILING\b|\bFAILURE[S]?\b|\bFAILED\b|\bMALFUNCTION[S]?\b': 'Other',
        r'\bROMI\b': 'Other',
        r'\bSHUNT\b': 'Other',
        r'\bSHOCK\b|\bCOOL\b|\bSPASM\b': 'Other',
        r'\bVISION LOSS\b': 'Other',
        r'\bHYPOTHERMIA\b|\bHYPERTHERMIA\b': 'Other',
        r'\bHEADACH[E]?\b|\bHEADCAHE\b': 'Other',
        r'\bHANGING\b|\bSUICIDE\b|\bSUICIDAL\b|\bJUMP\b': 'Other',
        r'\bBURN[S]?\b': 'Other',
        r'\bCONFUSION\b|\bOBTUNDED\b': 'Other',
        r'\bREIMPLANTATION OF\b': 'Other',
        r'\bGOITER\b|\bGOUT\b|\bFLANK\b': 'Other',
        r'\bOVARIAN\b|\bOVARY\b|\bUTERUS\b|\bVAGINA[L]?\b|\bUMBILICAL\b': 'Other',
        r'\bTOUNGE\b|\bTONGUE\b': 'Other',
        r'\bNON-[ ]?HEALING\b|\bNON[ ]?HEALING\b': 'Other',
        r'\bHIP\b|\bOA\b|\bOSTEOARTHRITIS\b|\bARTHRITIS\b': 'Other',
        r'\bAMPUTATION\b|\bREPLACEMENT\b|\bTRANSPLANT[S]?\b|\bNON[ ]?VIABLE\b': 'Other',
        r'\bRASH\b|\bSTEVEN[ ]JOHNSON[ ]SYNDROME\b': 'Other',
        r'\bANAPHYLAXIS\b|\bEXPOSURE\b|\bALLERGIC[ ]REACTION\b|\bALLERGY\b|\bANGIO[ ]?EDEMA\b': 'Other',
        r'\bNODE\b|\bMASS\b': 'Other',
        r'\bANOREXIA\b|\bBULIMIA\b':'Other',
        r'\bFATIGUE\b|\bLETHARGY\b|\bLETHARGIC\b': 'Other',
        r'\bDIARRHEA\b|\bDIAHRREA\b': 'Other',
        r'\bINCISION DRAINAGE\b': 'Other',
        r'\bNAUS[E]?A\b|\bVOMIT[T]?ING\b|\bHEMATEMESIS\b': 'Other',
        r'\bORIG[IE]N\b|\bUNKNOWN\b': 'Other',
        r'\bFEBRILE[ ]SYNDROME\b|\bSWELLING\b': 'Other',
        r'\bLOWER\b': 'Other',
        r'\bORGAN[ ]DONOR\b': 'Other',
        r'\bURESPONSIVE\b': 'Other',
        r'\bMORBID\b|\bOBESITY\b|\bOBESE\b|\bMALNUTRITION\b': 'Other',
        r'\bDEHYDRATION\b': 'Other',
        r'\bUNABLE[ ]TO[ ]STAND\b': 'Other',
        r'\bPAIN\b|\bPAINFUL\b|bNOSE BLEED\b': 'Other',
        r'\bFE[BV]ER[ES]?\b|\bNEUTROPENIC\b': 'Other',
        r'\bWEAKNESS\b|\bTELEMETRY\b': 'Other',
        r'\bCLAUDICATION\b|\bCLOTACATION\b': 'Other', 
        r'||': 'Other',
    }
    
    def get_category(diagnosis):
        if pd.isna(diagnosis) or not isinstance(diagnosis, str):
            return 'Other'
        
        for pattern, category in diagnosis_mapping.items():
            if re.search(pattern, diagnosis):
                #print(f"Matched '{diagnosis}' to category '{category}' with pattern '{pattern}'")  # Debugging print statement
                return category
        return 'Other'

    return df_column.apply(get_category)