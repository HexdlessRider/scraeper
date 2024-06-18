import asyncio
import os
import time
import json

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from core.engine import fetch_url


async def scrape_data(file_name: str):
    url = "https://www.woningnetregioamsterdam.nl/screenservices/DAKWP/Overzicht/Woningaanbod/DataActionHaalPassendAanbod"
    headers = {
        "accept": "application/json",
        "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/json; charset=UTF-8",
        "cookie": (
            "osVisitor=76a898b9-12ba-4b6f-911c-575f29bfdd3f; nr1Users=lid%3dAnonymous%3btuu%3d0%3bexp%3d0%3brhs%3dXBC1ss1nOgYW1SmqUjSxLucVOAg%3d%3bhmc%3dR6xQp6rNWPVAnyO7ESEh1iZLFx4%3d; "
            "nr2Users=crf%3dT6C%2b9iB49TLra4jEsMeSckDMNhQ%3d%3buid%3d0%3bunm%3d; "
            'CookieScriptConsent={"action":"accept","categories":"[\\"targeting\\"]"}; '
            "_ga=GA1.1.1280024582.1717676395; osVisit=2da5e3ce-4861-4665-a94a-774aec2fe39f"),
        "origin": "https://www.woningnetregioamsterdam.nl",
        "outsystems-locale": "nl-NL",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.woningnetregioamsterdam.nl/Woningaanbod",
        "sec-ch-ua": "\"Chromium\";v=\"124\", \"Opera\";v=\"110\", \"Not-A.Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0",
        "x-csrftoken": "T6C+9iB49TLra4jEsMeSckDMNhQ="
    }
    payload = {"versionInfo":{"moduleVersion":"W_P6MqvtkSAbxNaPdZRd6A","apiVersion":"ELSJ6at_o6i4dQ5obAqehg"},"viewName":"Overzicht.Woningaanbod","screenData":{"variables":{"PublicatieList":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"HuidigeSorteringDisplayTekst":"Oppervlakte","VerbergFilterSorteer":False,"Platform":"","PlatformVersie":"","PublicatieListAanbod":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"PublicatieListLoting":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"PublicatieListVrijeSector":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"PublicatieListParkerenOverig":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"PublicatieListKoop":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"ActiefTabblad":0,"FilterAantalActief":0,"IsGeenSpecifiekeDoelgroep":False,"PublicatieLabelList":{"List":[],"EmptyListItem":{"Label":"","IsActief":False}},"PublicatieListVoldoetAaanPublicatieLabelFilter":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"FilterBekijkWoningenAantal":0,"PublicatieListEmpty":{"List":[],"EmptyListItem":{"Id":"0","EinddatumTijd":"1900-01-01T00:00:00","PublicatieModel":"","PublicatieModule":"","PublicatieDatum":"1900-01-01T00:00:00","Matchpercentage":0,"VoorlopigePositie":"0","Foto_Locatie":"","GepersonaliseerdeHuur":"0","IsCluster":False,"EenheidSoort":"","Adres":{"Straatnaam":"","Huisnummer":0,"Huisletter":"","HuisnummerToevoeging":"","Postcode":"","Woonplaats":"","Wijk":"","PublicatieId":"0"},"Cluster":{"Naam":"","DetailSoort":"","Doelgroep":"","PrijsMinBekend":False,"PrijsMin":"0","PrijsMaxBekend":False,"PrijsMax":"0","WoonOppervlakteMinBekend":False,"WoonVertrekkenTotOppMin":0,"WoonOppervlakteMaxBekend":False,"WoonVertrekkenTotOppMax":0,"AantalEenheden":0,"AantalKamersMin":0,"AantalKamersMax":0,"Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","Eigenaar":""},"Eenheid":{"DetailSoort":"","Bestemming":"","AantalKamers":0,"TotaleOppervlakte":"0","WoonVertrekkenTotOpp":"0","Doelgroep":"","NettoHuurBekend":False,"NettoHuur":"0","Lengtegraad":"0","Breedtegraad":"0","Toegankelijkheidstag":"","PublicatieId":"0","SoortBouw":"","EnergieLabel":"","EnergieIndex":0,"Eigenaar":"","BrutoHuurBekend":False,"Brutohuur":"0","SubsidiabeleHuur":"0"},"PublicatieLabel":"","IsBewaard":False,"IsVerborgen":False,"ContractVorm":"","PublicatieOmschrijving":{"Id":"0","Tekst":None},"AantalReactiesOpPublicatie":"0","HeeftGereageerd":False,"IsIntrekkenReactieToegestaan":False,"RedenNietIntrekkenReactie":"","PositieAanbiedingsproces":"","VirtuelePositie":0}},"ShowPopup":False,"BekijkWoningenAantalOud":0,"PublicatieIdsList":{"List":[],"EmptyListItem":"0"},"IsVoorlopigePositieBeschikbaar":True,"HuidigePublicatieId":"0","_huidigePublicatieIdInDataFetchStatus":1}},"clientVariables":{"EnableDarkMode":False,"BerichtVerwijderenActief":False,"ClientLogEnabled":False,"IsVerbergenVraagNietMeer":False,"MoetInschrijfKostenBetalen":False,"SamenwerkingsverbandId":"2","OpleidingWRBOmschrijving":"","CacheVariant":1,"ZoekAanbod":"","RegelingWRBNaam":"","SessionToken":"","QiiInProfiel":False,"LastURL":"","IsVerbergKaart":False,"InschrijvenVoortzettenMogelijk":False,"RegelingIsCompleet":False,"IsWeergavePuntenteller":False,"SamenwerkingsverbandNaam":"Regio Amsterdam","IsGeenVerlengingBetalenNodig":False,"OpleidingWRBNaam":"","HuidigeSorteringAanbodIsAflopend":True,"OpleidingIsCompleet":False,"WoonwensFilterIsEis":False,"MaandenHistorie":-36,"QiiKeuzeRelatiegroepStatusCodeId":0,"IsWeergaveEinddatum":True,"CheckProfielPanelenVoorPopup":True,"PublicatieLabelFilters":"","ToonNieuweProfielBerichten":False,"HuidigeSorteringAanbodId":3,"RegelingWRBOmschrijving":"","Username":"","AanbodPublicatieLabelFilters":"[]"}}

    site_data = await fetch_url('POST', url, 1, payload=payload, headers=headers)

    if not site_data:
        return

    data = json.loads(site_data)

    result = [{
        'url': 'https://www.woningnetregioamsterdam.nl/HuisDetails?PublicatieId=' + elm['Id'],
        'rent_price': float(elm['GepersonaliseerdeHuur']),
        'square_meters': elm['Eenheid']['WoonVertrekkenTotOpp'],
        'bedrooms': elm['Eenheid']['AantalKamers'],
        'location': f"{elm['Adres']['Woonplaats']}, {elm['Adres']['Straatnaam']} {elm['Adres']['Huisnummer']}",
        # clear_info # ???
    } for elm in data['data']['PublicatieLijst']['List']]
    # print(result)
    # print(len(result))
    if result:
        await ApartmentStore.create_or_update_apartment(result, file_name)
        # await check uniq result (service class in db)
        # await store uniq result (service class in db )
        # wait next function call
        pass


async def main():
    script_path = os.path.abspath(__file__)
    script_name = (os.path.basename(script_path)).split('.')[0]
    while True:
        await scrape_data(file_name=script_name)
        await asyncio.sleep(VESTEDA_CD)


if __name__ == "__main__":
    asyncio.run(main())
