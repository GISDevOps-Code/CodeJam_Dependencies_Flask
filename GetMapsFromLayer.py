
from arcgis.gis import GIS
from arcgis.mapping import WebMap

def getMapsFromLayer(portal_url, username, pw):
    service_dict = {}
    portal = GIS(portal_url, username, pw, verify_cert=True)
    token = portal._con.token
    web_map_items = portal.content.search(query="*", item_type="Web Map", max_items=10)
    for item in web_map_items:
        wm = WebMap(item)
        print(item.get_data)

        map_details = {'ItemID' : item.id,
                                    'Name' : item.title,
                                    'Tags' : item.tags,
                                    'Description' : item.description,
                                    'Type' : 'Web Map',
                                    'Link' : item.homepage,
                                    'Owner': item.owner,
                                    'Sharing': item.access,
                                    'LastUpdate' : item.modified,
                                    'NumberOfViews' : item.numViews
                                 }
        lyrs = wm.layers
        for lyr in lyrs:
            if hasattr(lyr, 'url'):
                lyr_url = lyr.url
            elif hasattr(lyr, 'styleUrl'):
                lyr_url = lyr.styleUrl
            else:
                lyr_url = None
                
            if lyr_url is not None:
                if lyr_url not in service_dict:
                    service_dict[lyr_url] = [map_details]
                else:
                    service_dict[lyr_url].append(map_details)
    return(service_dict, token)




            
