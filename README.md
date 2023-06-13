# Service Dependencies
Created by Ellen Lester and Ben Baker as part of the June 2023 Code Jam
Warning: this code is a rough draft and not a finalized product

## Use
This site can be used to view web maps dependent upon a specified service.
To use:
1. Run the app.py file
2. Open http://127.0.0.1:5000
3. Provide your Portal or AGOL URL, Username, and Password and click “Submit”
4. Wait until the page finishes loading (it is generating a list of services and maps)
5. Once available, select a service from the dropdown and click “Submit”
You will see a list of web maps that use this service. The service should also render on the Leaflet map at the bottom of the page. 

## Known Limitations
- By default, the script only assesses 10 maps and their services. This value is set on line 9 in GetMapsFromLayer.py and can be adjusted as desired. The larger the __max_items__ count, the longer it will take the script to run.
- Sometimes a service won’t load on the Leaflet map. Error "Bounds are not valid" displays in the developer console.
- As the user interacts with the web page, the URL changes. Refreshing the page from one of these URLs may lead to unexpected behavior.

## Suggested Improvements
- Find a more efficient way to pull map and service connections for an entire organization
- While maps and services are being queried, display a progress bar or text to indicate that the code is running
- Add CSV download option (currently a CSV is generated but it is for a random service and the CSV is not accessible through the user interface)
- Improve user display, so it doesn’t load empty sections of the page ("choose a service" option shouldn’t appear until after credentials have been provided, the map table shouldn’t appear until after a service is selected, etc.)
- Extend dependencies to include apps, dashboards, etc.
- Provide option to search the service list so user can find services of interest more quickly
- Improve general code functionality/formatting
- Provide log out option
- Improve aesthetics of the page
- Don't change the URL after the forms are submitted
- Fix the Leaflet map issue

