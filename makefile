populate: runPhoneCall.sh autoNumber.py
	@echo "POPULATING"
	./runPhoneCall.sh
	@echo "AUTO STARTUP"
	python3 autoNumber.py
.PHONY: clean
clean:
	rm -f CALLINFO.txt 
	make populate