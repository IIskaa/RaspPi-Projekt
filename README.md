# RaspPi-Projekt


1) Vi får börja med att installera pipenv med hjälp av pip. Bara en gång
	pip install --user pipenv
	

3)Sedan får vi initiera vår virtuella miljö i ett nytt projekt:


mkdir my_new_project
cd my_new_project
pipenv --python 3			eller	python -m pipenv --python 3 = skapar första gången miljön
pipenv install				varje gång vi vill skapa en versuella miljö
pipenv shell or pipenv run python	aktivera versutella miljö
python .... .py				köra våran python filen 


tillåter vesuel studio code att hitta automatiskt : 
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser



ctrl C 		döddar mosquetto. Används för att döda program
pipenv install matplotlib	
pipenv uninstall matplotlib	ta bort 


MOSQUITTO
pip3 install paho-mqtt 
oppna en ny terminal +
1)hitta				C:\Program Files\Mosquitto
2)kör				mosquitto.exe			//OBS! det kanske inte funkar isåfall kör kommando nedan.
3)hitta andra datorer och köra 	.\mosquitto.exe -v -c .\mosquitto.conf


Topics: ett sätt att skicka data från någonstans till en annan stans. I MQTT kallas det för topic asså ett ämne
	den identifera ett specifik meddelandeköer 

skickar: Publicera
ta emot: Prenumererar

wildcard	/+  wildcard för en topic-nivå
		/#  wildcard för flera nivåer på slutet. 

