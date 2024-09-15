import re
import pandas as pd

def mapped_diagnosis(df_column):
    diagnosis_mapping = {
        r'\bSTAB\b|\bSTABBI[NM]G\b': 'Trauma/Injury',
        r'\bM[P]?OTOR\b|\bMOTORCYCLE\b|\bMOTORVEHICLE\b|\bVEHICLE\b|\bBICYCLE\b|\bBIKE\b|\bSTRUCK\b|\bBICYCLE/CAR\b|\bATV\b|\bPEDESTRIAN\b|\bCAR\b|\bMVA\b': 'Trauma/Injury',
        r'\bFRACTURE[S]?\b|\bFRACTURED\b|\bF[R]?X[S]?\b|\bINJURY\b': 'Trauma/Injury',
        r'\bT[R]?[AE]?UM[A]?\b|\bWOUND\b|\bLACERATION\b': 'Trauma/Injury',
        r'\bFALL\b|\bDISLOCATION\b': 'Trauma/Injury',
        r'\bGUN\b|\bGUNSHOT\b|\bGSW\b': 'Trauma/Injury',
        r'\b0681\b': 'Trauma/Injury',
        r'\bTEAR\b': 'Trauma/Injury',
        r'\bHEMATOMA\b': 'Trauma/Injury',
        r'\bHEMOTHORAX\b': 'Trauma/Injury',
        r'\bASSAULT\b': 'Trauma/Injury',
        r'\bFEMUR NON UNION\b': 'Trauma/Injury',
        r'\bTIB;FIB\b': 'Trauma/Injury',

        r'\bNECROTIZING\b|\bNECROTISING\b|\bNECTROTIZING\b|\bNECROTZING\b': 'Infections',
        r'\bSHINGLES\b': 'Infections',
        r'\bFASCIETIS\b|\bFASCITITIS\b|\bFASCITIS\b|\bFASCEITIS\b|\bFASCIITIS\b|\bFASCILITIS\b|\bFASCIATIS\b': 'Infections',
        r'\bDISCITIS\b': 'Infections',
        r'\bPYLEONEPHRITIS\b|\bPYELONEPHRITIS\b|\bPYLONEPHRITIS\b|\bUTI\b': 'Infections',
        r'\bVRE\b': 'Infections',
        r'\bFLU\b|\bINFLUENZA\b': 'Infections',
        r'\bOSTEOMYLITIS\b': 'Infections',
        r'\bC[-]?DIFF\b': 'Infections',
        r'\bLEUKOCYTOSIS\b': 'Infections',
        r'\bMENI[N]?GITIS\b': 'Infections',
        r'\bHIV\b': 'Infections',
        r'\bMONO\b|\bMONONUCLEOSIS\b|\bEBV\b': 'Infections',
        r'\bNEURO[ ]?SYPHIL[L]?IS\b': 'Infections',
        r'\bSEP[S]?IS\b|\bSEPISI\b|\bSEPTIC\b': 'Infections',
        r'\bHEPATITIS\b': 'Infections',
        r'\bURINARY\b': 'Infections',
        r'\bUROSEPSIS\b': 'Infections',
        r'\bCELLULITIS\b|\bCELLULTIIS\b': 'Infections',
        r'\bINFECTION\b|\bINFECTED\b': 'Infections',
        r'\bBACTEREMIA\b': 'Infections',
        r'\bMENINGITIS\b': 'Infections',
        r'\bAB[S]?CESS\b': 'Infections',
        r'\bPERITONITIS\b': 'Infections',
        r'\bOSTEOMYELITIS\b': 'Infections',
        r'\bASPERGILOMA\b': 'Infections',

        r'\bHODGKIN\'S\b|\bNON[-]?HODGKIN\'S\b|\bHODGKINS\b|\bNONHODGKINS\b': 'Cancer',
        r'\bHEPATOMA\b': 'Cancer',
        r'\bL[E]?UKEMIA\b': 'Cancer',
        r'\bMYELOMA\b': 'Cancer',
        r'\bSA[R]?COMA\b': 'Cancer',
        r'\bCHEMO\b|\bCHEMOTHERAPY\b|\bCANCER\b|\bTUMOR\b': 'Cancer',
        r'\bALLO TX\b': 'Cancer',
        r'\bTHYMOMA\b': 'Cancer',
        r'\bAML\b': 'Cancer',
        r'\bGBM\b': 'Cancer',
        r'\bTYPHLITIS\b': 'Cancer',
        r'\bTURBT\b': 'Cancer',
        r'\bCA\b|\bCA/SDA\b': 'Cancer',
        r'\bMETASTATIC\b|\bMALIGNANT\b': 'Cancer',
        r'\bMELANOMA\b': 'Cancer',
        r'\bGLIOBLASTOMA\b': 'Cancer',
        r'\bLY[MN]PHOMA\b': 'Cancer',
        r'\bMENIGIOMA\b': 'Cancer',
        r'\bCARCINOMA\b|ADENOCARCINOMA': 'Cancer',
        r'\bMYELOFIBROSIS\b': 'Cancer',
        r'\bCMML\b': 'Cancer',
        r'\bCARCINOMATOSIS\b': 'Cancer',
        r'\bMETASTISIS\b|\bMETASTASIS\b': 'Cancer',
        
        r'\bARF\b|\bGIB\b': 'Renal Issues',
        r'\bCRF\b': 'Renal Issues',
        r'\bCONN\'S\b': 'Renal Issues',
        r'\bREN[A]?L\b': 'Renal Issues',
        r'\bKIDNEY\b': 'Renal Issues',

        r'\bHIBILIRUBIN\b|\bHYPERBILIRUBEN\b|\bHYPERBILRUBINEIMA\b|\bHYPERVILIRUBINEMIA\b|\bBILIRUBINEMIA\b|\bBILIRUBEN\b': 'Liver Issues',
        r'\bINSULIN DENSENTIZATION\b': 'Liver Issues',
        r'\bASCITES\b': 'Liver Issues',
        r'\bTRANSAMINITIS\b': 'Liver Issues',
        r'\bLIVER\b': 'Liver Issues',
        r'\bHEPATIC\b': 'Liver Issues',
        r'\bCIRRHOSIS\b': 'Liver Issues',
        r'\bJAUNDICE\b': 'Liver Issues',

        r'\bPREGNANCY\b|\bLABOR\b|\bC[ ]?SECTION\b': 'Neonatal Care',
        r'\bFAILURE TO THIRVE\b|\bFTT\b': 'Neonatal Care',
        r'\bPREMATURE\b|\bPREMATURITY\b': 'Neonatal Care',
        r'\bDUSKY SPELLS\b': 'Neonatal Care',
        r'\bNEWBORN\b': 'Neonatal Care',

        r'\bATRAIL\b|\bATRIAL\b': 'Cardiovascular Issues',
        r'\bSVT\b|\bSVC\b': 'Cardiovascular Issues',
        r'\b\+MIBI\b': 'Cardiovascular Issues',
        r'\bFORAMEN OVALE\b|\bPFO\b': 'Cardiovascular Issues',
        r'\bCABG[E]?\b': 'Cardiovascular Issues',
        r'\bV-?TACH\b|\bVT\b|\bVT/VF\b': 'Cardiovascular Issues',
        r'\bMVR\b': 'Cardiovascular Issues',
        r'\bMYO[I]?CARDIAL\b|\bM.?I.?\b': 'Cardiovascular Issues',
        r'\bARREST\b|\bPOST[-]?ARREST\b': 'Cardiovascular Issues',
        r'\bVENTRICULAR FIBRILLATION\b|\bV[-]?FIB\b': 'Cardiovascular Issues',
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
        r'\bHEART\b|\bCARDIAC\b|\bCARDIOGENIC\b|\bCARDIOMYOPATHY\b|\bPACEMAKER\b': 'Cardiovascular Issues',
        r'\bELEVATED TROPONIN\b': 'Cardiovascular Issues',
        r'\bDEFIBRILLATOR\b': 'Cardiovascular Issues',
        r'\bARRYTHMIA\b': 'Cardiovascular Issues',
        r'\bTRICUSPID\b': 'Cardiovascular Issues',
        r'\bMR\\\\\b|\bMR\\\b|\bMR\b|\bMR\\MITRAL\b': 'Cardiovascular Issues',
        r'\bREGURGITATION\b': 'Cardiovascular Issues',
        r'\bSYNCOPE\b': 'Cardiovascular Issues',
        r'\bCAROTID\b': 'Cardiovascular Issues',
        r'\bAORTIC\b': 'Cardiovascular Issues',
        r'\bSTEMI\b': 'Cardiovascular Issues',
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
        r'\bAVR\b': 'Cardiovascular Issues',
        
        r'\bPNE[U]?MO[NM]IA\b|\bPNAUMONIA\b|\bPNA\b': 'Respiratory Issues',
        r'\bINFILTRATE[S]?\b': 'Respiratory Issues',
        r'\bCOUGH\b': 'Respiratory Issues',
        r'\bASPIRATION\b': 'Respiratory Issues',
        r'\b[R]?ESP[.]?\b|\bRE[S]?PIRATO[RT]Y\b|\bRESPITORY\b': 'Respiratory Issues',
        r'\bTHROAT\b': 'Respiratory Issues',
        r'\bLARYNGOSPASM\b': 'Respiratory Issues',
        r'\bTRACHEOMALACIA\b|\bTRACHEOSTOMY\b|\bTRACHEOBRONCHOPLASTY\b': 'Respiratory Issues',
        r'\bLOBE COLLAPSE\b': 'Respiratory Issues',
        r'\bPULMO[NM]ARY\b|\bPE\b': 'Respiratory Issues',
        r'\bCOPD\b': 'Respiratory Issues',
        r'\bPE\b|\bPULM\b|\bPNEUMOPERTONEUM\b': 'Respiratory Issues',
        r'\bLUNG\b': 'Respiratory Issues',
        r'\bDIAPHRA[G]?MATIC\b': 'Respiratory Issues',
        r'\bCHYLOTHORAX\b': 'Respiratory Issues',
        r'\bARDS\b': 'Respiratory Issues',
        r'\bSHOTRNESS OF[R]? BREATH\b|\bSOB\b': 'Respiratory Issues',
        r'\bTRACHEOBROCHOMALACIA\b|\bTRACHEO-BRONCHEO\b|\bTRACHEOBRONCHIO\b|\bTRACHEO-BRONCHEAL\b|\bTRACHEOBRONCHOMALACIA\b|\bTRACHEOBRONCOMALICIA\b': 'Respiratory Issues',
        r'\bHEMOP[T]?YSIS\b|\bHEMPOTYSIS\b': 'Respiratory Issues',
        r'\bTACHYPNEA\b': 'Respiratory Issues',
        r'\bHEMIPTHSIS\b': 'Respiratory Issues',
        r'\bTRACH\b|\bTRACHEA\b|\bTRACIAL\b|\bTRACHEOSTOMY\b|\bTRA[N]?CHEAL\b|\bTRACHAEL\b|\bTRACHEO\b': 'Respiratory Issues',
        r'\bEMPHSYEMA\b|\bEMPYEMA\b': 'Respiratory Issues',
        r'\bFIBROTHORAX\b': 'Respiratory Issues',
        r'\bMESOTHELIOMA\b': 'Respiratory Issues',
        r'\bCAVITARY\b': 'Respiratory Issues',
        r'\bASTHMA\b': 'Respiratory Issues',
        r'\bDYSPN[IE]A\b|\bDYPSNEA\b': 'Respiratory Issues',
        r'\bHYPOXIA\b': 'Respiratory Issues',
        r'\bCHEST\b': 'Respiratory Issues',
        r'\bCOPD\b|\bCHRONIC OBST PULM DISEASE\b': 'Respiratory Issues',
        r'\bBRADYCARDIA\b': 'Respiratory Issues',
        r'\bPLEURAL\b': 'Respiratory Issues',
        r'\bAIRWAY\b': 'Respiratory Issues',
        r'\b\+ETT.?\\?CATH\b': 'Respiratory Issues',
        r'\bPNEUMOTHORAX\b': 'Respiratory Issues',
        r'\bSTRIDOR\b': 'Respiratory Issues',
        r'\bBRONCHIAL\b|\bBRONCHIATISIS\b|\bBRONCHIOLE[S]?\b': 'Respiratory Issues',
        r'\bTB\b': 'Respiratory Issues',
        r'\bBOERHAAVE\b': 'Respiratory Issues',

        
        r'A\bCHALASIA\b': 'Gastrointestinal Issues',
        r'\bVENTRAL HERNIA\b': 'Gastrointestinal Issues',
        r'\bENTERIC FISTULA\b|\bENTEROCUTANEUS FISTULA\b|\bENTERO[ ]?CUTA[N]?EOUS\b|\bINTRACUTANEOUS FISTULA\b': 'Gastrointestinal Issues',
        r'\bCECUM\b': 'Gastrointestinal Issues',
        r'\bABDOMEN\b|\bABDOMAL\b|\bABD[.]?\b|\bABDOMINAL\b|\bADBOMINAL\b': 'Gastrointestinal Issues',
        r'\bSUPRA[ ]?GLOTTITIS\b|\bEPIGLOT[T]?ITIS\b|\bSUPERGLOTTITIS\b': 'Gastrointestinal Issues',
        r'\bSPLEEN\b|\bSPLENOMEGALIA\b|\bSPLE[E]?NECTOMY\b|\bSPLENOMEGALY\b|\bSPLENIC\b': 'Gastrointestinal Issues',
        r'\bPANCREAS\b|\bPANCREATIC\b|\bPANREATITIS\b': 'Gastrointestinal Issues',
        r'\bBILIARY\b|\bBILE\b': 'Gastrointestinal Issues',
        r'\bBARRETT\'S\b': 'Gastrointestinal Issues',
        r'\bCOLON\b|\bCOLON[G]?IC\b': 'Gastrointestinal Issues',
        r'\bINSULINOMA\b': 'Gastrointestinal Issues',
        r'\bOSTOMY\b': 'Gastrointestinal Issues',
        r'\bCHRON\'S\b|\bCROHN\'S\b|\bCHRONS\b|\bCROHNS\b': 'Gastrointestinal Issues',
        r'\bSWALLOWED\b|\bINGESTED\b|\bINGESTION\b': 'Gastrointestinal Issues',
        r'\bDYSPHAGIA\b': 'Gastrointestinal Issues',
        r'\bGASTRIC\b|\bGASTRO\b|\bGASTROINTESTINAL\b|\bESOPHAGUS\b|\bESOPHAGEAL\b|\bDIVERTICULAR\b|\bDIVERTICULITIS\b': 'Gastrointestinal Issues',
        r'\bCHOLECYSITIS\b|\bCHOLELITHIASIS\b|\bCHOLENGITIS\b|\bCHOELITHIASIS\b|\bCHOLYCYSTITIS\b|\bCHOLEDOCALITHIASIS\b|\bCHOALNGITIS\b|\bCHOLANGITIS\b|\bCHOLECYSTITIS\b': 'Gastrointestinal Issues',
        r'\bBPH\b': 'Gastrointestinal Issues',
        r'\bMEGACOLON\b': 'Gastrointestinal Issues',
        r'\bINCONTINENCE\b|\bURETERAL\b|\bURETHERAL\b|\bRECTAL\b|\bPROSTATITIS\b|\bBLADDER\b|\bURETER\b|\bPELVIC\b|\bBOWEL\b': 'Gastrointestinal Issues',
        r'\bG[-]?TUBE\b|\bJ-TUBE\b|\bG-J\b': 'Gastrointestinal Issues',
        r'\bINTESTINAL\b': 'Gastrointestinal Issues',
        r'\bGERD\b': 'Gastrointestinal Issues',
        r'\bPERFORATED VISCOUS\b': 'Gastrointestinal Issues',
        r'\bVOLVUL[O]?US\b|\bVULVULOS\b': 'Gastrointestinal Issues',
        r'\bBRBPR\b|\bBRIGHT RED BLOOD PER RECTUM\b': 'Gastrointestinal Issues',
        r'\bIDDM\b|\bDIABETES\b|\bDIABETIC\b': 'Gastrointestinal Issues',
        r'\bHEMOPERITONEUM\b': 'Gastrointestinal Issues',
        r'\bINGUINAL HERNIA[S]?\b|\bHIATAL HERNIA\b|\bVENTRAL HERNIA\b|\bINGU[I]?NAL\b': 'Gastrointestinal Issues', 
        r'\bCHOLE\b': 'Gastrointestinal Issues',
        r'\bGASTRINOMA\b': 'Gastrointestinal Issues', 
        r'\bPOUCHITIS\b': 'Gastrointestinal Issues',
        r'\bSTOMACH\b': 'Gastrointestinal Issues',
        r'\bILEUS\b|\bILIEUM\b|\bDUODE[N]?UM\b|\bDUODENAL\b|\bJEJUNUM\b|\bJEJUNAL\b': 'Gastrointestinal Issues', 
        r'\bGUT\b|\bGI\b': 'Gastrointestinal Issues',
        r'\bGARDNERS\b': 'Gastrointestinal Issues', 
        r'\bPANOLITIS\b|\bIBD\b': 'Gastrointestinal Issues',
        r'\bFASCIAL\b': 'Gastrointestinal Issues', 
        r'\bEXPLORATORY LAP\b': 'Gastrointestinal Issues',
        r'\bODYNOPHAGIA\b': 'Gastrointestinal Issues', 
        r'\bFREE AIR\b': 'Gastrointestinal Issues',
        r'\bERCP\b': 'Gastrointestinal Issues',
        r'\bGALLSTONE[S]?\b|\bSTONE\b': 'Gastrointestinal Issues',
        r'\bOGILV[I]?E\b': 'Gastrointestinal Issues',
        r'\bINTUSSUCEPTION\b': 'Gastrointestinal Issues',
        r'\bR/O HERSCH\b': 'Gastrointestinal Issues',
        r'\bCYSTO SUPRATOIC TUBE\b': 'Gastrointestinal Issues',
        r'\bMIDLINE HERNIA\b': 'Gastrointestinal Issues',
        r'\bMELENA\b': 'Gastrointestinal Issues',
        r'\bPOLYP ADENOMATOUS\b': 'Gastrointestinal Issues',
        r'\bAMPULLARY\b': 'Gastrointestinal Issues',
        r'\bAPPENDECTOMY\b': 'Gastrointestinal Issues',
        r'\bUGIB\b': 'Gastrointestinal Issues',
        r'\bAPPENDICITIS\b': 'Gastrointestinal Issues',
        r'\bINCARCERATED HERNIA\b|\bINCISIONAL HERNIA\b|\bVENTRAL HERNIA\b': 'Gastrointestinal Issues',
        r'\bMESENTERIC\b': 'Gastrointestinal Issues',
        r'\bCOLITIS\b': 'Gastrointestinal Issues',
        r'\bCHOLANGIOPANCREATOGRAPHY\b': 'Gastrointestinal Issues',
        r'\bGASTROPARESIS\b|\bGASTROENTERISTIS\b|\bGASTROENTERITIS\b': 'Gastrointestinal Issues',

        r'\bCP\b': 'Neurological Issues',
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
        r'\bDELTA MS\b': 'Neurological Issues',
        r'\bC2FRACTURE\b': 'Neurological Issues',
        r'\bSEROTONIN\b': 'Neurological Issues',
        r'\bNEUROACIDOSIS\b|\bNEUROSAICOIODOSIS\b': 'Neurological Issues',
        r'\bCHARCOT\b': 'Neurological Issues',
        r'\bDYSTONI[AC]\b': 'Neurological Issues',
        r'\bLUM[B]?AR\b': 'Neurological Issues',
        r'\bSPONDYLOLISTHESIS\b|\bSPONDYLOLOTHIASIS\b': 'Neurological Issues',
        r'\bEPILEPSY\b': 'Neurological Issues',
        r'\bFACIAL DROOP\b': 'Neurological Issues',
        r'\bCER[E]?BRAL\b': 'Neurological Issues',
        r'\bPNEUMOCEPHALUS\b': 'Neurological Issues',
        r'\bKEARNS SAYER\b': 'Neurological Issues',
        r'\bDEPRESSION\b|\bANXIETY\b': 'Neurological Issues',
        r'\bCEREBELL[AE]R\b|\bCEREBELLA\b|\bCEREBELLUM\b': 'Neurological Issues',
        r'\bMY[AE]STHENIA\b|\bMG\b': 'Neurological Issues',
        r'\bPARAPLEGIA\b': 'Neurological Issues',
        r'\bSDH\b': 'Neurological Issues',
        r'\bMENINGIOMA\b': 'Neurological Issues',
        r'\bAPHASIA\b': 'Neurological Issues',
        r'\bCNS\b': 'Neurological Issues',
        r'\bCONCUSSION\b': 'Neurological Issues',
        r'\bPOLYDIPSIA\b|\bPOLYDISPIA\b': 'Neurological Issues',
        r'\bTHALAMIC\b': 'Neurological Issues',
        r'\bCORD\b|\bDISC\b|\bSPINE\b|\bSPINAL\b|\bVERTEBRAL\b': 'Neurological Issues',
        r'\bBASAL GANGLIA\b': 'Neurological Issues',
        r'\bICB\b|\bTIA\b|\bICH\b|\bIPH\b': 'Neurological Issues',
        r'\bSCOLIOSIS\b|\bKYPHOSIS\b': 'Neurological Issues',
        r'\bMENT[AQ]L\b|\bDELERIUM\b': 'Neurological Issues',
        r'\bCRANIAL\b|\bSKULL\b|\bCRANIOTOMY\b|\bINTRACRANIAL\b|\bINTERCRANIAL\b': 'Neurological Issues',
        r'\bINTERPARENCYMAL\b|\bINTRAPARENCHYMAL\b|\bPARENCHYMAL\b|\bINTRAPRAECHYMAL\b': 'Neurological Issues',
        r'\bLAMINECTOMY\b': 'Neurological Issues',
        r'\bSEIZURE[S]?\b|\bSEZIZURE[S]?\b': 'Neurological Issues',
        r'\bAMYLOIDOSIS\b': 'Neurological Issues',
        r'\bGBS\b|\bSCI\b|\bSAH\b|\bCVA\b': 'Neurological Issues',
        r'\bMS\b': 'Neurological Issues',
        r'\bCATATONIA\b': 'Neurological Issues',
        r'\bPINEAL\b': 'Neurological Issues',
        r'\bMYASTHENIA GRAVIS\b|\bMG\b': 'Neurological Issues',
        r'\bANTERIOR CERVICAL COLLECTION\b|\bACDF\b': 'Neurological Issues',
        r'\bCOLLID CYST\b': 'Neurological Issues',
        r'\bGUILLAIN[- ]?BARRE\b|\bGUILLIAN\b|\bGUIANNE\b|\bGILLIAM\b|\bGU[I]?LL[I]?AN\b': 'Neurological Issues',
        r'\bSUBDURAL\b': 'Neurological Issues',
        r'\bSTROKE\b': 'Neurological Issues',
        r'\bENCEPHALOPATHY\b|\bHYDROCEPHALUS\b|\bENCEPHALOMYELITIS\b': 'Neurological Issues',
        r'\bCEREBRO[BV]AS[CV]ULAR\b': 'Neurological Issues',
        r'\bEPILEPTIC\b|\bEP[IE]LEPTICUS\b': 'Neurological Issues',
        r'\bHEMIPARESIS\b|\bHEMOPARINEUM\b': 'Neurological Issues',
        r'\bVISUAL\b': 'Neurological Issues',
        r'\bCHIARI\b': 'Neurological Issues',
        r'\bNEURO\b|\bNUERO\b|\bNEUROPATHY\b': 'Neurological Issues',
        r'\bLOBE LESION\b': 'Neurological Issues',
        r'\bSPONDYLOSIS\b': 'Neurological Issues',
        r'\bMYLEOPATHY\b': 'Neurological Issues',

        r'\bANEURSYM\b|\bANUERYSM\b|\bANEURYSM\b': 'Blood Conditions',
        r'\bEPISTAXIS\b': 'Blood Conditions',
        r'\bHYPERPARATHYROIDISM\b|\bHYPOPARATHYROIDISM\b|\bHYPERTHYROIDISM\b|\bHYPOTHYROIDISM\b': 'Blood Conditions',
        r'\bHYPERCARBIA\b': 'Blood Conditions',
        r'\bARTERIAL\b|\bATERIAL\b|\bARTERAL\b|\b[A]?VASCULAR\b': 'Blood Conditions',
        r'\bCOMPARTMENT SYNDROME\b': 'Blood Conditions',
        r'\bHCT DROP\b': 'Blood Conditions',
        r'\bHYPER[ ]?STIMULATION\b': 'Blood Conditions',
        r'\bHEMORRHAGIC|HEMORRHAGE\b': 'Blood Conditions',
        r'\bHYPOXEMIA\b': 'Blood Conditions',
        r'\bACIDOSIS\b': 'Blood Conditions',
        r'\bIPH\b|\bTTP\b|\bSMA\b|\bIVC\b|\bCFA\b|\bDIC\b|\bDVT\b|\bMVC\b|\bPVD\b|\bHTN\b|\bDKA\b': 'Blood Conditions',
        r'\bCOAGULOPATHY\b': 'Blood Conditions',
        r'\bCAVENOMA\b': 'Blood Conditions',
        r'\bELEVATED\b': 'Blood Conditions',
        r'\bATHERSCLEROSIS\b|\bARTHEROSCLEROSIS\b': 'Blood Conditions',
        r'\bRHABDO\b|\bRHABDOMYOLYSIS\b': 'Blood Conditions',
        r'\bTRIPLE A\b|\bAAA\b|\bTYPE A\b': 'Blood Conditions',
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
        r'\bHYPER[E]?GLYCEMIA\b|\bHYPOGLYCEMIA\b|\bHIGH BLOOD SUGAR\b|\bLOW BLOOD SUGAR\b': 'Blood Conditions',
        r'\bILIAC\b|': 'Blood Conditions',
        r'\bANASARCA\b': 'Blood Conditions',
        r'\bPHLEGMASIA\b': 'Blood Conditions',
        r'\bANEMIA\b': 'Blood Conditions',
        r'\bHYPERBILIRUBINEMIA\b|\bHYPERBILIRUBERIMIA\b': 'Blood Conditions',
        r'\bSICKLE CELL\b': 'Blood Conditions',
        r'\bANGIO\b': 'Blood Conditions',
        r'\bHYPERCALCEMIA\b': 'Blood Conditions',
        r'\bCAROTIS ARTERY STENOSIS\b': 'Blood Conditions',
        r'\bCLOTTED IV FISTULA\b': 'Blood Conditions',
        r'\bATHEROSCLEROSIS\b|\bARTHROSLOROSIS\b': 'Blood Conditions',
        r'\bULCER\b': 'Blood Conditions',
        r'\bLITHIUM\b|\bLI\b': 'Blood Conditions',
        r'\bMASTOCYTOSIS\b|\bSTENOSIS\b': 'Blood Conditions',
        r'\bNEUTROPENIA\b|\bPANCYTOPENIA\b': 'Blood Conditions',
        r'\bISCHEMIC\b|\bIS[C]?HEMIA\b': 'Blood Conditions',
        r'\bGANGRENE\b': 'Blood Conditions',
        r'\bVOLUME OVERLOAD\b': 'Blood Conditions',
        r'\bPERIPHERAL INSUFFICIENCY\b': 'Blood Conditions',
        r'\bMETHYLGLOBLUIN\b': 'Blood Conditions',
    }

    def categorize_diagnosis(diagnosis):
        if pd.isna(diagnosis) or not isinstance(diagnosis, str):
            return 'Other'
        
        for pattern, category in diagnosis_mapping.items():
            if re.search(pattern, diagnosis, re.IGNORECASE):
                return category
        return 'Other'
    
    df_transformed = df_column.apply(categorize_diagnosis)

    return df_transformed




    '''
    df_column = df_column.fillna('')
    for pattern, category in diagnosis_mapping.items():
        df_transformed = df_column.apply(lambda x: re.sub(pattern, category, x, flags = re.IGNORECASE))

    return df_transformed
    '''
