# Installation of package VLS_AMMP_MinMolecules.

EXE = mol2_to_templ_sp4 mol2_to_templ_sp5 renumb_ligand save_energy ammp_to_mol2 
PY =  AMMOS_SmallMol_sp4.py AMMOS_SmallMol_sp5.py 
BIN = ../../bin

all :
	echo "Installation of AMMP program"
	cd ../progs/ammp; rm *.o; make -e ammp; cp ammp ammp_nongraph; mv ammp_nongraph $(BIN);
	echo ""; echo ""; echo ""

	echo "Installation of PREAMMP program"	
	cd ../progs/preammp; rm *.o; make -e presp4; cp presp4 preammp; mv preammp $(BIN);
	echo ""; echo ""; echo "";


	echo "Installation of VLS_AMMP package_MinMolecules"
	cd ../progs/vls_min; rm *.o; make -e all
	cd ../progs/vls_min; mv $(EXE) $(BIN);
	cd ../progs/Python_scripts; cp $(PY) $(BIN);
