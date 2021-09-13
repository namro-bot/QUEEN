################################################################################
#This source code was auto-generated by 'quine' funtion of QUEEN 1.0.0.
#Project Name    :pCMV_Target_AID
#File Name       :output/pCMV-Target-AID_reconstruction.py
#Creation Date   :2021-08-26
################################################################################
project='pCMV_Target_AID'
import sys
sys.path.append("/Users/hideto/Dropbox (Yachie Lab)/HIDETO_MORI.LAB/Experiments/Project/Dbrick/github/demo/tutorial/../..")
from QUEEN.queen import *
from QUEEN import cutsite as cs
set_namespace(globals())

QUEEN(record='https://benchling.com/s/seq-cfnGDU0Mq8cUwn185LPF', dbtype='benchling', project='pcDNA_Target_AID', product='pcDNA_Target_AID', process_id='pCMV_Target_AID-EZbi1moI0C')
QUEEN(record='https://benchling.com/s/seq-K4HkSd2E8WiTAulJUeBf', dbtype='benchling', project='pCMV_ABE', product='pCMV_ABE', process_id='pCMV_Target_AID-rA2RRtBu3d')

process1={'name':'PCR', 'description':'The N-terminus of Target-AID (fragment1) was amplified from pcDNA3.1_pCMV-nCas-PmCDA1-ugi pH1-gRNA(HPRT) (Addgene 79620) using primer pairs RS045/HM129.'}
QUEEN(seq='GAGAGCCGCCACCATGGCACCGAAGAAGAAGCG', project='RS045', product='RS045', process_id='pCMV_Target_AID-WpgGb7XWl5', process_name=process1['name'], process_description=process1['description'])
QUEEN(seq='CTGGGGCACGATATGATCCACGTCGTAGTCGGAGA', project='HM129', product='HM129', process_id='pCMV_Target_AID-q3VxR7sxc2', process_name=process1['name'], process_description=process1['description'])
pcDNA_Target_AID.searchsequence(query=RS045.seq[-18:], product='FW1', process_id='pCMV_Target_AID-ncQKuKboBk', process_name=process1['name'], process_description=process1['description'])
pcDNA_Target_AID.searchsequence(query=HM129.seq[-18:], product='RV1', process_id='pCMV_Target_AID-Yhy8TvI76F', process_name=process1['name'], process_description=process1['description'])
cropdna(pcDNA_Target_AID, start=FW1[0].end, end=RV1[0].start, product='extract1', process_id='pCMV_Target_AID-3AjRaQxViH', process_name=process1['name'], process_description=process1['description'])
modifyends(extract1, left=RS045.seq, right=HM129.rcseq, product='fragment1', process_id='pCMV_Target_AID-tm34jxHzZx', process_name=process1['name'], process_description=process1['description'])

process2={'name':'PCR', 'description':'The C-terminus of Target-AID (fragment2) was amplified from pcDNA3.1_pCMV-nCas-PmCDA1-ugi pH1-gRNA(HPRT) (Addgene 79620) using primer pairs HM128/RS046.'}
QUEEN(seq='CTACGACGTGGATCATATCGTGCCCCAGTCTTTTC', project='HM128', product='HM128', process_id='pCMV_Target_AID-Pdu8Zk8Kcu', process_name=process2['name'], process_description=process2['description'])
QUEEN(seq='TTTAAACTCATTATAGCATCTTGATCTTGTTCTCTC', project='RS046', product='RS046', process_id='pCMV_Target_AID-a96XNwwKYV', process_name=process2['name'], process_description=process2['description'])
pcDNA_Target_AID.searchsequence(query=HM128.seq[-18:], product='FW2', process_id='pCMV_Target_AID-oBPkpzeOwc', process_name=process2['name'], process_description=process2['description'])
pcDNA_Target_AID.searchsequence(query=RS046.seq[-18:], product='RV2', process_id='pCMV_Target_AID-4NvpQbAVb8', process_name=process2['name'], process_description=process2['description'])
cropdna(pcDNA_Target_AID, start=FW2[0].end, end=RV2[0].start, product='extract2', process_id='pCMV_Target_AID-r6NI2fSBK4', process_name=process2['name'], process_description=process2['description'])
modifyends(extract2, left=HM128.seq, right=RS046.rcseq, product='fragment2', process_id='pCMV_Target_AID-bjx9zDibMA', process_name=process2['name'], process_description=process2['description'])

process3={'name':'PCR', 'description':'The backbone fragment was amplified from pCMV-ABE7.10 using RS047/RS048.'}
QUEEN(seq='ATCAAGATGCTATAATGAGTTTAAACCCGCTGATC', project='RS047', product='RS047', process_id='pCMV_Target_AID-xbYwpI6slr', process_name=process3['name'], process_description=process3['description'])
QUEEN(seq='CTTCGGTGCCATGGTGGCGGCTCTCCCTATAG', project='RS048', product='RS048', process_id='pCMV_Target_AID-uANRoOl8Yj', process_name=process3['name'], process_description=process3['description'])
pCMV_ABE.searchsequence(query=RS047.seq[-18:], product='FW3', process_id='pCMV_Target_AID-ZRzlemHnPL', process_name=process3['name'], process_description=process3['description'])
pCMV_ABE.searchsequence(query=RS048.seq[-18:], product='RV3', process_id='pCMV_Target_AID-OZqgFZtJ07', process_name=process3['name'], process_description=process3['description'])
cropdna(pCMV_ABE, start=FW3[0].end, end=RV3[0].start, product='extract3', process_id='pCMV_Target_AID-4Syq4DDNMa', process_name=process3['name'], process_description=process3['description'])
modifyends(extract3, left=RS047.seq, right=RS048.rcseq, product='fragment3', process_id='pCMV_Target_AID-nxOQby3rWS', process_name=process3['name'], process_description=process3['description'])

process4={'name':'Gibson Assembly', 'description':'The Target-AID plasmid (pCMV-Target-AID) was constructed by assembling two insert fragments and a backbone fragments.'}
modifyends(fragment1, left='*{25}/-{25}', right='-{28}/*{28}', product='fragment1_mod', process_id='pCMV_Target_AID-fNk9Pxad1N', process_name=process4['name'], process_description=process4['description'])
modifyends(fragment2, left='*{28}/-{28}', right='-{25}/*{25}', product='fragment2_mod', process_id='pCMV_Target_AID-V9witA8v4C', process_name=process4['name'], process_description=process4['description'])
modifyends(fragment3, left='*{25}/-{25}', right='-{25}/*{25}', product='fragment3_mod', process_id='pCMV_Target_AID-CGjYNsICes', process_name=process4['name'], process_description=process4['description'])
joindna(*[fragment1_mod, fragment2_mod, fragment3_mod], topology='circular', product='pCMV_Target_AID', process_id='pCMV_Target_AID-D3mSzAAq0h', process_name=process4['name'], process_description=process4['description'])
if __name__ == '__main__':
    check = quine(pCMV_Target_AID, author=None, project=project, _check=True)
    if check == True:
        pCMV_Target_AID.writedna()
