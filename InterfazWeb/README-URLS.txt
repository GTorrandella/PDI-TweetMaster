Urls que puede acceder el usuario:

/index: home de la app. 	-->index.html con enlaces a las URLs de abajo:

/Campaign:             -->Alta y Baja de Campaña. 
	/Campaign/Alta -->Alta de Campaña. AltaCampaign.html
	/Campaign/Baja -->Baja de Campaña. BajaCampaign.html
	/Campaign/Modificacion -->Modificacion de Campaña. ModifCampaign.html
	/GET/#CampaignID:  	-->Luego de hacer el alta. Hacer el html directamente con Flask que diga
	el status code correspondiente y el id de la campaña creada. (Ver los Status codes disponibles en /doc). 
	Por ej. si se creó satisfactoriamente --> "202 created. Campaña #IdCampaña creada."	
	/DELETE/#CampaignID:  	-->Luego de hacer la eliminación. Hacer el html directamente con Flask que diga
	el status code correspondiente y el id de la campaña eliminación. (Ver los Status codes disponibles en /doc).
	/PUT/#CampaignID:       -->Luego de indicar los campos a cambiar.

/Reporter:             -->Obtención del reporte.
	/GET/ReporterRaw  -->Obtención del reporte Raw.
	/GET/ReporterJSON -->Obtención del reporte JSON.
	[En estos 2 GET tambien se tendrían que mostrar los status codes como en los GET y DELETE de Campaign de arriba
	 --> estos están en SWAGGER. Hay que implementarlos con FLASK].

/doc: Documentacion de la API con Swagger.  --> 